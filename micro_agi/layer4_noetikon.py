import random
from typing import Dict, Any, List, Tuple
from deap import base, creator, tools, algorithms

# Setup DEAP genetic algorithm framework for evolving models
# We create a simple setup to optimize hyperparameters/equations
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

class SelfEvolutionEngine:
    """
    Subsystem of Noetikon Layer that runs a Genetic Algorithm to evolve the Causal Model variables/weights.
    """
    def __init__(self, individual_size: int = 3):
        self.individual_size = individual_size
        self.toolbox = base.Toolbox()

        # Attribute generator: float values between 0.0 and 1.0 representing system/equation tuning parameters
        self.toolbox.register("attr_float", random.uniform, 0.0, 1.0)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_float, n=self.individual_size)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        # Register operators
        self.toolbox.register("mate", tools.cxBlend, alpha=0.5)
        self.toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    def evaluate_individual(self, individual: List[float], target_force: float) -> Tuple[float]:
        """
        Evaluation function representing a simulated causal fitness test.
        Fitness = alpha * Causal Accuracy + beta * Creativity + gamma * Coherence.
        Here we score how close the parameters get to a target value.
        """
        simulated_value = individual[0] * 10.0 + individual[1] * 5.0 - individual[2] * 2.0
        error = abs(simulated_value - target_force)
        # We want to minimize error, i.e., maximize fitness
        fitness = 100.0 / (1.0 + error)
        return (fitness,)

    def evolve(self, target_force: float, generations: int = 5, pop_size: int = 10) -> List[float]:
        """
        Runs the genetic algorithm loop.
        """
        # We must make sure evaluate is registered to the specific target_force instance
        self.toolbox.register("evaluate", self.evaluate_individual, target_force=target_force)

        pop = self.toolbox.population(n=pop_size)

        # Simple genetic algorithm
        algorithms.eaSimple(pop, self.toolbox, cxpb=0.5, mutpb=0.2, ngen=generations, verbose=False)

        best_ind = tools.selBest(pop, 1)[0]
        return list(best_ind)


class CoherenceSupervisor:
    """
    Monitors global consistency and resolves conflicts in the belief/knowledge graph.
    """
    def __init__(self):
        pass

    def check_coherence(self, beliefs: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Checks for semantic/physical conflicts.
        e.g., negative mass, infinite distance, or conflict in variables.
        """
        conflicts = []
        if beliefs.get("mass_1", 1.0) < 0:
            conflicts.append("Conflict: Negative mass for mass_1 detected.")
        if beliefs.get("mass_2", 1.0) < 0:
            conflicts.append("Conflict: Negative mass for mass_2 detected.")
        if beliefs.get("distance", 1.0) <= 0:
            conflicts.append("Conflict: Zero or negative distance detected.")

        is_coherent = len(conflicts) == 0
        return is_coherent, conflicts


class ReflexiveOperator:
    """
    Reflexive Operator R: Belief Space -> Consistent Belief Space
    Detects contradictions and resolves them (e.g. mapping invalid beliefs back to valid state space).
    """
    def __init__(self):
        pass

    def resolve_conflicts(self, beliefs: Dict[str, Any], conflicts: List[str]) -> Dict[str, Any]:
        """
        Enforces constraints on invalid parameters.
        """
        resolved_beliefs = beliefs.copy()
        for conflict in conflicts:
            if "mass_1" in conflict:
                resolved_beliefs["mass_1"] = abs(beliefs["mass_1"]) if beliefs["mass_1"] != 0 else 1.0
            if "mass_2" in conflict:
                resolved_beliefs["mass_2"] = abs(beliefs["mass_2"]) if beliefs["mass_2"] != 0 else 1.0
            if "distance" in conflict:
                resolved_beliefs["distance"] = 1.0 if beliefs["distance"] <= 0 else beliefs["distance"]
        return resolved_beliefs


class NarrativeIdentitySystem:
    """
    Maintains AGI state/identity continuity over time.
    """
    def __init__(self):
        self.history: List[str] = ["Initial state: Born into virtual embodiment."]

    def append_experience(self, experience: str):
        self.history.append(experience)

    def generate_narrative_summary(self) -> str:
        return " -> ".join(self.history[-5:])


class NoetikonLayer:
    """
    Layer 4: Noetikon Layer (طبقة النويتيكون)
    Provides metacognitive self-evolution, coherence monitoring, conflict resolution,
    and narrative identity tracking.
    """
    def __init__(self):
        self.evolution_engine = SelfEvolutionEngine()
        self.coherence_supervisor = CoherenceSupervisor()
        self.reflexive_operator = ReflexiveOperator()
        self.narrative_identity = NarrativeIdentitySystem()

    def process_metacognition(self, beliefs: Dict[str, Any], target_force: float) -> Dict[str, Any]:
        # 1. Check Coherence
        is_coherent, conflicts = self.coherence_supervisor.check_coherence(beliefs)

        # 2. Resolve Conflicts via Reflexive Operator
        consistent_beliefs = beliefs
        if not is_coherent:
            consistent_beliefs = self.reflexive_operator.resolve_conflicts(beliefs, conflicts)
            self.narrative_identity.append_experience(f"Resolved conflicts: {', '.join(conflicts)}")

        # 3. Perform evolution loop to adapt / self-evolve hyperparameters
        best_hyperparameters = self.evolution_engine.evolve(target_force=target_force, generations=3, pop_size=8)
        self.narrative_identity.append_experience(f"Evolved new causal hyperparameters: {best_hyperparameters}")

        return {
            "is_coherent_before": is_coherent,
            "conflicts_detected": conflicts,
            "consistent_beliefs": consistent_beliefs,
            "best_hyperparameters": best_hyperparameters,
            "narrative_state": self.narrative_identity.generate_narrative_summary()
        }
