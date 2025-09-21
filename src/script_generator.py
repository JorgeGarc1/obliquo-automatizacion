"""
Script Generator Module
Generates audiovisual content script ideas based on business analysis and audience profile.
"""

import random
from typing import List, Dict

class ScriptGenerator:
    """Generates script ideas for audiovisual content"""

    def __init__(self):
        self.content_formats = [
            'educational video', 'testimonial', 'product demo', 'behind-the-scenes',
            'customer story', 'expert interview', 'tutorial', 'case study',
            'motivational talk', 'Q&A session', 'live stream', 'short clip',
            'documentary style', 'animated explanation', 'vlog', 'webinar'
        ]

        self.themes = [
            'success story', 'problem-solution', 'day in the life', 'transformation',
            'expert insights', 'industry trends', 'tips and tricks', 'myth busting',
            'comparison', 'future vision', 'historical perspective', 'current events',
            'personal journey', 'team spotlight', 'innovation showcase', 'community impact'
        ]

        self.angles = [
            'emotional connection', 'practical value', 'entertainment', 'education',
            'inspiration', 'controversy', 'uniqueness', 'urgency', 'social proof',
            'authority', 'exclusivity', 'simplicity', 'innovation', 'tradition'
        ]

    def generate_ideas(self, business_analysis: Dict, audience_profile: Dict, count: int = 40) -> List[Dict]:
        """Generate script ideas for audiovisual content"""
        ideas = []

        # Extract key elements from analysis
        key_topics = self._extract_key_topics(business_analysis)
        target_tone = audience_profile.get('tone', 'professional')
        target_language = audience_profile.get('language', 'simple')
        cultural_elements = audience_profile.get('cultural_elements', [])
        comm_prefs = audience_profile.get('communication_preferences', [])

        for i in range(count):
            idea = self._generate_single_idea(
                i + 1,
                key_topics,
                target_tone,
                target_language,
                cultural_elements,
                comm_prefs
            )
            ideas.append(idea)

        return ideas

    def _generate_single_idea(self, idea_number: int, key_topics: List[str],
                            tone: str, language: str, cultural_elements: List[str],
                            comm_prefs: List[str]) -> Dict:
        """Generate a single script idea"""
        # Randomly select components
        format_type = random.choice(self.content_formats)
        theme = random.choice(self.themes)
        angle = random.choice(self.angles)
        topic = random.choice(key_topics) if key_topics else "business topic"

        # Generate title
        title = self._generate_title(format_type, theme, topic, angle)

        # Generate description
        description = self._generate_description(
            format_type, theme, topic, angle, tone, language, cultural_elements
        )

        # Generate key elements
        key_elements = self._generate_key_elements(format_type, comm_prefs)

        return {
            'id': idea_number,
            'title': title,
            'format': format_type,
            'theme': theme,
            'angle': angle,
            'topic': topic,
            'description': description,
            'key_elements': key_elements,
            'estimated_duration': self._estimate_duration(format_type),
            'target_platforms': self._suggest_platforms(format_type, comm_prefs)
        }

    def _extract_key_topics(self, business_analysis: Dict) -> List[str]:
        """Extract key topics from business analysis"""
        topics = []

        # Get topics from structure
        structure = business_analysis.get('structure', {})
        if 'key_components' in structure:
            topics.extend([topic[0] for topic in structure['key_components'][:5]])

        # Get topics from market position
        market_pos = business_analysis.get('market_position', {})
        if 'unique_selling_points' in market_pos:
            topics.extend(market_pos['unique_selling_points'][:3])

        # Get topics from value network
        value_net = business_analysis.get('value_network', {})
        if 'stakeholders' in value_net:
            topics.extend(value_net['stakeholders'][:2])

        return topics if topics else ['business growth', 'customer success', 'innovation']

    def _generate_title(self, format_type: str, theme: str, topic: str, angle: str) -> str:
        """Generate an engaging title"""
        title_templates = [
            f"How {topic} {angle} Changed Everything",
            f"The {angle} Side of {topic}",
            f"{theme.title()}: A {topic} Story",
            f"Unlocking {topic} Through {angle}",
            f"{format_type.title()}: {topic} {theme}",
            f"Discover {angle} in {topic}",
            f"{topic} {theme}: What You Need to Know",
            f"From {angle} to Success: {topic}"
        ]

        return random.choice(title_templates)

    def _generate_description(self, format_type: str, theme: str, topic: str,
                            angle: str, tone: str, language: str,
                            cultural_elements: List[str]) -> str:
        """Generate detailed description"""
        description = f"This {format_type} explores {theme} in {topic}, "

        if angle:
            description += f"focusing on the {angle} aspect. "

        if tone:
            description += f"The content uses a {tone} tone "

        if language:
            description += f"with {language} language "

        if cultural_elements:
            culture_str = ", ".join(cultural_elements)
            description += f"incorporating {culture_str} cultural elements. "

        description += "Perfect for engaging your target audience and driving action."

        return description

    def _generate_key_elements(self, format_type: str, comm_prefs: List[str]) -> List[str]:
        """Generate key elements for the script"""
        elements = []

        # Format-specific elements
        if 'video' in format_type:
            elements.extend(['strong opening hook', 'visual demonstrations', 'clear call-to-action'])
        elif 'interview' in format_type:
            elements.extend(['expert introduction', 'key questions', 'actionable insights'])
        elif 'tutorial' in format_type:
            elements.extend(['step-by-step instructions', 'visual aids', 'practice exercises'])

        # Communication preference elements
        if 'visual content' in comm_prefs:
            elements.append('compelling visuals')
        if 'video content' in comm_prefs:
            elements.append('dynamic video elements')

        # Default elements
        elements.extend(['engaging narrative', 'clear messaging', 'audience-focused content'])

        return list(set(elements))  # Remove duplicates

    def _estimate_duration(self, format_type: str) -> str:
        """Estimate content duration"""
        duration_map = {
            'short clip': '15-30 seconds',
            'testimonial': '1-2 minutes',
            'tutorial': '3-5 minutes',
            'interview': '5-10 minutes',
            'webinar': '30-60 minutes',
            'documentary style': '10-15 minutes',
            'live stream': '30-90 minutes'
        }

        return duration_map.get(format_type, '2-5 minutes')

    def _suggest_platforms(self, format_type: str, comm_prefs: List[str]) -> List[str]:
        """Suggest appropriate platforms"""
        platforms = []

        if 'video' in format_type or 'short clip' in format_type:
            platforms.extend(['YouTube', 'TikTok', 'Instagram Reels'])
        elif 'live stream' in format_type:
            platforms.extend(['YouTube Live', 'Facebook Live', 'LinkedIn Live'])
        elif 'educational' in format_type:
            platforms.extend(['YouTube', 'LinkedIn', 'Website'])

        if 'social media' in str(comm_prefs).lower():
            platforms.extend(['Instagram', 'Facebook', 'Twitter'])

        return list(set(platforms)) if platforms else ['YouTube', 'Website']

    def improve_ideas(self, selected_ideas: List[Dict], feedback: Dict) -> List[Dict]:
        """Improve ideas based on user feedback"""
        improved_ideas = []

        for idea in selected_ideas:
            improved_idea = idea.copy()

            # Apply feedback improvements
            if feedback.get('tone_change'):
                improved_idea['description'] = improved_idea['description'].replace(
                    idea.get('tone', 'professional'), feedback['tone_change']
                )

            if feedback.get('format_change'):
                improved_idea['format'] = feedback['format_change']
                improved_idea['key_elements'] = self._generate_key_elements(
                    feedback['format_change'], idea.get('target_platforms', [])
                )

            if feedback.get('additional_elements'):
                improved_idea['key_elements'].extend(feedback['additional_elements'])

            improved_ideas.append(improved_idea)

        return improved_ideas