import yaml
from data_importer.api_client import fetch_data
from data_importer.db import get_db_engine
from data_importer.logger import setup_logger
from data_importer.models import validate_data

def main():
    logger = setup_logger()
    
    try:
        # Load configuration
        with open("config/config.yaml", "r") as file:
            config = yaml.safe_load(file)
        
        # Fetch data
        logger.info("Fetching data from URL.")
        data = fetch_data(config["data_url"])
        
        # Validate data
        logger.info("Validating data.")
        validate_data(data)
        
        # Insert data into the database
        logger.info("Connecting to the database.")
        engine = get_db_engine()
        logger.info("Inserting data into the database.")
        
        
        logger.info("Data import completed successfully!")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
