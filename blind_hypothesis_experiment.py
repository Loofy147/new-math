"""
The Blind Hypothesis Experiment (Micro-AGI v3.0 Atlas Edition)
---------------------------------------------------------------
1. Setup: Discover a hidden law that combines two different domains:
   y = 2.5 * x + sin(1.2 * x)
2. Action 1 (Upgrade B): Run "Model Zoo" ensemble with N-1 contingency.
3. Action 2 (Upgrade A): Generate "zero-knowledge attestation" of discovered rules.
4. Action 3 (Diagnosis B): Active sampling in "camouflaged" mode (Kyle model).
5. Action 4 (Diagnosis A): Inject periodic "weak ties" every 5 generations.
"""
import numpy as np
import time
from micro_agi.etbs import (
    SelfProvingHypothesisEngine,
    camouflaged_bald_acquisition,
    CorrelationFilter,
    ModelZoo,
    AttestationLayer
)

def run_blind_hypothesis_experiment():
    print("=====================================================================")
    print("      🚀 Starting Experiment: 'The Blind Hypothesis' (v3.0)         ")
    print("=====================================================================")

    # 1. Target function: hybrid across two domains
    def target_func(x):
        return 2.5 * x + np.sin(1.2 * x)

    # Training (calibration) points with minimal noise
    x_train = np.linspace(1.0, 10.0, 15)
    y_train = target_func(x_train) + np.random.normal(0, 0.02, size=len(x_train))

    # Testing (reference) points for validation
    x_test = np.linspace(1.5, 9.5, 10)
    y_test = target_func(x_test)

    # Initialize Engine
    engine = SelfProvingHypothesisEngine(baseline_crps=None)
    engine.calibration_x = x_train
    engine.calibration_y = y_train
    engine.reference_x = x_test
    engine.reference_y = y_test
    engine.reference_true_function = target_func

    print("\n--- Running 10 Generations of the Atlas-enhanced Discovery ---")

    experiment_log = []
    start_time = time.time()

    for gen in range(1, 11):
        print(f"\n[Generation {gen}]")

        # Action 4 (Diagnosis A): Weak Ties Injection (done periodically or manually)
        is_weak_tie_gen = (gen % 5 == 0)
        if is_weak_tie_gen:
            print("  -> [Diagnosis A] Injecting Weak Tie / External dataset...")
            res = engine.inject_weak_tie()
        else:
            res = engine.run_generation()

        # Action 3 (Diagnosis B): Camouflaged active sampling
        # We want to select 2 new query candidate points from a large pool
        candidate_pool = np.linspace(1.0, 12.0, 50)
        camouflaged_queries = camouflaged_bald_acquisition(
            model_ensemble=engine.model_ensemble,
            candidate_points=candidate_pool,
            n_samples=2,
            camouflage_ratio=1.5
        )
        print(f"  -> [Diagnosis B] Camouflaged Query Points (Kyle Model): {np.round(camouflaged_queries, 3)}")

        # Status and outputs
        print(f"  -> Model Classification: {res['classification']}")
        print(f"  -> Empirical Verisimilitude V: {res['verisimilitude']:.4f}")
        print(f"  -> Adaptive Threshold: {res['adaptive_threshold']:.4f}")
        print(f"  -> Correction Factor: {res['correction_factor']:.4f}")

        # Action 1 (Upgrade B): N-1 Contingency Check
        if res.get("fallback_active"):
            print("  -> [Upgrade B] ⚠️ Best model failed! Activated N-1 Contingency Fallback Model.")
        else:
            print("  -> [Upgrade B] Zoo Operating normally (no fallback needed).")

        # Action 2 (Upgrade A): Cryptographic Attestation Proof
        if res.get("attestation_proof"):
            proof = res["attestation_proof"]
            print(f"  -> [Upgrade A] 🔐 Cryptographic Attestation Commitment: {proof['commitment'][:20]}...")
            print(f"  -> [Upgrade A] Verification Status: {proof['status']} (Error: {proof['relative_error']:.2%})")

        experiment_log.append({
            "generation": gen,
            "verisimilitude": res["verisimilitude"],
            "classification": res["classification"],
            "fallback_active": res.get("fallback_active", False),
            "attested": res.get("attestation_proof") is not None
        })

    end_time = time.time()
    elapsed = end_time - start_time

    print("\n=====================================================================")
    print("                     EXPERIMENT COMPLETED                            ")
    print("=====================================================================")
    print(f"Total Execution Time: {elapsed:.2f} seconds")
    print("Summary of Generations:")
    for log in experiment_log:
        attest_str = "🔐 Yes" if log["attested"] else "❌ No"
        fallback_str = "⚠️ Fallback" if log["fallback_active"] else "✅ Normal"
        print(f"  Gen {log['generation']:2d} | V: {log['verisimilitude']:.4f} | "
              f"Class: {log['classification']:<25} | Zoo: {fallback_str:<10} | Attested: {attest_str}")
    print("=====================================================================")

if __name__ == "__main__":
    run_blind_hypothesis_experiment()
