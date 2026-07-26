import random
import math
import sympy as sp
from typing import Dict, Any, List, Tuple

class HypothesisGenerator:
    """
    3.1. Hypothesis Generator (HG) (مولّد الفرضيات)
    Draws suggestions from L2 Causal Graph to propose new relations,
    translates them into simulations using SymPy, based on uncertainty levels.
    """
    def __init__(self):
        pass

    def generate_hypothesis(self, causal_nodes: List[str], uncertainty_index: float) -> Dict[str, Any]:
        """
        Generates a hypothesis (H) if uncertainty is high enough, or if requested.
        Maps inputs to a mathematical relation structure.
        """
        if not causal_nodes:
            causal_nodes = ["distance", "mass_1", "mass_2"]

        # Randomly choose nodes to relate
        cause = random.choice(causal_nodes)
        effect = "gravity_force" if cause != "gravity_force" else "acceleration"

        # Propose relation equation symbolically
        # e.g., H: Force relates to cause with exponential factor or power factor
        param = random.choice(["alpha", "beta", "lambda"])
        equation_str = f"G * m1 * m2 / (r ** 2) * exp(-{param} * r)"

        return {
            "id": f"hyp_{random.randint(1000, 9999)}",
            "cause": cause,
            "effect": effect,
            "param": param,
            "proposed_equation": equation_str,
            "uncertainty": uncertainty_index,
            "statement": f"An increased {cause} causes a decayed impact on {effect} regulated by {param}."
        }


class InternalSandbox:
    """
    3.2. Internal Sandbox (IS) (المُحاكي الداخلي)
    A fast quantitative symbolic-numeric causal inference engine.
    Executes SymPy compiled equations thousands of times (simulated here) with Gaussian noise.
    Produces statistical distributions.
    """
    def __init__(self):
        pass

    def run_simulation(self, hypothesis: Dict[str, Any], initial_beliefs: Dict[str, Any], iterations: int = 100) -> Dict[str, Any]:
        """
        Runs a fast Monte Carlo simulation with Gaussian noise.
        """
        equation_str = hypothesis["proposed_equation"]
        param_name = hypothesis["param"]

        # Setup symbols
        G_sym, m1_sym, m2_sym, r_sym, param_sym = sp.symbols(f'G m1 m2 r {param_name}')

        try:
            expr = sp.sympify(equation_str)
            # Lambdify for ultra-fast numeric execution
            func = sp.lambdify((G_sym, m1_sym, m2_sym, r_sym, param_sym), expr, 'math')
        except Exception as e:
            # Fallback direct formula
            func = lambda G, m1, m2, r, p: (G * m1 * m2 / (r**2)) * math.exp(-p * r)

        results = []
        G_val = initial_beliefs.get("gravity_constant", 6.6743e-11)
        m1_val = initial_beliefs.get("mass_1", 1.0)
        m2_val = initial_beliefs.get("mass_2", 1.0)
        r_val = initial_beliefs.get("distance", 1.0)
        p_val = initial_beliefs.get("lambda_decay", 0.05)

        # Simulate over iterations with Gaussian noise
        for _ in range(iterations):
            # Apply gaussian noise to variables
            r_noisy = max(0.01, r_val + random.gauss(0, 0.05 * r_val))
            p_noisy = max(0.0, p_val + random.gauss(0, 0.1 * p_val))

            try:
                out = func(G_val, m1_val, m2_val, r_noisy, p_noisy)
                results.append(out)
            except Exception:
                results.append(0.0)

        mean_val = sum(results) / len(results) if results else 0.0
        variance = sum((x - mean_val)**2 for x in results) / len(results) if results else 0.0

        return {
            "hypothesis_id": hypothesis["id"],
            "raw_results": results[:10], # sample output
            "mean": mean_val,
            "variance": variance,
            "iterations": iterations
        }


