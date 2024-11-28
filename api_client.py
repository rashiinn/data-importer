import requests
import pandas as pd

def fetch_data(url):
    """Fetches data from the given URL and returns a Pandas DataFrame."""
    try:
        response = requests.get(url)
        response.raise_for_status()

        json_data = response.json()
        data = pd.json_normalize(json_data)
        return data
    except ValueError as ve:
        raise RuntimeError(f"Error parsing JSON data: {ve}")
    except Exception as e:
        raise RuntimeError(f"Error fetching data: {e}")