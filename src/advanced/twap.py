import time
import math
from binance.client import Client
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Load API keys from .env
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize Futures client
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = 'https://testnet.binancefuture.com'  # Futures testnet

# Logging
logging.basicConfig(filename='bot.log', level=logging.INFO)

def place_twap_order(symbol, total_quantity, intervals, delay, side="BUY"):
    quantity_per_order = math.floor(total_quantity / intervals * 1000) / 1000  # Truncate to 3 decimals

    print(f"TWAP Strategy for {symbol} ({side})")
    print(f"Placing {intervals} orders of {quantity_per_order} every {delay} seconds...")

    for i in range(intervals):
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity_per_order
            )
            logging.info(f"[TWAP] Order {i+1}/{intervals} placed: {order}")
            print(f"✅ Order {i+1} placed at market price")
        except Exception as e:
            logging.error(f"[TWAP] Failed to place order {i+1}: {e}")
            print(f"❌ Failed to place order {i+1}:", e)
        time.sleep(delay)

    print("🎯 TWAP execution complete.")

if __name__ == "__main__":
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    total_quantity = float(input("Enter total quantity to buy/sell: "))
    intervals = int(input("Enter number of intervals: "))
    delay = int(input("Enter delay between orders (in seconds): "))
    side = input("Enter order side (BUY or SELL): ").upper()

    place_twap_order(symbol, total_quantity, intervals, delay, side)
