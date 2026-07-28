import unittest
from micro_agi.layer0_interface import InterfaceLayer
from micro_agi.layer1_cognitive import CognitivePartition
from micro_agi.layer2_world_model import WorldModel
from micro_agi.layer3_praxis import PraxisEngine
from micro_agi.layer4_noetikon import NoetikonLayer
from micro_agi.orchestrator import MicroAGIOrchestrator
from micro_agi.etbs import ETBSConduit, ExternalAnchorFusion

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

    def test_etbs_bridging_substrate(self):
        # 1. External Anchors
        fusion = ExternalAnchorFusion()
        self.assertEqual(fusion.fetch_anchor("speed_of_light"), 299792458.0)

        # 2. Conduit workflow
        conduit = ETBSConduit()
        res = conduit.execute_bridge(
            causal_nodes=["distance", "mass_1"],
            beliefs={"mass_1": 1e11, "mass_2": 1.0, "distance": 1.0},
            uncertainty=0.9
        )
        self.assertIn("hypothesis", res)
        self.assertIn("simulation", res)
        self.assertTrue(0.0 <= res["verisimilitude"] <= 1.0)
        self.assertIn("classification", res["feedback"])

    def test_orchestrator_pipeline_with_etbs(self):
        orch = MicroAGIOrchestrator()

        # Simple Query Flow
        simple_res = orch.query_flow("Hello")
        self.assertEqual(simple_res["route"], "Local/Direct")
        self.assertIn("directly", simple_res["response"])

        # Complex Query Flow with ETBS bridge integrated
        complex_res = orch.query_flow("Why does gravity decay existentially?")
        self.assertEqual(complex_res["route"], "Deep Reasoning (Layers 0-4) + ETBS Bridge")
        self.assertIn("Reasoned deeply", complex_res["response"])
        self.assertIn("etbs_bridging", complex_res)

        # Learning Loop Integration
        learning_res = orch.learning_loop({"mass_1": 1e12, "distance": 2.0})
        self.assertIn("ETBS Verified", learning_res["status"])
        self.assertIn("etbs_verification", learning_res)

    def test_production_readiness_checklist(self):
        orch = MicroAGIOrchestrator()
        eval_report = orch.run_production_checklist_evaluation()

        self.assertEqual(eval_report["overall_readiness_score"], 100.0)
        self.assertTrue(eval_report["is_production_ready"])
        self.assertTrue(eval_report["categories"]["architectural_layer_integrity"]["passed"])
        self.assertTrue(eval_report["categories"]["experimental_translation_bridging"]["passed"])
        self.assertTrue(eval_report["categories"]["performance_efficiency"]["passed"])
        self.assertTrue(eval_report["categories"]["ethical_alignment_coherence"]["passed"])

        # Introduce a conflict and check if score falls/handles it
        orch.layer2.update_beliefs({"mass_1": -100.0})
        dirty_report = orch.run_production_checklist_evaluation()
        self.assertFalse(dirty_report["categories"]["ethical_alignment_coherence"]["passed"])
        self.assertLess(dirty_report["overall_readiness_score"], 100.0)


    def test_hybrid_verisimilitude_and_sandbox_mutation(self):
        from micro_agi.etbs import ETBSConduit
        conduit = ETBSConduit()

        sim_results = {
            "mean": 6.6743e-11,
            "variance": 1e-22,
            "iterations": 100
        }
        hyp = {
            "cause": "distance",
            "proposed_equation": "G * m1 * m2 / (r ** 2)",
            "param": "lambda",
            "id": "hyp_test"
        }

        v_hybrid = conduit.vm.calculate_verisimilitude(sim_results, hyp, {})
        self.assertTrue(0.0 <= v_hybrid <= 1.0)

        medium_hyp, medium_v, history = conduit.sandbox.refine_hypothesis(hyp, {}, 0.5)
        self.assertTrue(len(history) >= 1)
        self.assertTrue(medium_v >= 0.0)

    def test_dynamic_threshold_modulation(self):
        from micro_agi.layer3_praxis import PraxisEngine
        pe = PraxisEngine()

        self.assertEqual(pe.get_success_rate(), 0.5)
        initial_threshold = pe.calculate_promotion_threshold()
        self.assertAlmostEqual(initial_threshold, 0.85)

        for _ in range(5):
            pe.register_hypothesis_outcome(True)
        self.assertEqual(pe.get_success_rate(), 1.0)
        high_threshold = pe.calculate_promotion_threshold()
        self.assertGreater(high_threshold, 0.85)

        for _ in range(10):
            pe.register_hypothesis_outcome(False)
        self.assertLess(pe.get_success_rate(), 0.5)
        low_threshold = pe.calculate_promotion_threshold()
        self.assertLess(low_threshold, 0.85)


    def test_crps_score_calculation(self):
        from micro_agi.etbs import crps_score
        import numpy as np
        y_true = np.array([2.0])
        y_pred = np.array([[1.9], [2.1], [2.0]])
        val = crps_score(y_true, y_pred)
        self.assertGreaterEqual(val, 0.0)
        self.assertLess(val, 1.0)

    def test_pit_and_bayesian_coverage(self):
        from micro_agi.etbs import pit_histogram, bayesian_coverage_credible
        import numpy as np
        y_true = np.array([5.0])
        y_pred = np.array([[4.8], [5.2], [5.0], [5.1], [4.9]])
        hist, bins = pit_histogram(y_true, y_pred, n_bins=5)
        self.assertEqual(len(hist), 5)

        low, mean, high = bayesian_coverage_credible(y_true, y_pred)
        self.assertTrue(0.0 <= low <= mean <= high <= 1.0)

    def test_cma_es_evolution(self):
        from micro_agi.etbs import CMA_EvolutionaryEngine
        import numpy as np
        engine = CMA_EvolutionaryEngine([1.0, 1.0], (0.1, 5.0), population_size=10)
        best = engine.evolve(lambda x: -np.sum((x - 2.0)**2), n_generations=2)
        self.assertEqual(len(best), 2)

    def test_bald_acquisition(self):
        from micro_agi.etbs import bald_acquisition
        import numpy as np
        models = [lambda x: 1.0 * x, lambda x: 1.2 * x]
        candidates = np.array([1.0, 2.0, 3.0])
        selected = bald_acquisition(models, candidates, n_samples=1)
        self.assertEqual(len(selected), 1)
        self.assertIn(selected[0], candidates)

    def test_curiosity_threshold_manager(self):
        from micro_agi.layer3_praxis import CuriosityThresholdManager
        manager = CuriosityThresholdManager(base_threshold=0.85)
        self.assertEqual(manager.adaptive_threshold, 0.85)
        val = manager.update(True)
        self.assertGreater(val, 0.8)

    def test_robust_multimodal_model(self):
        from micro_agi.etbs import RobustMultiModalModel
        import numpy as np
        model = RobustMultiModalModel([1.0, 2.0])
        x = np.linspace(1, 5, 10)
        y = 2.0 * x + 0.5 * (x**2)
        model.fit(x, y)
        self.assertEqual(len(model.k), 2)
        preds = model.predict(x[:3])
        self.assertEqual(len(preds), 3)

    def test_reality_check_layer(self):
        from micro_agi.etbs import RealityCheckLayer
        import numpy as np
        layer = RealityCheckLayer()
        self.assertEqual(layer.correction_factor, 1.0)

        class MockEngine:
            def simulate(self, x):
                return np.array([2.0 * x, 2.0 * x])

        factor = layer.inject_known_perturbation(lambda x: 2.0 * x, MockEngine())
        self.assertTrue(factor > 0)

    def test_self_proving_hypothesis_engine(self):
        from micro_agi.etbs import SelfProvingHypothesisEngine
        engine = SelfProvingHypothesisEngine()
        res = engine.run_generation()
        self.assertEqual(res['generation'], 1)
        self.assertIn('crps', res)
        self.assertIn('verisimilitude', res)

if __name__ == "__main__":
    unittest.main()
