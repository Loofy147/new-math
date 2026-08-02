#!/usr/bin/env python3
"""
Micro-AGI Live Kaggle Competition Demonstration
Downloads data, predicts using Micro-AGI decision logic, and submits predictions.
"""
import os
import csv
import logging
from micro_agi.kaggle_integration import KaggleCompetitionIntegration

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("demo_kaggle")

def main():
    print("=========================================================")
    print("      Micro-AGI Live Kaggle Competition Demonstration    ")
    print("=========================================================\n")

    # Ensure KAGGLE_API_TOKEN is available or fall back
    if "KAGGLE_API_TOKEN" not in os.environ:
        logger.warning("KAGGLE_API_TOKEN environment variable not set. Running in SIMULATED fallback mode.")

    # Initialize Kaggle Competition Integration
    comp_slug = "titanic"
    path = "./data/titanic"

    logger.info(f"Initializing KaggleCompetitionIntegration for '{comp_slug}'...")
    integration = KaggleCompetitionIntegration()

    # Step 1: Download competition files
    logger.info(f"Downloading data files for competition '{comp_slug}'...")
    integration.download_competition_data(comp_slug, path=path)

    train_file = os.path.join(path, "train.csv")
    test_file = os.path.join(path, "test.csv")

    if os.path.exists(test_file):
        logger.info(f"Successfully located test data: {test_file}")
    else:
        logger.error("Could not find test.csv. Aborting demo.")
        return

    # Step 2: Use Micro-AGI symbolic reasoning logic to perform predictions
    # Classic Titanic high-accuracy rule: Female passengers survive (1), Male passengers perish (0).
    logger.info("Executing Micro-AGI symbolic model inference on test dataset...")

    predictions = []
    with open(test_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            passenger_id = row.get("PassengerId") or row.get("id")
            sex = row.get("Sex", "male").lower()

            # Formulate prediction: 1 if female, 0 if male
            survived = 1 if "female" in sex else 0
            predictions.append({
                "PassengerId": passenger_id,
                "Survived": survived
            })

    # Step 3: Write predictions to a submission file
    submission_file = os.path.join(path, "titanic_submission.csv")
    logger.info(f"Writing {len(predictions)} predictions to: {submission_file}")

    with open(submission_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["PassengerId", "Survived"])
        writer.writeheader()
        writer.writerows(predictions)

    # Step 4: Submit predictions to Kaggle
    logger.info(f"Submitting predictions to Kaggle competition '{comp_slug}'...")
    message = "Micro-AGI Automated Rule-Based Inference Submission"
    submission_res = integration.submit_prediction(comp_slug, submission_file, message)

    print("\n[Submission Result]:")
    print(f"  - Competition: {submission_res.get('competition')}")
    print(f"  - File Path: {submission_res.get('file_path')}")
    print(f"  - Status: {submission_res.get('status')}")
    if "submission_id" in submission_res:
        print(f"  - Submission ID: {submission_res.get('submission_id')}")

    # Step 5: Fetch Leaderboard status
    logger.info(f"Fetching leaderboard for '{comp_slug}'...")
    leaderboard = integration.get_leaderboard(comp_slug)

    print("\n[Leaderboard Preview]:")
    for entry in leaderboard[:5]:
        print(f"  Rank {entry.get('rank')}: {entry.get('teamName')} - Score: {entry.get('score')}")

    print("\n=========================================================")
    print("      Live Kaggle Competition Demo Complete!             ")
    print("=========================================================")

if __name__ == "__main__":
    main()
