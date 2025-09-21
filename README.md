# Business Content Agent

An automated Python agent that analyzes business information from Google Drive, performs topological business analysis, and generates 40 audiovisual content script ideas tailored to the target audience.

## Features

- **Google Drive Integration**: Accesses business documents from a specified Google Drive folder
- **Text Processing**: Uses NLP to extract context, key ideas, and entities from documents
- **Web Research**: Searches for additional relevant information from the internet
- **Business Analysis**: Performs topological analysis of business structure and relationships
- **Audience Analysis**: Determines optimal tone, language, and cultural elements for content
- **Script Generation**: Creates 40 unique audiovisual content ideas
- **User Interaction**: Collects additional information via forms and feedback for iterative improvement

## Setup

### 1. Install Dependencies

```bash
cd business_content_agent
pip install -r requirements.txt
```

### 2. Google Drive API Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Drive API
4. Create credentials (OAuth 2.0 Client ID)
5. Download the credentials JSON file and place it in the project root as `credentials.json`
6. The first run will prompt for authentication and create `token.json`

### 3. Configure the Agent

Edit `config/config.json`:

```json
{
  "google_drive": {
    "credentials_path": "credentials.json",
    "token_path": "token.json",
    "folder_id": "YOUR_GOOGLE_DRIVE_FOLDER_ID"
  },
  "web_search": {
    "api_key": "YOUR_GOOGLE_SEARCH_API_KEY",
    "search_engine_id": "YOUR_CUSTOM_SEARCH_ENGINE_ID"
  },
  "nlp": {
    "model": "en_core_web_sm"
  },
  "ui": {
    "port": 5000
  }
}
```

### 4. Google Custom Search API Setup (Optional)

For enhanced web research capabilities:

1. Enable Custom Search API in Google Cloud Console
2. Create a Custom Search Engine at [cse.google.com](https://cse.google.com)
3. Get your Search Engine ID and API Key

## Usage

### Basic Execution

```bash
python main.py
```

The agent will:

1. Authenticate with Google Drive
2. Download and process business documents
3. Extract key ideas and context
4. Search for additional information
5. Request additional details if needed
6. Perform business topological analysis
7. Analyze target audience characteristics
8. Generate 40 script ideas
9. Present ideas for selection
10. Collect feedback for iterative improvement

### Web Interface

The agent includes a Flask-based web interface for better user interaction. To run it separately:

```python
from src.ui import UserInterface
import json

with open('config/config.json') as f:
    config = json.load(f)

ui = UserInterface(config['ui'])
ui.run_web_app()
```

## Project Structure

```
business_content_agent/
├── config/
│   └── config.json          # Configuration settings
├── src/
│   ├── __init__.py
│   ├── drive_access.py      # Google Drive integration
│   ├── text_processor.py    # NLP text processing
│   ├── web_search.py        # Web research functionality
│   ├── form_handler.py      # User form handling
│   ├── business_analyzer.py # Business topological analysis
│   ├── audience_analyzer.py # Audience characteristic analysis
│   ├── script_generator.py  # Content idea generation
│   └── ui.py                # User interface
├── main.py                  # Main execution script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Key Components

### Business Topological Analysis

The agent performs a comprehensive analysis of:
- Business structure and type
- Market relationships and positioning
- Value network and stakeholders
- Growth opportunities and challenges

### Audience Analysis

Determines:
- Target demographics
- Preferred tone (professional, casual, inspirational, etc.)
- Language style (simple, technical, storytelling, etc.)
- Cultural elements and communication preferences

### Script Generation

Creates 40 unique content ideas combining:
- Various content formats (videos, testimonials, tutorials, etc.)
- Different themes and angles
- Platform-specific optimizations
- Audience-tailored messaging

## Requirements

- Python 3.8+
- Google Drive API credentials
- Internet connection for web research
- spaCy language model (automatically downloaded)

## License

This project is provided as-is for educational and business purposes.