import unittest
import numpy as np
from micro_agi.etbs import (
    AttestationLayer, ModelZoo, CorrelationFilter,
    camouflaged_bald_acquisition, RobustMultiModalModel, SelfProvingHypothesisEngine
)

class TestAtlasV3Upgrades(unittest.TestCase):

    def setUp(self):
        self.x = np.linspace(1, 5, 20)
        self.y = 2.0 * self.x + 0.5 * (self.x ** 2)

    def test_upgrade_a_attestation_layer(self):
        # Setup and fit model
        model = RobustMultiModalModel([1.0, 2.0])
        model.fit(self.x, self.y)

        # Test commitment is a non-empty string and looks like sha256
        commitment = AttestationLayer.compute_commitment(model)
        self.assertIsInstance(commitment, str)
        self.assertEqual(len(commitment), 64)

        # Test proof generation
        x_attest = np.linspace(1.5, 4.5, 5)
        y_attest = 2.0 * x_attest + 0.5 * (x_attest ** 2)
        proof = AttestationLayer.generate_proof(model, x_attest, y_attest)

        self.assertEqual(proof["commitment"], commitment)
        self.assertTrue(proof["is_valid"])
        self.assertEqual(proof["status"], "Verification Successful")
        self.assertLess(proof["relative_error"], 0.20)

    def test_upgrade_b_model_zoo_with_n_1_contingency(self):
        zoo = ModelZoo(capacity=3)

        # Create two distinct models
        model_poly = RobustMultiModalModel([1.0, 2.0])
        model_poly.fit(self.x, self.y)

        model_exp = RobustMultiModalModel(['exp', 1.0])
        model_exp.fit(self.x, self.y)

        # Verify families
        self.assertEqual(ModelZoo.get_model_family(model_poly), "Polynomial")
        self.assertEqual(ModelZoo.get_model_family(model_exp), "Exponential")

        # Add models to zoo
        zoo.add_model(model_poly, 0.95)
        zoo.add_model(model_exp, 0.35)

        # Test best model is model_poly (higher score)
        self.assertEqual(zoo.get_best_model(), model_poly)

        # Test fallback model is model_exp (N-1 contingency)
        self.assertEqual(zoo.get_fallback_model(), model_exp)

        # Prune to capacity test
        model_trig = RobustMultiModalModel(['sin', 1.0])
        model_trig.fit(self.x, self.y)
        zoo.add_model(model_trig, 0.80)

        # Since model_trig score (0.80) is between poly and exp, order is: poly, trig, exp
        self.assertEqual(zoo.get_best_model(), model_poly)
        self.assertEqual(zoo.get_fallback_model(), model_trig)

    def test_upgrade_c_correlation_filter(self):
        # We use np.linspace(1, 10, 50) where x^1 and x^2 correlation is ~0.976 < 0.995.
        x_pos = np.linspace(1, 10, 50)
        candidates = [1.0, 1.01, 2.0, 'sin']
        filtered = CorrelationFilter.filter_exponents(candidates, existing=[], x=x_pos)

        # 1.01 should be filtered out because correlation with 1.0 is > 0.995
        self.assertIn(1.0, filtered)
        self.assertNotIn(1.01, filtered)
        self.assertIn(2.0, filtered)
        self.assertIn('sin', filtered)

    def test_diagnosis_a_weak_ties(self):
        engine = SelfProvingHypothesisEngine()
        # Initial calibration
        self.assertEqual(engine.generation, 0)

        # Inject weak tie
        res = engine.inject_weak_tie()
        self.assertTrue(res["weak_tie_injected"])
        self.assertEqual(res["generation"], 1)

    def test_diagnosis_b_camouflaged_bald_acquisition(self):
        # Setup mock ensemble
        models = [
            lambda x: 2.0 * x,
            lambda x: 2.1 * x
        ]
        candidates = np.linspace(1, 10, 10)

        # Select 2 samples with camouflage ratio 1.5 -> expect 2 high value + 3 distractors = 5 total
        selected = camouflaged_bald_acquisition(models, candidates, n_samples=2, camouflage_ratio=1.5)
        self.assertEqual(len(selected), 5)
        for pt in selected:
            self.assertIn(pt, candidates)

if __name__ == "__main__":
    unittest.main()
