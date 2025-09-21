#!/usr/bin/env python3
"""
Test script to check if all modules can be imported successfully.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print('Testing imports...')

modules_to_test = [
    ('drive_access', 'Google Drive integration'),
    ('text_processor', 'Text processing with NLP'),
    ('web_search', 'Web search functionality'),
    ('form_handler', 'Form handling for user input'),
    ('business_analyzer', 'Business topological analysis'),
    ('audience_analyzer', 'Audience characteristic analysis'),
    ('script_generator', 'Script idea generation'),
    ('ui', 'User interface')
]

all_passed = True

for module_name, description in modules_to_test:
    try:
        __import__(module_name)
        print(f'✓ {module_name} - {description}')
    except ImportError as e:
        print(f'✗ {module_name} - {description}: {e}')
        all_passed = False
    except Exception as e:
        print(f'⚠ {module_name} - {description}: Unexpected error: {e}')
        all_passed = False

if all_passed:
    print('\n🎉 All modules imported successfully!')
else:
    print('\n❌ Some modules failed to import. Check dependencies.')

print('\nTesting main script import...')
try:
    import main
    print('✓ main.py imported successfully')
except ImportError as e:
    print(f'✗ main.py import failed: {e}')
    all_passed = False

if all_passed:
    print('\n✅ Project is ready to run!')
else:
    print('\n❌ Project has issues that need to be resolved.')