import unittest
from micro_agi.layer0_interface import InterfaceLayer
from micro_agi.layer1_cognitive import CognitivePartition
from micro_agi.layer2_world_model import WorldModel
from micro_agi.layer3_praxis import PraxisEngine
from micro_agi.layer4_noetikon import NoetikonLayer
from micro_agi.orchestrator import MicroAGIOrchestrator

class TestMicroAGIFramework(unittest.TestCase):

    def test_layer0_parsing_and_encoding(self):
        layer0 = InterfaceLayer()
        query = "  Why does GRAVITY decay?  "
        encoded = layer0.encode(query)
        self.assertEqual(encoded, "Why does GRAVITY decay?")

        parsed = layer0.parse_query(encoded)
        self.assertTrue(parsed["has_question_word"])
        self.assertTrue(parsed["has_existential_tone"])
        self.assertEqual(parsed["length"], 4)

    def test_layer1_cognitive_complexity_routing(self):
        cp = CognitivePartition(threshold=1.5)

        simple_query = {"length": 1, "has_question_word": False, "has_existential_tone": False}
        route_simple = cp.route_query(simple_query)
        self.assertFalse(route_simple["should_elevate"])

        complex_query = {"length": 10, "has_question_word": True, "has_existential_tone": True}
        route_complex = cp.route_query(complex_query)
        self.assertTrue(route_complex["should_elevate"])

    def test_layer2_sympy_and_causal_graph(self):
        wm = WorldModel()
        causes_of_force = wm.get_causes("gravity_force")
        self.assertIn("mass_1", causes_of_force)
        self.assertIn("distance", causes_of_force)

        # Test Gravity model: F = (G * m1 * m2 / r^2) * e^(-lambda * r)
        # For m1=1e11, m2=1, r=1, lambda=0, G=6.6743e-11 -> F should be approx 6.6743
        force = wm.evaluate_gravity_model(1e11, 1.0, 1.0, 0.0, G=6.6743e-11)
        self.assertAlmostEqual(force, 6.6743, places=4)

    def test_layer3_praxis_motivation_and_friction(self):
        pe = PraxisEngine()
        mot = pe.calculate_motivation(complexity=2.0)
        friction = pe.calculate_internal_friction(decision_complexity=2.0)

        # Motivation should be a valid bounded float
        self.assertTrue(0.0 <= mot <= 1.0)
        self.assertTrue(friction >= 0.0)

    def test_layer4_noetikon_metacognition(self):
        nl = NoetikonLayer()
        beliefs = {"mass_1": -50, "mass_2": 20, "distance": 0.0}
        results = nl.process_metacognition(beliefs, target_force=10.0)

        self.assertFalse(results["is_coherent_before"])
        self.assertTrue(len(results["conflicts_detected"]) > 0)
        # Check reflexive correction
        self.assertEqual(results["consistent_beliefs"]["mass_1"], 50)
        self.assertEqual(results["consistent_beliefs"]["distance"], 1.0)
        self.assertEqual(len(results["best_hyperparameters"]), 3)

    def test_orchestrator_pipeline(self):
        orch = MicroAGIOrchestrator()

        # Simple Query Flow
        simple_res = orch.query_flow("Hello")
        self.assertEqual(simple_res["route"], "Local/Direct")
        self.assertIn("directly", simple_res["response"])

        # Complex Query Flow
        complex_res = orch.query_flow("Why does gravity decay existentially?")
        self.assertEqual(complex_res["route"], "Deep Reasoning (Layers 0-4)")
        self.assertIn("Reasoned deeply", complex_res["response"])

        # Learning Loop Integration
        learning_res = orch.learning_loop({"mass_1": 1e12, "distance": 2.0})
        self.assertEqual(learning_res["status"], "Learning loop complete")
        self.assertTrue(learning_res["simulation_results"]["gravity_force"] > 0)

if __name__ == "__main__":
    unittest.main()
