import math
from typing import Dict, Any, List

def calculate_creativity_index(new_concepts: int, known_concepts: int, impact: float = 1.0) -> float:
    """
    CI = (New Concepts / Known Concepts) * log(Impact)
    Avoid division by zero or log of non-positive values.
    """
    if known_concepts <= 0:
        known_concepts = 1
    safe_impact = max(1.001, impact)
    return (new_concepts / known_concepts) * math.log(safe_impact)


def calculate_causal_depth(causal_chains: List[List[str]]) -> float:
    """
    CD = sum_{i=1}^n (1 / len(causal_chain_i))
    Determines the cognitive causal length complexity.
    """
    depth = 0.0
    for chain in causal_chains:
        if len(chain) > 0:
            depth += 1.0 / len(chain)
    return depth


def calculate_causal_quotient(correct_relations: int, total_relations: int) -> float:
    """
    CQ = Correct Relations / Total Relations
    """
    if total_relations <= 0:
        return 0.0
    return correct_relations / total_relations


def calculate_efficiency(causal_depth: float, creativity: float, energy: float, data: float) -> float:
    """
    Efficiency = (CausalDepth * Creativity) / (Energy * Data)
    """
    energy = max(0.001, energy)
    data = max(0.001, data)
    return (causal_depth * creativity) / (energy * data)


def get_all_metrics(
    new_concepts: int,
    known_concepts: int,
    impact: float,
    causal_chains: List[List[str]],
    correct_relations: int,
    total_relations: int,
    energy: float,
    data: float
) -> Dict[str, float]:
    ci = calculate_creativity_index(new_concepts, known_concepts, impact)
    cd = calculate_causal_depth(causal_chains)
    cq = calculate_causal_quotient(correct_relations, total_relations)
    eff = calculate_efficiency(cd, ci, energy, data)

    return {
        "creativity_index": ci,
        "causal_depth": cd,
        "causal_quotient": cq,
        "efficiency": eff
    }