class ExternalAnchorFusion:
    """
    6. Integration with External Anchors (التكامل مع المُثبَتات الخارجية)
    Maintains solid, experimentally-proven physical constants & human benchmarks.
    """
    def __init__(self):
        self.anchors = {
            "gravity_constant": 6.6743e-11,
            "speed_of_light": 299792458.0,
            "planck_constant": 6.62607015e-34,
            "expected_gravity_force_at_unit_dist": 6.6743e-11  # validation benchmark
        }

    def fetch_anchor(self, key: str) -> Any:
        return self.anchors.get(key)


class VerificationModule:
    """
    3.3. Verification Module (VM) (مُحقّق النتائج)
    Compares Internal Sandbox outputs with core knowledge base laws, external anchors, and L2 coherence.
    Computes Hybrid Empirical Verisimilitude (V_hybrid).
    """
    def __init__(self):
        self.anchor_fusion = ExternalAnchorFusion()

    def calculate_verisimilitude(self, sim_results: Dict[str, Any], hypothesis: Dict[str, Any], beliefs: Dict[str, Any]) -> float:
        """
        V_hybrid = 2 * (R2 * Coverage) / (R2 + Coverage) - lambda_penalty * MaxErrorRatio
        Returns bounded float [0.0, 1.0] indicating empirical truth likelihood.
        """
        mean_sim = sim_results["mean"]

        # 1. Compare with external expected benchmarks (Anchor Correlation -> R^2)
        expected_ref = self.anchor_fusion.fetch_anchor("expected_gravity_force_at_unit_dist")

        if expected_ref == 0:
            r2 = 1.0
        else:
            diff = abs(mean_sim - expected_ref) / (expected_ref + abs(mean_sim))
            r2 = max(0.0, 1.0 - diff)

        # 2. Coverage calculation
        # Coverage is modeled as structural coherence + noise score
        var_sim = sim_results["variance"]
        expected_var = 1e-22  # Scale of gravity variance
        if expected_var == 0 or var_sim == 0:
            noise_score = 0.5
        else:
            noise_ratio = min(var_sim, expected_var) / max(var_sim, expected_var)
            noise_score = max(0.0, noise_ratio)

        cause = hypothesis["cause"]
        coherence_score = 1.0 if cause in ["distance", "mass_1", "mass_2"] else 0.2

        coverage = (0.6 * noise_score) + (0.4 * coherence_score)

        # 3. MaxErrorRatio
        # Computed as the normalized error of the mean compared to the reference
        max_error_ratio = diff if expected_ref != 0 else 0.0

        # Calculate V_hybrid
        lambda_penalty = 0.1
        if (r2 + coverage) == 0:
            v_hybrid = 0.0
        else:
            harmonic_mean = (2.0 * r2 * coverage) / (r2 + coverage)
            v_hybrid = harmonic_mean - (lambda_penalty * max_error_ratio)

        return min(1.0, max(0.0, v_hybrid))


class FeedbackMapper:
    """
    3.4. Feedback Mapper (FM) (مُخطط التغذية الراجعة)
    Translates Verisimilitude scores into system correction signals.
    - High success (V >= promote_threshold): Add causal node/update positive structure weights in L2, log innovation in L4.
    - Medium failure (GAP: 0.3 < V < promote_threshold): Send to Evolutionary Sandbox for refinement.
    - Severe failure (V <= 0.3): Mark as hallucination, apply negative gradient to inhibit L2 neural weight pathways.
    """
    def __init__(self):
        pass

    def map_feedback(self, verisimilitude: float, hypothesis: Dict[str, Any], promote_threshold: float = 0.85) -> Dict[str, Any]:
        if verisimilitude >= promote_threshold:
            classification = "New Narrative / Discovery"
            action = "Add causal edge to L2 and register as landmark Innovation in L4."
            weight_adjustment = 1.0
        elif verisimilitude > 0.3:
            classification = "Needs Refinement (GAP Region)"
            action = "Resubmit hypothesis to Evolutionary Sandbox for mutation and refinement."
            weight_adjustment = 0.0
        else:
            classification = "Hallucination"
            action = "Inhibit causal connection. Apply negative gradient to suppress the associated neural pathway in L2."
            weight_adjustment = -1.0

        return {
            "hypothesis_id": hypothesis["id"],
            "verisimilitude": verisimilitude,
            "classification": classification,
            "action": action,
            "weight_adjustment": weight_adjustment
        }


