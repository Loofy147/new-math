import unittest
import os
import shutil
from unittest.mock import MagicMock, patch
from micro_agi.kaggle_integration import KaggleDataSource, KaggleCompetitionIntegration
from micro_agi.etbs import SelfProvingHypothesisEngine

class TestKaggleIntegration(unittest.TestCase):
    def setUp(self):
        self.temp_dir = "./test_kaggle_data"
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_kaggle_data_source_simulated(self):
        with patch("kaggle.api.kaggle_api_extended.KaggleApi.authenticate", side_effect=Exception("No credentials")):
            source = KaggleDataSource()
            self.assertFalse(source.is_authenticated)

            datasets = source.search_datasets("gravity")
            self.assertEqual(len(datasets), 2)
            self.assertIn("ref", datasets[0])
            self.assertIn("quantum-gravity-dataset", datasets[0]["ref"])

            meta = source.get_dataset_metadata("theisaperez/quantum-gravity-dataset")
            self.assertEqual(meta["title"], "Simulated Physics and Gravity Dataset")

            path = source.download_dataset("theisaperez/quantum-gravity-dataset", path=self.temp_dir)
            self.assertTrue(os.path.exists(path))
            csv_file = os.path.join(path, "theisaperez_quantum-gravity-dataset_simulated.csv")
            self.assertTrue(os.path.exists(csv_file))

    def test_kaggle_competition_integration_simulated(self):
        with patch("kaggle.api.kaggle_api_extended.KaggleApi.authenticate", side_effect=Exception("No credentials")):
            comp = KaggleCompetitionIntegration()
            self.assertFalse(comp.is_authenticated)

            comps = comp.list_competitions("gravity")
            self.assertEqual(len(comps), 2)
            self.assertEqual(comps[0]["ref"], "gravity-coefficient-challenge")

            path = comp.download_competition_data("gravity-coefficient-challenge", path=self.temp_dir)
            self.assertTrue(os.path.exists(os.path.join(path, "train.csv")))
            self.assertTrue(os.path.exists(os.path.join(path, "test.csv")))

            sub_res = comp.submit_prediction("gravity-coefficient-challenge", "./dummy_sub.csv", "Micro-AGI submission")
            self.assertEqual(sub_res["status"], "Submitted successfully (Simulated Mode)")
            self.assertEqual(sub_res["submission_id"], 99999)

            leaderboard = comp.get_leaderboard("gravity-coefficient-challenge")
            self.assertEqual(len(leaderboard), 3)
            self.assertEqual(leaderboard[0]["teamName"], "Micro-AGI Engine (Ours)")

    @patch("kaggle.api.kaggle_api_extended.KaggleApi.authenticate")
    @patch("kaggle.api.kaggle_api_extended.KaggleApi.dataset_list")
    @patch("kaggle.api.kaggle_api_extended.KaggleApi.dataset_metadata")
    @patch("kaggle.api.kaggle_api_extended.KaggleApi.dataset_download_files")
    def test_kaggle_data_source_real_api(self, mock_download, mock_metadata, mock_list, mock_auth):
        mock_auth.return_value = None

        mock_dataset_obj = MagicMock()
        mock_dataset_obj.id = 12345
        mock_dataset_obj.ref = "user/real-dataset"
        mock_dataset_obj.title = "Real Dataset"
        mock_dataset_obj.size = "10 MB"
        mock_dataset_obj.usabilityRating = 0.9

        mock_list.return_value = [mock_dataset_obj]

        def side_effect_metadata(slug, path):
            import json
            with open(os.path.join(path, "dataset-metadata.json"), "w") as f:
                json.dump({"title": "Mocked Metadata", "ref": slug}, f)

        mock_metadata.side_effect = side_effect_metadata

        source = KaggleDataSource()
        self.assertTrue(source.is_authenticated)

        datasets = source.search_datasets("gravity")
        self.assertEqual(len(datasets), 1)
        self.assertEqual(datasets[0]["ref"], "user/real-dataset")

        meta = source.get_dataset_metadata("user/real-dataset", path=self.temp_dir)
        self.assertEqual(meta["title"], "Mocked Metadata")

        path = source.download_dataset("user/real-dataset", path=self.temp_dir)
        self.assertEqual(path, self.temp_dir)
        mock_download.assert_called_once_with("user/real-dataset", path=self.temp_dir, unzip=True)

    def test_self_proving_hypothesis_engine_load_kaggle_data(self):
        engine = SelfProvingHypothesisEngine()

        success = engine.load_data_from_kaggle(
            dataset_slug="user/test-gravity",
            x_col="x",
            y_col="y_true",
            path=self.temp_dir
        )
        self.assertTrue(success)
        self.assertGreater(len(engine.calibration_x), 0)
        self.assertGreater(len(engine.calibration_y), 0)

if __name__ == "__main__":
    unittest.main()
