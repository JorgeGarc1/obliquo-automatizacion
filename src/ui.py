"""
User Interface Module
Provides web interface for presenting ideas and collecting feedback.
"""

from flask import Flask, render_template_string, request, jsonify
import json
from typing import List, Dict, Tuple

class UserInterface:
    """Web-based user interface for the agent"""

    def __init__(self, config):
        self.config = config
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        """Set up Flask routes"""

        @self.app.route('/')
        def index():
            return render_template_string(self._get_main_template())

        @self.app.route('/api/ideas', methods=['POST'])
        def get_ideas():
            ideas = request.json.get('ideas', [])
            return jsonify({'ideas': ideas})

        @self.app.route('/api/feedback', methods=['POST'])
        def collect_feedback():
            feedback = request.json
            return jsonify({'status': 'feedback_received', 'feedback': feedback})

    def present_ideas_and_get_feedback(self, ideas: List[Dict]) -> Tuple[List[Dict], Dict]:
        """Present ideas to user and collect feedback"""
        print(f"\nGenerated {len(ideas)} script ideas!")
        print("Starting web interface for idea selection and feedback...")

        # For this implementation, we'll use a simple console-based selection
        # In a full implementation, this would launch the Flask app
        selected_ideas = self._console_selection(ideas)
        feedback = self._collect_console_feedback(selected_ideas)

        return selected_ideas, feedback

    def _console_selection(self, ideas: List[Dict]) -> List[Dict]:
        """Console-based idea selection"""
        print("\n" + "="*80)
        print("SCRIPT IDEAS GENERATED")
        print("="*80)

        selected = []
        for idea in ideas[:10]:  # Show first 10 for selection
            print(f"\nID: {idea['id']}")
            print(f"Title: {idea['title']}")
            print(f"Format: {idea['format']}")
            print(f"Theme: {idea['theme']}")
            print(f"Description: {idea['description']}")
            print(f"Duration: {idea['estimated_duration']}")
            print(f"Platforms: {', '.join(idea['target_platforms'])}")

            choice = input("Select this idea? (y/n): ").lower().strip()
            if choice == 'y':
                selected.append(idea)

        return selected

    def _collect_console_feedback(self, selected_ideas: List[Dict]) -> Dict:
        """Collect feedback via console"""
        if not selected_ideas:
            return {}

        print("\n" + "="*50)
        print("FEEDBACK COLLECTION")
        print("="*50)

        feedback = {
            'rating': input("Rate the selected ideas (1-5): ").strip(),
            'improvements': input("What improvements would you like?: ").strip(),
            'tone_change': input("Preferred tone change (leave empty for none): ").strip(),
            'format_change': input("Preferred format change (leave empty for none): ").strip(),
            'additional_elements': input("Additional elements to include: ").strip().split(','),
            'improve': input("Generate improved versions? (y/n): ").lower().strip() == 'y'
        }

        # Clean up empty fields
        feedback = {k: v for k, v in feedback.items() if v and v != []}

        return feedback

    def _get_main_template(self) -> str:
        """Get HTML template for web interface"""
        return """
<!DOCTYPE html>
<html>
<head>
    <title>Business Content Agent</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .idea { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .selected { background-color: #e8f5e8; }
        button { padding: 10px 15px; margin: 5px; cursor: pointer; }
        .feedback { background-color: #f9f9f9; padding: 15px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Business Content Agent - Script Ideas</h1>
    <div id="ideas-container"></div>
    <div class="feedback">
        <h3>Provide Feedback</h3>
        <textarea id="feedback-text" rows="4" cols="50" placeholder="Enter your feedback..."></textarea><br>
        <button onclick="submitFeedback()">Submit Feedback</button>
    </div>

    <script>
        let selectedIdeas = [];

        function displayIdeas(ideas) {
            const container = document.getElementById('ideas-container');
            container.innerHTML = '';

            ideas.forEach(idea => {
                const div = document.createElement('div');
                div.className = 'idea';
                div.innerHTML = `
                    <h3>${idea.title}</h3>
                    <p><strong>Format:</strong> ${idea.format}</p>
                    <p><strong>Theme:</strong> ${idea.theme}</p>
                    <p>${idea.description}</p>
                    <p><strong>Duration:</strong> ${idea.estimated_duration}</p>
                    <p><strong>Platforms:</strong> ${idea.target_platforms.join(', ')}</p>
                    <button onclick="selectIdea(${idea.id})">Select</button>
                `;
                container.appendChild(div);
            });
        }

        function selectIdea(id) {
            if (selectedIdeas.includes(id)) {
                selectedIdeas = selectedIdeas.filter(i => i !== id);
            } else {
                selectedIdeas.push(id);
            }
            updateSelections();
        }

        function updateSelections() {
            document.querySelectorAll('.idea').forEach(div => {
                const button = div.querySelector('button');
                const id = parseInt(button.onclick.toString().match(/\\d+/)[0]);
                if (selectedIdeas.includes(id)) {
                    div.classList.add('selected');
                    button.textContent = 'Selected';
                } else {
                    div.classList.remove('selected');
                    button.textContent = 'Select';
                }
            });
        }

        function submitFeedback() {
            const feedback = document.getElementById('feedback-text').value;
            fetch('/api/feedback', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    selected_ideas: selectedIdeas,
                    feedback: feedback,
                    improve: true
                })
            });
            alert('Feedback submitted!');
        }

        // Load ideas on page load
        window.onload = function() {
            // This would be populated with actual ideas
            displayIdeas([]);
        };
    </script>
</body>
</html>
        """

    def run_web_app(self):
        """Run the Flask web application"""
        self.app.run(debug=True, port=self.config['port'])