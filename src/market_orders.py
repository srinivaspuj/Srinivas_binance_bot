# src/market_orders.py

import logging
import os
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

# Load API credentials
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize client
client = Client(API_KEY, API_SECRET)

def place_market_order(symbol: str, quantity: float):
    """
    Places a market buy order.
    """
    try:
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        logging.info(f"Market BUY order placed: {order}")
        print(f"✅ Market BUY order placed successfully for {symbol}, Quantity: {quantity}")
        return order
    except Exception as e:
        logging.error(f"Error placing market BUY order: {e}")
        print(f"❌ Error placing market BUY order: {e}")
        return None

def place_market_sell(symbol: str, quantity: float):
    """
    Places a market sell order.
    """
    try:
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        logging.info(f"Market SELL order placed: {order}")
        print(f"✅ Market SELL order placed successfully for {symbol}, Quantity: {quantity}")
        return order
    except Exception as e:
        logging.error(f"Error placing market SELL order: {e}")
        print(f"❌ Error placing market SELL order: {e}")
        return None

# Test block (Optional: You can run this file directly to test)
if __name__ == "__main__":
    # Be careful — this will actually place live orders if API keys are active.
    place_market_order("BTCUSDT", 0.001)   # Example
    place_market_sell("BTCUSDT", 0.001)  # Example
