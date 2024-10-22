import yaml
import os

def load_config():
    # Correctly set the path to the config.yaml file
    config_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')

    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    
    return config
