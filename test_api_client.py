import unittest
from data_importer.api_client import fetch_data

class TestApiClient(unittest.TestCase):
    def test_fetch_data(self):
        # Replace with a mock or test URL
        test_url = "https://api.restful-api.dev/objects"
        data = fetch_data(test_url)
        self.assertFalse(data.empty)

if __name__ == "__main__":
    unittest.main()
