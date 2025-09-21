#!/usr/bin/env python3
"""
Test script to check if main.py can start without errors.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_main_imports():
    """Test if main.py imports work"""
    try:
        from src.drive_access import GoogleDriveAccess
        from src.text_processor import TextProcessor
        from src.web_search import WebSearch
        from src.form_handler import FormHandler
        from src.business_analyzer import BusinessAnalyzer
        from src.audience_analyzer import AudienceAnalyzer
        from src.script_generator import ScriptGenerator
        from src.ui import UserInterface
        print("✓ All main imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_config_loading():
    """Test if config can be loaded"""
    try:
        import json
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.json')
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✓ Config loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Config loading error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality without external dependencies"""
    try:
        from src.business_analyzer import BusinessAnalyzer
        from src.audience_analyzer import AudienceAnalyzer
        from src.script_generator import ScriptGenerator

        # Test business analyzer
        analyzer = BusinessAnalyzer()
        mock_data = {
            'full_text': 'This is a test business that sells products online.',
            'key_ideas': ['online sales', 'product selling'],
            'entities': ['business'],
            'topics': [('sales', 5), ('products', 3)]
        }
        result = analyzer.analyze_business(mock_data, [])
        print("✓ Business analyzer works")

        # Test audience analyzer
        audience_analyzer = AudienceAnalyzer()
        audience_result = audience_analyzer.analyze_audience(result)
        print("✓ Audience analyzer works")

        # Test script generator
        script_gen = ScriptGenerator()
        scripts = script_gen.generate_ideas(result, audience_result, 5)
        print(f"✓ Script generator works (generated {len(scripts)} ideas)")

        return True
    except Exception as e:
        print(f"✗ Functionality test error: {e}")
        return False

if __name__ == "__main__":
    print("Testing Business Content Agent...")
    print("=" * 40)

    tests = [
        ("Main imports", test_main_imports),
        ("Config loading", test_config_loading),
        ("Basic functionality", test_basic_functionality)
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\nRunning: {test_name}")
        if test_func():
            passed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! The agent is ready to run.")
        print("\nNote: Full functionality requires:")
        print("- Google Drive API credentials (credentials.json)")
        print("- Google Custom Search API key")
        print("- A Google Drive folder with business documents")
    else:
        print("❌ Some tests failed. Please check the errors above.")