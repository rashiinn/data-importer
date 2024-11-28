from sqlalchemy import create_engine
import yaml

def get_db_engine(config_path="config/config.yaml"):
    """Creates and returns a SQLAlchemy engine."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    db = config['database']
    
    # Construct connection string
    connection_string = (
        f"postgresql+psycopg2://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
    )
    
    return create_engine(connection_string)
