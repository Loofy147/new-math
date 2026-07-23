import networkx as nx
import sympy as sp
from typing import Dict, Any, List, Tuple

class WorldModel:
    """
    Layer 2: World Model / Reasoning Substrate (نموذج العالم / الاستدلال)
    Maintains a Causal Graph using NetworkX, parses and executes symbolic equations using SymPy,
    and updates beliefs of the reality/simulation.
    """
    def __init__(self):
        # Initialize causal graph
        self.causal_graph = nx.DiGraph()
        self._setup_default_causal_graph()

        # Persistent Beliefs: variables representing current world status
        self.beliefs: Dict[str, Any] = {
            "gravity_constant": 6.6743e-11,
            "lambda_decay": 0.05,  # Innovative gravity decay constant lambda
            "mass_1": 5.972e24,    # e.g., Earth Mass
            "mass_2": 70.0,        # e.g., Human Mass
            "distance": 6371000.0  # e.g., Earth Radius
        }

    def _setup_default_causal_graph(self):
        """
        Populate default causes and effects.
        e.g., Mass -> Gravity -> Force -> Acceleration -> Velocity
        """
        self.causal_graph.add_edge("mass_1", "gravity_force", weight=1.0)
        self.causal_graph.add_edge("mass_2", "gravity_force", weight=1.0)
        self.causal_graph.add_edge("distance", "gravity_force", weight=-2.0)
        self.causal_graph.add_edge("lambda_decay", "gravity_force", weight=-1.0)
        self.causal_graph.add_edge("gravity_force", "acceleration", weight=1.0)

    def get_causes(self, target_node: str) -> List[str]:
        """
        Returns list of parent causes for a given target node.
        """
        if target_node in self.causal_graph:
            return list(self.causal_graph.predecessors(target_node))
        return []

    def evaluate_gravity_model(self, m1: float, m2: float, r: float, lamb: float, G: float = 6.6743e-11) -> float:
        """
        Evaluates the innovative gravity model:
        F = (G * m1 * m2 / r^2) * e^(-lambda * r)
        Using SymPy for symbolic computation and evaluation.
        """
        G_sym, m1_sym, m2_sym, r_sym, lambda_sym = sp.symbols('G m1 m2 r lambda')

        # Innovative gravity formula
        formula = (G_sym * m1_sym * m2_sym / (r_sym ** 2)) * sp.exp(-lambda_sym * r_sym)

        # Substitute values
        evaluation = formula.subs({
            G_sym: G,
            m1_sym: m1,
            m2_sym: m2,
            r_sym: r,
            lambda_sym: lamb
        })

        return float(evaluation.evalf())

    def update_beliefs(self, updates: Dict[str, Any]):
        """
        Updates persistent beliefs from external environment observations.
        """
        for k, v in updates.items():
            self.beliefs[k] = v

    def run_simulation(self, steps: int = 1) -> Dict[str, Any]:
        """
        Simulates hypothetical outcomes. Calculates innovative gravity force based on beliefs.
        """
        m1 = self.beliefs["mass_1"]
        m2 = self.beliefs["mass_2"]
        r = self.beliefs["distance"]
        lamb = self.beliefs["lambda_decay"]
        G = self.beliefs["gravity_constant"]

        force = self.evaluate_gravity_model(m1, m2, r, lamb, G)

        # Simple dynamics update
        acceleration = force / m2

        simulation_results = {
            "gravity_force": force,
            "acceleration": acceleration,
            "steps_simulated": steps
        }

        # Save results to belief space as well
        self.beliefs["last_gravity_force"] = force
        self.beliefs["last_acceleration"] = acceleration

        return simulation_results
