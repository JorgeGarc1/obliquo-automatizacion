"""
Web Search Module
Searches for additional relevant information from the web.
"""

import requests
from bs4 import BeautifulSoup
import time

class WebSearch:
    """Handles web searches for additional information"""

    def __init__(self, config):
        self.api_key = config['api_key']
        self.search_engine_id = config['search_engine_id']
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def search_related_info(self, key_ideas):
        """Search for additional information related to key ideas"""
        additional_info = []

        for idea in key_ideas[:5]:  # Limit to top 5 ideas to avoid rate limits
            print(f"Searching for: {idea}")
            results = self._google_search(idea)
            additional_info.extend(results)
            time.sleep(1)  # Rate limiting

        return additional_info

    def _google_search(self, query):
        """Perform Google Custom Search"""
        params = {
            'key': self.api_key,
            'cx': self.search_engine_id,
            'q': query,
            'num': 5  # Get top 5 results
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            results = []
            for item in data.get('items', []):
                results.append({
                    'title': item['title'],
                    'snippet': item['snippet'],
                    'url': item['link'],
                    'query': query
                })

            return results

        except requests.RequestException as e:
            print(f"Search failed for query '{query}': {e}")
            return []

    def search_specialized_documents(self, topics):
        """Search for specialized documents and books"""
        specialized_info = []

        for topic in topics[:3]:  # Limit to top 3 topics
            query = f"{topic[0]} business book OR document OR research"
            results = self._google_search(query)
            specialized_info.extend(results)

        return specialized_info