"""
Google Drive Access Module
Handles authentication and document retrieval from Google Drive.
"""

import os
import io
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GoogleDriveAccess:
    """Handles Google Drive API interactions"""

    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    def __init__(self, config):
        self.config = config
        self.creds = None
        self.service = None
        self.authenticate()

    def authenticate(self):
        """Authenticate with Google Drive API"""
        creds_path = Path(self.config['credentials_path'])
        token_path = Path(self.config['token_path'])

        if token_path.exists():
            self.creds = Credentials.from_authorized_user_file(str(token_path), self.SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                if not creds_path.exists():
                    raise FileNotFoundError(f"Credentials file not found: {creds_path}")

                flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), self.SCOPES)
                self.creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(token_path, 'w') as token:
                token.write(self.creds.to_json())

        self.service = build('drive', 'v3', credentials=self.creds)

    def get_documents(self):
        """Retrieve documents from the specified Google Drive folder"""
        folder_id = self.config['folder_id']
        documents = []

        # Query for files in the folder
        query = f"'{folder_id}' in parents and mimeType contains 'text/'"
        results = self.service.files().list(
            q=query,
            fields="nextPageToken, files(id, name, mimeType)"
        ).execute()

        items = results.get('files', [])

        for item in items:
            print(f"Downloading: {item['name']}")
            content = self._download_file(item['id'])
            documents.append({
                'name': item['name'],
                'content': content,
                'type': item['mimeType']
            })

        return documents

    def _download_file(self, file_id):
        """Download a file's content"""
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while done is False:
            status, done = downloader.next_chunk()

        fh.seek(0)
        return fh.read().decode('utf-8')