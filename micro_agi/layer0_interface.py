import re
from typing import Dict, Any

class InterfaceLayer:
    """
    Layer 0: Interface Layer (طبقة الواجهة)
    Handles linguistic interaction, encoding/decoding of queries, syntactic/semantic analysis,
    and generating surface responses.
    """
    def __init__(self):
        # Simulation of a lightweight language model encoder/decoder mapping/behavior
        pass

    def encode(self, query: str) -> str:
        """
        Encodes/normalizes the incoming user query.
        """
        # Strip white space and lowercase
        normalized = query.strip()
        return normalized

    def parse_query(self, query: str) -> Dict[str, Any]:
        """
        Performs syntactic and semantic analysis on the query.
        """
        words = re.findall(r'\w+', query.lower())
        length = len(words)

        # Simple semantic classification (e.g., detecting question types or existential tones)
        has_question_word = any(w in ["why", "how", "what", "who", "where", "كيف", "لماذا", "ما", "من", "أين"] for w in words)
        has_existential_tone = any(w in ["existential", "purpose", "existence", "causal", "cause", "gravity", "وجود", "سبب", "غاية", "جاذبية"] for w in words)

        return {
            "query": query,
            "words": words,
            "length": length,
            "has_question_word": has_question_word,
            "has_existential_tone": has_existential_tone,
        }

    def decode_response(self, content: str) -> str:
        """
        Decodes raw system responses into user-friendly format.
        """
        return f"[Micro-AGI Interface Response]: {content}"

    def generate_surface_response(self, query_info: Dict[str, Any]) -> str:
        """
        Quick surface response for simple queries.
        """
        return self.decode_response(f"I processed your query '{query_info['query']}' directly in Layer 0/1. No deep reasoning required.")
