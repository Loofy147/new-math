#!/usr/bin/env python3
"""
Micro-AGI Orchestrator Demonstration
Runs a complete lifecycle of the Probabilistic Neuro-Symbolic general intelligence framework.
"""
from micro_agi.orchestrator import MicroAGIOrchestrator

def main():
    print("=========================================================")
    print("         Micro-AGI Framework: Complete Demo              ")
    print("=========================================================\n")

    # Initialize the Orchestrator with routing threshold 1.5
    orchestrator = MicroAGIOrchestrator(routing_threshold=1.5)

    # ----------------------------------------------------
    # Case 1: Simple interaction (Local Direct processing)
    # ----------------------------------------------------
    print("--- CASE 1: Processing a simple direct query ---")
    query_1 = "Hi Micro-AGI, what is your version?"
    print(f"User: {query_1}")
    result_1 = orchestrator.query_flow(query_1)
    print(f"Route Selected: {result_1['route']}")
    print(f"Complexity: {result_1['complexity']:.4f}")
    print(f"Response: {result_1['response']}")
    print(f"Metrics: {result_1['metrics']}\n")

    # ----------------------------------------------------
    # Case 2: Deep causal reasoning query (Full ASA activation)
    # ----------------------------------------------------
    print("--- CASE 2: Processing a complex existential causal query ---")
    query_2 = "Why does gravity decay existentially with lambda over distance?"
    print(f"User: {query_2}")

    # Let's update world model beliefs beforehand to make it simulated
    orchestrator.layer2.update_beliefs({
        "mass_1": 1e12,
        "mass_2": 5.0,
        "distance": 1.5,
        "lambda_decay": 0.1
    })

    result_2 = orchestrator.query_flow(query_2)
    print(f"Route Selected: {result_2['route']}")
    print(f"Complexity: {result_2['complexity']:.4f}")
    print(f"Motivation Score: {result_2['motivation']:.4f}")
    print(f"Internal Friction: {result_2['friction']:.4f}")
    print(f"Simulated Gravity Force: {result_2['simulation']['gravity_force']:.6e} N")
    print(f"Response: {result_2['response']}")
    print(f"Metrics: {result_2['metrics']}\n")

    # ----------------------------------------------------
    # Case 3: Interactive Learning Loop
    # ----------------------------------------------------
    print("--- CASE 3: Running self-evolution learning loop ---")
    observation = {
        "mass_1": 5e11,
        "mass_2": 10.0,
        "distance": 0.5,
        "lambda_decay": 0.2
    }
    print(f"Injecting new environment observation: {observation}")
    learn_res = orchestrator.learning_loop(observation)
    print(f"Status: {learn_res['status']}")
    print(f"New Simulated Force: {learn_res['simulation_results']['gravity_force']:.6e} N")
    print(f"Ethical/principle Distance: {learn_res['reward_evaluation']['ethical_distance']:.4f}")
    print(f"Metacognition consistent parameters: {learn_res['metacognition']['consistent_beliefs']}")
    print(f"Evolved best causal hyperparameters: {learn_res['metacognition']['best_hyperparameters']}")
    print(f"Narrative Continuity: {learn_res['metacognition']['narrative_state']}")
    print(f"Updated System Metrics: {learn_res['metrics']}")
    print("\n=========================================================")
    print("            Micro-AGI Lifecycle Completed Successfully   ")
    print("=========================================================")

if __name__ == "__main__":
    main()
