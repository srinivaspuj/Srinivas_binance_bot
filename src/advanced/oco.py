from binance.client import Client
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Load API keys from .env
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize client for SPOT (OCO works only on SPOT)
client = Client(API_KEY, API_SECRET)
client.API_URL = 'https://testnet.binance.vision/api'  # SPOT testnet URL

# Logging
logging.basicConfig(filename='bot.log', level=logging.INFO)

def place_oco_order(symbol, quantity, price, stop_price, stop_limit_price):
    try:
        order = client.create_oco_order(
            symbol=symbol,
            side=Client.SIDE_SELL,
            quantity=quantity,
            price=price,  # Limit price
            stopPrice=stop_price,  # Stop price
            stopLimitPrice=stop_limit_price,  # Limit price after stop is hit
            stopLimitTimeInForce=Client.TIME_IN_FORCE_GTC
        )
        logging.info(f"OCO Order placed successfully: {order}")
        print("✅ OCO Order placed:", order)
    except Exception as e:
        logging.error(f"Error placing OCO Order: {e}")
        print("❌ Failed to place OCO Order:", e)

if __name__ == "__main__":
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter limit price: "))
    stop_price = float(input("Enter stop price: "))
    stop_limit_price = float(input("Enter stop-limit price: "))

    place_oco_order(symbol, quantity, price, stop_price, stop_limit_price)
