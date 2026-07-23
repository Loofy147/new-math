import math
from typing import Dict, Any

class PraxisEngine:
    """
    Layer 3: Praxis Engine (محرك الممارسة)
    Handles emotional and motivational modulation, internal friction modeling,
    and reward / alignment tracking.
    """
    def __init__(self, alpha: float = 0.4, beta: float = 0.3, gamma: float = 0.3):
        # Weighting coefficients for Motivation
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        # State values
        self.valence = 0.5  # Valence network output (emotional weight - positive/negative)
        self.utility = 0.5  # Task usefulness
        self.curiosity = 0.8  # Dynamic exploratory drive

    def calculate_internal_friction(self, decision_complexity: float) -> float:
        """
        Calculates internal cognitive friction based on complexity and state.
        Friction is high when decision is highly complex and valence or curiosity is low.
        """
        base_friction = decision_complexity * 0.5
        mitigator = (self.valence + self.curiosity) / 2.0
        friction = max(0.0, base_friction - (0.2 * mitigator))
        return friction

    def calculate_motivation(self, complexity: float) -> float:
        """
        Calculates motivation score based on the equation:
        Motivation = alpha * Valence + beta * Utility + gamma * Curiosity
        """
        # Dynamically scale curiosity slightly based on complexity (more complex -> higher curiosity/challenge)
        scaled_curiosity = min(1.0, self.curiosity + (complexity * 0.05))

        motivation = (self.alpha * self.valence) + (self.beta * self.utility) + (self.gamma * scaled_curiosity)
        return motivation

    def evaluate_decision(self, outcome: Dict[str, Any], target_alignment: float = 1.0) -> Dict[str, Any]:
        """
        Evaluates the ethical/alignment distance of a simulated outcome.
        D_ethical = ||State - Core Principle||
        We simulate this with a simplified difference evaluation.
        """
        actual_val = outcome.get("gravity_force", 1.0)
        # Let's say alignment is perfect (0 distance) if force matches expected range,
        # otherwise distance is modeled.
        ethical_distance = abs(actual_val - target_alignment) / (1.0 + abs(actual_val))

        # Adjust internal valence based on performance/alignment
        if ethical_distance < 0.2:
            self.valence = min(1.0, self.valence + 0.1)
        else:
            self.valence = max(0.0, self.valence - 0.1)

        return {
            "ethical_distance": ethical_distance,
            "valence_updated": self.valence,
            "is_aligned": ethical_distance < 0.5
        }