class EvolutionarySandbox:
    """
    Experimental Evolutionary Sandbox (Mutation Engine) to refine borderline hypotheses in the GAP region.
    """
    def __init__(self, conduit: 'ETBSConduit'):
        self.conduit = conduit

    def mutate_hypothesis(self, hypothesis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Randomly mutates the hypothesis equation by adding a correction factor or modifying parameters.
        """
        mutated = hypothesis.copy()
        param = hypothesis["param"]
        mutation_bias = hypothesis.get("mutation_bias", 0.0) + random.uniform(-0.05, 0.05)
        mutated["mutation_bias"] = mutation_bias

        # Perturb the proposed equation string slightly to simulate mutation
        mutated["proposed_equation"] = f"G * m1 * m2 / (r ** 2) * exp(-{param} * r) + {mutation_bias:.4f}"
        return mutated

    def refine_hypothesis(self, hypothesis: Dict[str, Any], beliefs: Dict[str, Any], initial_v: float) -> Tuple[Dict[str, Any], float, List[Dict[str, Any]]]:
        """
        Runs the mutation loop up to 10 iterations to optimize verisimilitude V.
        """
        current_hyp = hypothesis
        current_v = initial_v
        history = [{"hypothesis": current_hyp.copy(), "v": current_v}]

        for i in range(10):
            # If we exit the GAP region (either V >= 0.85 or V <= 0.3), stop
            if current_v >= 0.85 or current_v <= 0.3:
                break

            mutated_hyp = self.mutate_hypothesis(current_hyp)
            sim = self.conduit.is_box.run_simulation(mutated_hyp, beliefs)
            new_v = self.conduit.vm.calculate_verisimilitude(sim, mutated_hyp, beliefs)

            # If verisimilitude improves, adopt the mutated hypothesis
            if new_v > current_v:
                current_hyp = mutated_hyp
                current_v = new_v
                history.append({"hypothesis": current_hyp.copy(), "v": current_v})

        return current_hyp, current_v, history


class ETBSConduit:
    """
    The main horizontal conduit linking layers 0-4 dynamically.
    Experimental Translation Bridging Substrate (ETBS).
    """
    def __init__(self):
        self.hg = HypothesisGenerator()
        self.is_box = InternalSandbox()
        self.vm = VerificationModule()
        self.fm = FeedbackMapper()
        self.sandbox = EvolutionarySandbox(self)

    def execute_bridge(self, causal_nodes: List[str], beliefs: Dict[str, Any], uncertainty: float, promote_threshold: float = 0.85) -> Dict[str, Any]:
        # Step 1: Generate hypothesis
        hyp = self.hg.generate_hypothesis(causal_nodes, uncertainty)

        # Step 2: Internal Sandbox simulation (Fast Monte Carlo)
        sim = self.is_box.run_simulation(hyp, beliefs)

        # Step 3: Verify results using hybrid verisimilitude
        v_score = self.vm.calculate_verisimilitude(sim, hyp, beliefs)

        # Step 4: If in GAP region (0.3 < v_score < promote_threshold), run Evolutionary Sandbox!
        was_mutated = False
        mutation_history = []
        if 0.3 < v_score < promote_threshold:
            refined_hyp, refined_v, history = self.sandbox.refine_hypothesis(hyp, beliefs, v_score)
            if refined_v != v_score:
                hyp = refined_hyp
                v_score = refined_v
                was_mutated = True
                mutation_history = history
                # Re-run simulation with the refined hypothesis for final outputs
                sim = self.is_box.run_simulation(hyp, beliefs)

        # Step 5: Map feedback signals using current (possibly refined) v_score
        feedback = self.fm.map_feedback(v_score, hyp, promote_threshold)

        return {
            "hypothesis": hyp,
            "simulation": sim,
            "verisimilitude": v_score,
            "feedback": feedback,
            "was_mutated": was_mutated,
            "mutation_history": mutation_history
        }
