"""
Text Processing Module
Uses NLP to extract context, key ideas, and insights from documents.
"""

import spacy
from collections import Counter
import re

class TextProcessor:
    """Processes text documents using NLP techniques"""

    def __init__(self, config):
        self.config = config
        try:
            self.nlp = spacy.load(config['model'])
        except OSError:
            # Download model if not available
            import subprocess
            subprocess.run(['python', '-m', 'spacy', 'download', config['model']])
            self.nlp = spacy.load(config['model'])

    def process_documents(self, documents):
        """Process multiple documents and extract key information"""
        all_text = ""
        key_ideas = []
        entities = []
        topics = []

        for doc in documents:
            processed = self._process_single_document(doc['content'])
            all_text += processed['text'] + "\n"
            key_ideas.extend(processed['key_phrases'])
            entities.extend(processed['entities'])
            topics.extend(processed['topics'])

        return {
            'full_text': all_text,
            'key_ideas': list(set(key_ideas)),  # Remove duplicates
            'entities': list(set(entities)),
            'topics': self._consolidate_topics(topics),
            'document_count': len(documents)
        }

    def _process_single_document(self, text):
        """Process a single document"""
        # Clean text
        text = self._clean_text(text)

        # Process with spaCy
        doc = self.nlp(text)

        # Extract key phrases (noun chunks)
        key_phrases = [chunk.text.lower() for chunk in doc.noun_chunks
                      if len(chunk.text.split()) > 1]

        # Extract entities
        entities = [ent.text for ent in doc.ents]

        # Extract topics (common nouns and proper nouns)
        topics = [token.lemma_.lower() for token in doc
                 if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop]

        return {
            'text': text,
            'key_phrases': key_phrases[:20],  # Top 20 key phrases
            'entities': entities,
            'topics': topics
        }

    def _clean_text(self, text):
        """Clean and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        return text.strip()

    def _consolidate_topics(self, all_topics):
        """Consolidate and rank topics by frequency"""
        topic_counts = Counter(all_topics)
        return topic_counts.most_common(50)  # Top 50 topics