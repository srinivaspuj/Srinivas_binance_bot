import os
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize Binance Futures Testnet client
client = Client(api_key=API_KEY, api_secret=API_SECRET, testnet=True)

# Order config
symbol = "BTCUSDT"
order_quantity = 0.001
limit_price = 60000  # Change based on your testing

def place_limit_order():
    try:
        print(f"📦 Placing LIMIT BUY order for {symbol} at ${limit_price}...")
        response = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=order_quantity,
            price=str(limit_price)
        )
        print("✅ Order Placed:", response)
    except Exception as e:
        print("❌ Error placing order:", str(e))

if __name__ == "__main__":
    place_limit_order()
