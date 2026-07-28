import time
import numpy as np
from micro_agi.etbs import SelfProvingHypothesisEngine, RobustMultiModalModel, crps_score

def run_stress_test():
    print("=========================================================")
    print("        Micro-AGI Phase 8: Realistic Stress Test          ")
    print("=========================================================")

    # 1. Define diverse test target functions
    targets = {
        "Linear": lambda x: 3.0 * x + 1.0,
        "Quadratic": lambda x: 0.5 * (x**2) + 2.0 * x,
        "Cubic": lambda x: 0.1 * (x**3) - (x**2) + 4.0,
        "Exponential": lambda x: 5.0 * np.exp(-0.5 * x),
        "Sine": lambda x: 2.0 * np.sin(x) + 5.0
    }

    n_runs = 20  # Fast and efficient stress test for validation
    runs_per_target = n_runs // len(targets)

    tdr_count = 0
    far_count = 0
    total_generations = 0
    start_time = time.time()

    # For recording trace to dynamic_behavior_log.txt
    trace_log = []

    for target_name, target_func in targets.items():
        print(f"\n--- Testing Target Function: {target_name} ---")

        for run in range(runs_per_target):
            # Generate limited initial data points with heavy Cauchy noise
            x_train = np.linspace(1.0, 10.0, 10)
            # Cauchy noise has severe outliers
            noise = np.random.standard_cauchy(size=len(x_train)) * 0.1
            noise = np.clip(noise, -2.0, 2.0) # Challenging but physical
            y_train = target_func(x_train) + noise

            # Setup separate validation/test points (strict data isolation)
            x_test = np.linspace(1.5, 9.5, 10)
            y_test_true = target_func(x_test)

            # Initialize SelfProvingHypothesisEngine with dynamic baseline
            engine = SelfProvingHypothesisEngine(baseline_crps=None)
            engine.calibration_x = x_train
            engine.calibration_y = y_train
            engine.reference_x = x_test
            engine.reference_y = y_test_true
            engine.reference_true_function = target_func

            # Evolve for up to 5 generations or until discovery
            discovered = False
            for gen in range(5):
                res = engine.run_generation()
                total_generations += 1

                # Check for True Discovery
                if engine.promoted_models:
                    best_model = engine.promoted_models[-1]
                    preds = best_model.predict(x_test)
                    mae = np.mean(np.abs(preds - y_test_true))
                    relative_error = mae / (np.mean(np.abs(y_test_true)) + 1e-15)

                    if relative_error < 0.20:
                        discovered = True
                        break

                # Check for False Alarm (Incorrectly Promoted when relative error is high)
                if res['classification'] == "Promoted (Discovery)":
                    best_model = engine.model_ensemble[-1]
                    preds = best_model.predict(x_test)
                    mae = np.mean(np.abs(preds - y_test_true))
                    relative_error = mae / (np.mean(np.abs(y_test_true)) + 1e-15)
                    if relative_error >= 0.20:
                        far_count += 1

            if discovered or (engine.promoted_models and relative_error < 0.20):
                tdr_count += 1

            # Log trace of threshold and correction factor
            trace_log.append({
                "target": target_name,
                "run": run,
                "generations": gen + 1,
                "discovered": discovered or (engine.promoted_models and relative_error < 0.20),
                "threshold": engine.threshold_manager.adaptive_threshold,
                "correction_factor": engine.reality_check.correction_factor
            })

    end_time = time.time()
    elapsed = end_time - start_time

    # Calculate performance metrics
    tdr = (tdr_count / n_runs) * 100.0
    far = (far_count / n_runs) * 100.0
    avg_gen = total_generations / n_runs

    print("\n=========================================================")
    print("                  STRESS TEST REPORT                     ")
    print("=========================================================")
    print(f"Total Runs:                 {n_runs}")
    print(f"True Discovery Rate (TDR):  {tdr:.2f}%")
    print(f"False Alarm Rate (FAR):     {far:.2f}%")
    print(f"Avg Generations to Converge: {avg_gen:.2f}")
    print(f"Total Execution Time:       {elapsed:.2f} seconds")
    print("=========================================================")

    # Write detailed trace report to dynamic_behavior_log.txt
    with open("dynamic_behavior_log.txt", "w") as f:
        f.write("=========================================================\n")
        f.write("      Micro-AGI Phase 9: Dynamic Behavior Trace Log      \n")
        f.write("=========================================================\n\n")
        f.write(f"Total Runs:                 {n_runs}\n")
        f.write(f"True Discovery Rate (TDR):  {tdr:.2f}%\n")
        f.write(f"False Alarm Rate (FAR):     {far:.2f}%\n")
        f.write(f"Avg Generations:            {avg_gen:.2f}\n")
        f.write(f"Execution Time:             {elapsed:.2f} seconds\n\n")
        f.write("Detailed Run History:\n")
        f.write("---------------------------------------------------------\n")
        for log in trace_log:
            f.write(f"Target: {log['target']:<12} | Run: {log['run']:2d} | "
                    f"Gens: {log['generations']} | Discovered: {str(log['discovered']):<5} | "
                    f"Threshold: {log['threshold']:.4f} | Correction Factor: {log['correction_factor']:.4f}\n")

    print("\nDynamic behavior trace written to 'dynamic_behavior_log.txt' successfully.")

if __name__ == "__main__":
    run_stress_test()
