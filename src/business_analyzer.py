"""
Business Analyzer Module
Performs topological analysis of business information.
"""

import re
from collections import defaultdict

class BusinessAnalyzer:
    """Analyzes business information using topological methods"""

    def __init__(self):
        self.business_elements = {
            'products_services': [],
            'target_market': [],
            'competitors': [],
            'value_proposition': [],
            'goals': [],
            'challenges': [],
            'opportunities': []
        }

    def has_sufficient_info(self, processed_data, additional_info):
        """Check if we have sufficient information for analysis"""
        key_indicators = [
            'business' in processed_data['full_text'].lower(),
            len(processed_data['key_ideas']) > 5,
            len(processed_data['entities']) > 3,
            len(additional_info) > 0
        ]

        return sum(key_indicators) >= 3  # At least 3 indicators present

    def analyze_business(self, processed_data, additional_info):
        """Perform topological business analysis"""
        analysis = {
            'structure': self._analyze_structure(processed_data),
            'relationships': self._analyze_relationships(processed_data),
            'market_position': self._analyze_market_position(processed_data, additional_info),
            'value_network': self._build_value_network(processed_data),
            'growth_opportunities': self._identify_growth_opportunities(processed_data, additional_info)
        }

        return analysis

    def _analyze_structure(self, data):
        """Analyze business structure"""
        text = data['full_text'].lower()

        structure = {
            'business_type': self._extract_business_type(text),
            'industry': self._extract_industry(text),
            'size': self._estimate_business_size(text),
            'key_components': data['topics'][:10]
        }

        return structure

    def _analyze_relationships(self, data):
        """Analyze business relationships and connections"""
        entities = data['entities']
        relationships = defaultdict(list)

        # Simple relationship extraction based on co-occurrence
        for i, entity1 in enumerate(entities):
            for entity2 in entities[i+1:]:
                if self._are_related(entity1, entity2, data['full_text']):
                    relationships[entity1].append(entity2)
                    relationships[entity2].append(entity1)

        return dict(relationships)

    def _analyze_market_position(self, data, additional_info):
        """Analyze market position"""
        position = {
            'competitive_advantages': self._extract_competitive_advantages(data),
            'market_gaps': self._identify_market_gaps(data, additional_info),
            'unique_selling_points': data['key_ideas'][:5]
        }

        return position

    def _build_value_network(self, data):
        """Build value network topology"""
        network = {
            'suppliers': [],
            'customers': [],
            'partners': [],
            'competitors': [],
            'stakeholders': data['entities']
        }

        return network

    def _identify_growth_opportunities(self, data, additional_info):
        """Identify growth opportunities"""
        opportunities = []

        # Extract opportunity indicators from text
        opportunity_keywords = ['growth', 'expansion', 'opportunity', 'potential', 'market']
        text = data['full_text'].lower()

        for keyword in opportunity_keywords:
            if keyword in text:
                opportunities.append(f"Potential {keyword} area identified")

        return opportunities

    def _extract_business_type(self, text):
        """Extract business type from text"""
        types = ['retail', 'service', 'manufacturing', 'technology', 'consulting', 'e-commerce']
        for business_type in types:
            if business_type in text:
                return business_type
        return 'unknown'

    def _extract_industry(self, text):
        """Extract industry from text"""
        industries = ['healthcare', 'finance', 'education', 'entertainment', 'food', 'automotive']
        for industry in industries:
            if industry in text:
                return industry
        return 'general'

    def _estimate_business_size(self, text):
        """Estimate business size"""
        size_indicators = {
            'small': ['small business', 'startup', 'local'],
            'medium': ['growing', 'established', 'regional'],
            'large': ['enterprise', 'international', 'corporation']
        }

        for size, indicators in size_indicators.items():
            if any(indicator in text for indicator in indicators):
                return size

        return 'unknown'

    def _extract_competitive_advantages(self, data):
        """Extract competitive advantages"""
        advantages = []
        advantage_keywords = ['unique', 'better', 'faster', 'cheaper', 'quality', 'innovation']

        for idea in data['key_ideas']:
            if any(keyword in idea.lower() for keyword in advantage_keywords):
                advantages.append(idea)

        return advantages

    def _identify_market_gaps(self, data, additional_info):
        """Identify market gaps"""
        gaps = []

        # Look for problem statements in additional info
        for info in additional_info:
            if 'problem' in info['snippet'].lower() or 'gap' in info['snippet'].lower():
                gaps.append(info['snippet'][:100] + '...')

        return gaps

    def _are_related(self, entity1, entity2, text):
        """Check if two entities are related in the text"""
        # Simple proximity check
        text_lower = text.lower()
        pos1 = text_lower.find(entity1.lower())
        pos2 = text_lower.find(entity2.lower())

        if pos1 != -1 and pos2 != -1:
            return abs(pos1 - pos2) < 500  # Within 500 characters

        return False