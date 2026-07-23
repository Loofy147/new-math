import math
from typing import Dict, Any, List

class WorkingMemory:
    """
    Manages active session context, query history, and temporary activation values.
    """
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.context: List[Dict[str, Any]] = []

    def push(self, item: Dict[str, Any]):
        if len(self.context) >= self.capacity:
            self.context.pop(0)
        self.context.append(item)

    def get_latest(self) -> Dict[str, Any]:
        return self.context[-1] if self.context else {}

    def clear(self):
        self.context.clear()


class CognitivePartition:
    """
    Layer 1: Cognitive Partition (القسم المعرفي)
    Manages the Working Memory and computes the Cognitive Complexity index (kappa_i).
    Routes queries to local layer-0/1 quick responder or elevates them to Layer 2+.
    """
    def __init__(self, threshold: float = 1.5):
        self.working_memory = WorkingMemory()
        self.threshold = threshold

    def calculate_complexity(self, query_info: Dict[str, Any]) -> float:
        """
        Computes the Cognitive Complexity Index kappa_i.
        Equation: kappa_i = f(Query Length, Semantic Ambiguity, Syntactic Complexity)
        We model this as:
        kappa_i = w1 * log(length + 1) + w2 * has_existential_tone + w3 * has_question_word
        """
        length = query_info.get("length", 0)
        has_existential_tone = query_info.get("has_existential_tone", False)
        has_question_word = query_info.get("has_question_word", False)

        w1 = 0.5
        w2 = 1.5
        w3 = 0.8

        complexity = (w1 * math.log(length + 1)) + (w2 if has_existential_tone else 0.0) + (w3 if has_question_word else 0.0)
        return complexity

    def route_query(self, query_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluates the query and determines path (local/direct response or elevate to higher layers).
        """
        complexity = self.calculate_complexity(query_info)
        should_elevate = complexity >= self.threshold

        result = {
            "query_info": query_info,
            "complexity": complexity,
            "should_elevate": should_elevate,
            "route": "Layer 2 (Deep Reasoning)" if should_elevate else "Local (Layer 0/1 Quick Response)"
        }
        self.working_memory.push(result)
        return result
