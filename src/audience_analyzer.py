"""
Audience Analyzer Module
Analyzes target audience characteristics including tone, language, and cultural elements.
"""

class AudienceAnalyzer:
    """Analyzes target audience characteristics"""

    def __init__(self):
        self.tone_profiles = {
            'professional': ['formal', 'corporate', 'business-like', 'serious'],
            'casual': ['friendly', 'relaxed', 'conversational', 'approachable'],
            'youthful': ['energetic', 'trendy', 'fun', 'modern'],
            'expert': ['authoritative', 'technical', 'detailed', 'informative'],
            'inspirational': ['motivational', 'uplifting', 'positive', 'encouraging']
        }

        self.language_styles = {
            'simple': ['clear', 'straightforward', 'easy to understand'],
            'technical': ['industry-specific', 'jargon', 'detailed'],
            'storytelling': ['narrative', 'engaging', 'emotional'],
            'persuasive': ['convincing', 'benefit-focused', 'action-oriented']
        }

        self.cultural_elements = {
            'western': ['individualism', 'achievement', 'innovation'],
            'eastern': ['harmony', 'tradition', 'community'],
            'latin': ['family', 'passion', 'social connections'],
            'youth': ['technology', 'social media', 'trends'],
            'professional': ['expertise', 'credibility', 'results']
        }

    def analyze_audience(self, business_analysis):
        """Analyze target audience based on business analysis"""
        audience_profile = {
            'demographics': self._extract_demographics(business_analysis),
            'tone': self._determine_tone(business_analysis),
            'language': self._determine_language(business_analysis),
            'cultural_elements': self._identify_cultural_elements(business_analysis),
            'communication_preferences': self._identify_communication_prefs(business_analysis)
        }

        return audience_profile

    def _extract_demographics(self, analysis):
        """Extract audience demographics"""
        demographics = {
            'age_group': 'unknown',
            'income_level': 'unknown',
            'education_level': 'unknown',
            'location': 'unknown'
        }

        # Analyze structure and market position for demographic clues
        structure = analysis.get('structure', {})
        market_pos = analysis.get('market_position', {})

        # Simple demographic inference
        if 'youth' in str(structure).lower() or 'young' in str(market_pos).lower():
            demographics['age_group'] = '18-35'
        elif 'professional' in str(structure).lower():
            demographics['age_group'] = '25-55'

        if 'premium' in str(market_pos).lower():
            demographics['income_level'] = 'high'
        elif 'budget' in str(market_pos).lower():
            demographics['income_level'] = 'medium'

        return demographics

    def _determine_tone(self, analysis):
        """Determine appropriate tone for content"""
        text_content = str(analysis).lower()

        tone_scores = {}
        for tone, keywords in self.tone_profiles.items():
            score = sum(1 for keyword in keywords if keyword in text_content)
            tone_scores[tone] = score

        # Return tone with highest score, default to professional
        best_tone = max(tone_scores, key=tone_scores.get)
        return best_tone if tone_scores[best_tone] > 0 else 'professional'

    def _determine_language(self, analysis):
        """Determine language style"""
        text_content = str(analysis).lower()

        language_scores = {}
        for style, keywords in self.language_styles.items():
            score = sum(1 for keyword in keywords if keyword in text_content)
            language_scores[style] = score

        # Return style with highest score, default to simple
        best_style = max(language_scores, key=language_scores.get)
        return best_style if language_scores[best_style] > 0 else 'simple'

    def _identify_cultural_elements(self, analysis):
        """Identify relevant cultural elements"""
        text_content = str(analysis).lower()

        cultural_scores = {}
        for culture, elements in self.cultural_elements.items():
            score = sum(1 for element in elements if element in text_content)
            cultural_scores[culture] = score

        # Return top 2 cultural elements
        sorted_cultures = sorted(cultural_scores.items(), key=lambda x: x[1], reverse=True)
        return [culture for culture, score in sorted_cultures[:2] if score > 0]

    def _identify_communication_prefs(self, analysis):
        """Identify communication preferences"""
        preferences = []

        text_content = str(analysis).lower()

        if 'social media' in text_content or 'instagram' in text_content:
            preferences.append('visual content')
        if 'video' in text_content:
            preferences.append('video content')
        if 'blog' in text_content or 'article' in text_content:
            preferences.append('written content')
        if 'presentation' in text_content:
            preferences.append('live presentations')

        # Default preferences if none identified
        if not preferences:
            preferences = ['visual content', 'video content']

        return preferences