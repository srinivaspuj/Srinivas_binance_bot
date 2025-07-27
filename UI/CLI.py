import sys
import os

# Ensure root directory is in path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
from binance.enums import *

from src.market_orders import place_market_order, place_market_sell
from src.limit_orders import place_limit_order
from src.stop_limit import place_stop_limit_order
from src.grid import place_grid_orders
from src.advanced.oco import place_oco_order
from src.advanced.twap import place_twap_order

# Load API credentials
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def main():
    print("\n Welcome to Srinivas Crypto Trading Bot ")

    while True:
        print("\nSelect an option:")
        print("1. Market Order")
        print("2. Limit Order")
        print("3. OCO Order")
        print("4. TWAP Order")
        print("5. Grid Order")
        print("6. Stop-Limit Order")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("👋 Exiting bot...")
            break

        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
        side = input("Side (BUY/SELL): ").upper()

        if choice == "1":
            quantity = float(input("Enter quantity: "))
            if side == "BUY":
                place_market_order(symbol, quantity)
            elif side == "SELL":
                place_market_sell(symbol, quantity)
            else:
                print("❌ Invalid side. Please enter BUY or SELL.")

        elif choice == "2":
            quantity = float(input("Enter quantity: "))
            price = float(input("Enter limit price: "))
            place_limit_order(symbol, side, quantity, price)

        elif choice == "3":
            quantity = float(input("Enter quantity: "))
            price = float(input("Enter limit price: "))
            stop_price = float(input("Enter stop price: "))
            stop_limit_price = float(input("Enter stop-limit price: "))
            place_oco_order(symbol, side, quantity, price, stop_price, stop_limit_price)

        elif choice == "4":
            quantity = float(input("Enter total quantity to buy/sell: "))
            interval = float(input("Interval in seconds between orders: "))
            parts = int(input("Split into how many parts?: "))
            place_twap_order(symbol, side, quantity, interval, parts)

        elif choice == "5":
            lower = float(input("Lower price: "))
            upper = float(input("Upper price: "))
            grid_count = int(input("Number of grids: "))
            quantity = float(input("Quantity per grid: "))
            place_grid_orders(symbol, lower, upper, grid_count, quantity)

        elif choice == "6":
            stop_price = float(input("Enter stop price: "))
            limit_price = float(input("Enter limit price: "))
            quantity = float(input("Enter quantity: "))
            place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)

        else:
            print("❌ Invalid option.")

        again = input("\nPlace another order? (y/n): ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
