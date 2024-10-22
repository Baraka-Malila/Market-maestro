import asyncio
from deriv_api import DerivAPI
from api_connection import setup_api_connection
from config_loader import load_config

async def get_market_data(api, symbol, subscribe=False):
    try:
        request = {
            "ticks_history": symbol,
            "count": 1000,          
            "end": "latest",
            "start": 1,
            "style": "candles",     
            "granularity": 60,      
            "subscribe": subscribe  
        }
        
        response = await api.send(request)
        if 'error' in response:
            print(f"Error loading market data: {response['error']['message']}")
        else:
            print(f"Market data for {symbol}:")
            return response.get('candles', [])
    except Exception as e:
        print(f"Failed to get market data: {e}")

async def main():
    api = await setup_api_connection()  # Get the connected API instance
    if api:
        config = load_config()
        symbol = config["trading"]["symbols"][0]  # Use the first symbol from config
        market_data = await get_market_data(api, symbol=symbol)
        print(market_data)

if __name__ == "__main__":
    asyncio.run(main())
