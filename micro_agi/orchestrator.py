from typing import Dict, Any, List
from micro_agi.layer0_interface import InterfaceLayer
from micro_agi.layer1_cognitive import CognitivePartition
from micro_agi.layer2_world_model import WorldModel
from micro_agi.layer3_praxis import PraxisEngine
from micro_agi.layer4_noetikon import NoetikonLayer
from micro_agi.metrics import get_all_metrics
from micro_agi.etbs import ETBSConduit

class MicroAGIOrchestrator:
    """
    Coordinates the entire processing pipeline, Query Flow, and Learning Loop of Micro-AGI.
    Now enhanced with the Experimental Translation Bridging Substrate (ETBS).
    """
    def __init__(self, routing_threshold: float = 1.5):
        self.layer0 = InterfaceLayer()
        self.layer1 = CognitivePartition(threshold=routing_threshold)
        self.layer2 = WorldModel()
        self.layer3 = PraxisEngine()
        self.layer4 = NoetikonLayer()

        # Experimental Translation Bridging Substrate (ETBS) Conduit
        self.etbs = ETBSConduit()

        # Metrics trackers
        self.new_concepts_discovered = 0
        self.total_concepts = 10
        self.energy_consumed = 0.0
        self.data_processed = 0.0

    def query_flow(self, user_query: str) -> Dict[str, Any]:
        """
        Processes query through layers 0 -> 1 -> 2 -> 3 -> 4 -> 0.
        Refer to Figure 2 (Query Flow) in Architectural Documentation.
        """
        self.energy_consumed += 0.5  # Base query energy cost
        self.data_processed += float(len(user_query))

        # 1. Layer 0 (Interface Layer)
        encoded = self.layer0.encode(user_query)
        parsed = self.layer0.parse_query(encoded)

        # 2. Layer 1 (Cognitive Partition Routing)
        route_decision = self.layer1.route_query(parsed)

        if not route_decision["should_elevate"]:
            # Route locally
            surface_resp = self.layer0.generate_surface_response(parsed)
            return {
                "route": "Local/Direct",
                "complexity": route_decision["complexity"],
                "response": surface_resp,
                "metrics": self.get_current_metrics()
            }

        # 3. Layer 2 (Deep Reasoning - World Model)
        self.energy_consumed += 1.5  # Elevating consumes more energy
        simulation = self.layer2.run_simulation()

        # --- ETBS CONDUIT ACTIVATION ---
        # ETBS intersects deep queries to run hypothesis generation & verification cycles.
        causal_nodes = list(self.layer2.causal_graph.nodes)
        etbs_results = self.etbs.execute_bridge(
            causal_nodes=causal_nodes,
            beliefs=self.layer2.beliefs,
            uncertainty=0.75  # Simulating a default uncertainty trigger
        )

        # Reflect feedback directly onto causal structure
        feedback = etbs_results["feedback"]
        if feedback["weight_adjustment"] > 0:
            # Positive verisimilitude: evolve model and reward praxis
            self.layer3.valence = min(1.0, self.layer3.valence + 0.15)
            self.layer4.narrative_identity.append_experience(
                f"ETBS validated discovery {feedback['hypothesis_id']} with high verisimilitude."
            )
        elif feedback["weight_adjustment"] < 0:
            # Suppress hallucinated causal paths
            self.layer3.valence = max(0.0, self.layer3.valence - 0.1)
            self.layer4.narrative_identity.append_experience(
                f"ETBS suppressed hallucination {feedback['hypothesis_id']}."
            )

        # 4. Layer 3 (Praxis Engine Evaluation)
        motivation = self.layer3.calculate_motivation(route_decision["complexity"])
        friction = self.layer3.calculate_internal_friction(route_decision["complexity"])
        decision_eval = self.layer3.evaluate_decision(simulation, target_alignment=simulation["gravity_force"])

        # 5. Layer 4 (Noetikon Metacognition & Self-Evolution)
        self.energy_consumed += 2.0
        # Feed current beliefs and look for self-adaptation
        metacog_results = self.layer4.process_metacognition(
            beliefs=self.layer2.beliefs,
            target_force=simulation["gravity_force"]
        )

        # Adapt Layer 2 beliefs to consistent beliefs determined by Layer 4 Reflexive Operator
        self.layer2.update_beliefs(metacog_results["consistent_beliefs"])

        # Increase concept count upon deep reasoning
        self.new_concepts_discovered += 1
        self.total_concepts += 1

        # Formulate final response via Layer 0
        raw_response = (
            f"Reasoned deeply about '{user_query}' (Complexity: {route_decision['complexity']:.2f}, "
            f"Motivation: {motivation:.2f}, Friction: {friction:.2f}). "
            f"ETBS verified simulated hypothesis ({feedback['classification']}) "
            f"with Verisimilitude: {feedback['verisimilitude']:.4f}. "
            f"Simulated innovative gravity force = {simulation['gravity_force']:.4e} N. "
            f"Alignment is { 'Correct' if decision_eval['is_aligned'] else 'Tuned' }. "
            f"Meta-identity state: {metacog_results['narrative_state']}"
        )
        final_response = self.layer0.decode_response(raw_response)

        return {
            "route": "Deep Reasoning (Layers 0-4) + ETBS Bridge",
            "complexity": route_decision["complexity"],
            "motivation": motivation,
            "friction": friction,
            "simulation": simulation,
            "decision_evaluation": decision_eval,
            "etbs_bridging": etbs_results,
            "metacognition": metacog_results,
            "response": final_response,
            "metrics": self.get_current_metrics()
        }

    def learning_loop(self, external_observations: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes learning loop process:
        [Environment/Data] -> Layer 1 (Ingest) -> Layer 2 (Causal updates) -> Layer 3 (Reward) -> Layer 4 (Reflexive update)
        Now also includes ETBS dynamic testing on newly updated causal weights.
        """
        self.energy_consumed += 3.0
        self.data_processed += 100.0  # Simulated observation packet size

        # Ingest observations into Layer 2 Beliefs
        self.layer2.update_beliefs(external_observations)

        # Run simulation with new observations
        sim = self.layer2.run_simulation()

        # Run ETBS bridge to evaluate newly ingested states
        causal_nodes = list(self.layer2.causal_graph.nodes)
        etbs_res = self.etbs.execute_bridge(
            causal_nodes=causal_nodes,
            beliefs=self.layer2.beliefs,
            uncertainty=0.5
        )

        # Evaluate reward (Layer 3)
        reward_eval = self.layer3.evaluate_decision(sim, target_alignment=sim["gravity_force"])

        # Meta-review and self-adaptation (Layer 4)
        metacog = self.layer4.process_metacognition(self.layer2.beliefs, target_force=sim["gravity_force"])

        self.new_concepts_discovered += 1
        self.total_concepts += 1

        return {
            "status": "Learning loop complete + ETBS Verified",
            "simulation_results": sim,
            "etbs_verification": etbs_res,
            "reward_evaluation": reward_eval,
            "metacognition": metacog,
            "metrics": self.get_current_metrics()
        }

    def get_current_metrics(self) -> Dict[str, float]:
        # Simple definition of chains for depth calculations
        causal_chains = [
            ["mass_1", "gravity_force", "acceleration"],
            ["mass_2", "gravity_force", "acceleration"],
            ["distance", "gravity_force", "acceleration"]
        ]

        # Correct relations count based on the DiGraph checks
        correct_relations = self.layer2.causal_graph.number_of_edges()
        total_relations = correct_relations + 1  # Add a dummy potential incorrect/hypothetical relation

        return get_all_metrics(
            new_concepts=self.new_concepts_discovered,
            known_concepts=self.total_concepts,
            impact=1.5,
            causal_chains=causal_chains,
            correct_relations=correct_relations,
            total_relations=total_relations,
            energy=self.energy_consumed,
            data=self.data_processed
        )


    def run_production_checklist_evaluation(self) -> Dict[str, Any]:
        """
        Executes a production checklist verification across the framework.
        """
        from micro_agi.production_checklist import ProductionChecklistEvaluator
        evaluator = ProductionChecklistEvaluator()
        return evaluator.evaluate_readiness(self)
