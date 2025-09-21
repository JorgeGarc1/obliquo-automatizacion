#!/usr/bin/env python3
"""
Business Content Agent - Main Entry Point
Automates the process of analyzing business information from Google Drive,
generating audiovisual content script ideas, and iteratively improving based on feedback.
"""

import os
import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.drive_access import GoogleDriveAccess
from src.text_processor import TextProcessor
from src.web_search import WebSearch
from src.form_handler import FormHandler
from src.business_analyzer import BusinessAnalyzer
from src.audience_analyzer import AudienceAnalyzer
from src.script_generator import ScriptGenerator
from src.ui import UserInterface

def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent / 'config' / 'config.json'
    with open(config_path, 'r') as f:
        return json.load(f)

def main():
    """Main execution flow"""
    print("Starting Business Content Agent...")

    # Load configuration
    config = load_config()

    # Initialize components
    drive_access = GoogleDriveAccess(config['google_drive'])
    text_processor = TextProcessor(config['nlp'])
    web_search = WebSearch(config['web_search'])
    form_handler = FormHandler()
    business_analyzer = BusinessAnalyzer()
    audience_analyzer = AudienceAnalyzer()
    script_generator = ScriptGenerator()
    ui = UserInterface(config['ui'])

    # Step 1: Access Google Drive and extract business information
    print("Accessing Google Drive repository...")
    documents = drive_access.get_documents()

    # Step 2: Process documents to understand context and key ideas
    print("Processing documents...")
    processed_data = text_processor.process_documents(documents)

    # Step 3: Search for additional relevant information
    print("Searching for additional information...")
    additional_info = web_search.search_related_info(processed_data['key_ideas'])

    # Step 4: Request additional information if needed
    print("Checking if additional information is needed...")
    if not business_analyzer.has_sufficient_info(processed_data, additional_info):
        additional_data = form_handler.request_additional_info()
        processed_data.update(additional_data)

    # Step 5: Perform business topological analysis
    print("Performing business analysis...")
    business_analysis = business_analyzer.analyze_business(processed_data, additional_info)

    # Step 6: Analyze target audience
    print("Analyzing target audience...")
    audience_profile = audience_analyzer.analyze_audience(business_analysis)

    # Step 7: Generate 40 script ideas
    print("Generating script ideas...")
    script_ideas = script_generator.generate_ideas(business_analysis, audience_profile, 40)

    # Step 8: Present ideas to user and collect feedback
    print("Presenting ideas to user...")
    selected_ideas, feedback = ui.present_ideas_and_get_feedback(script_ideas)

    # Step 9: Iterative improvement loop
    while feedback and feedback.get('improve', False):
        print("Improving based on feedback...")
        improved_ideas = script_generator.improve_ideas(selected_ideas, feedback)
        selected_ideas, feedback = ui.present_ideas_and_get_feedback(improved_ideas)

    print("Process completed successfully!")

if __name__ == "__main__":
    main()