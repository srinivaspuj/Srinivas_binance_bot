import time
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
client = Client(api_key, api_secret)

def place_grid_orders(symbol, lower_price, upper_price, grid_count, quantity):
    step = (upper_price - lower_price) / (grid_count - 1)
    orders = []
    for i in range(grid_count):
        price = round(lower_price + step * i, 2)
        side = SIDE_BUY if i % 2 == 0 else SIDE_SELL
        try:
            order = client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)
            )
            orders.append(order)
            print(f"{side} order placed at {price}")
        except Exception as e:
            print(f"Failed to place {side} order at {price}: {e}")
        time.sleep(1)
    return orders

# Example usage
# place_grid_orders('BTCUSDT', 27000, 28000, 5, 0.001)