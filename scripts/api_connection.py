import asyncio
import logging
from config_loader import load_config
from deriv_api import DerivAPI

logging.basicConfig(level=logging.DEBUG)

async def setup_api_connection():
    config = load_config()
    logging.debug("Loaded Config: %s", config)

    api = DerivAPI(
        app_id=config['api']['app_id'],
        api_token=config['api']['api_key'],
        api_url=config['api']['api_url']
    )
    
    logging.debug("DerivAPI methods: %s", dir(api))

    # Print out the methods of the api object for debugging
    logging.debug("DerivAPI methods: %s", dir(api))

    # Attempt to connect or login using available methods
    try:
        # Use correct method to connect or login
        await api.login()  # Adjust according to available methods
        logging.info("API connected successfully.")
    except AttributeError as e:
        logging.error("Connection method not found: %s", e)
    except Exception as e:
        logging.error("Failed to connect to API: %s", e)

if __name__ == "__main__":
    asyncio.run(setup_api_connection())
