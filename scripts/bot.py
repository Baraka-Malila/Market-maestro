import yaml
import requests

# Load configuration from config.yaml
def load_config():
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config

# Connect to Deriv API
def connect_to_deriv(api_key, api_url):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(f"{api_url}/v3/tick", headers=headers)

    if response.status_code == 200:
        print("Successfully connected to Deriv API")
    else:
        print(f"Failed to connect to Deriv API. Status code: {response.status_code}")
    return response

if __name__ == "__main__":
    config = load_config()
    
    # Access the keys properly
    api_key = config["api"]["api_key"]  # Correctly access the API key
    api_url = config["api"]["api_url"]   # Correctly access the API URL

    connect_to_deriv(api_key, api_url)
