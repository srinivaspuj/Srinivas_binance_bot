from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Connect to Binance Futures Testnet
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = 'https://testnet.binancefuture.com'

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",  # STOP for stop-limit in futures
            quantity=quantity,
            price=str(limit_price),
            stopPrice=str(stop_price),
            timeInForce="GTC"
        )
        print(f"✅ STOP-LIMIT order placed: {order}")
        return order

    except Exception as e:
        print(f"❌ Failed to place STOP-LIMIT order: {e}")
        return None

# Example usage:
# place_stop_limit_order("BTCUSDT", SIDE_SELL, 0.001, stop_price=27500, limit_price=27400)
