"""
Form Handler Module
Manages forms for requesting additional information from users.
"""

class FormHandler:
    """Handles user forms for additional information"""

    def __init__(self):
        self.questions = [
            "What is the primary target market for your business?",
            "What are your main competitors?",
            "What is your unique value proposition?",
            "What are your business goals for the next year?",
            "Who is your ideal customer persona?",
            "What cultural aspects are important for your audience?",
            "What tone should the content have (formal, casual, professional, etc.)?",
            "Are there any specific topics you want to avoid?"
        ]

    def request_additional_info(self):
        """Present form to user and collect responses"""
        print("\n" + "="*50)
        print("ADDITIONAL INFORMATION REQUESTED")
        print("="*50)
        print("Please provide the following information to improve analysis:")

        responses = {}
        for i, question in enumerate(self.questions, 1):
            print(f"\n{i}. {question}")
            response = input("> ").strip()
            if response:
                responses[f"question_{i}"] = response

        print("\nThank you for providing additional information!")
        return responses

    def get_missing_info_questions(self, analysis_result):
        """Generate specific questions based on analysis gaps"""
        missing_questions = []

        if 'target_market' not in analysis_result:
            missing_questions.append("What is your primary target market?")

        if 'competitors' not in analysis_result:
            missing_questions.append("Who are your main competitors?")

        if 'value_proposition' not in analysis_result:
            missing_questions.append("What makes your business unique?")

        return missing_questions