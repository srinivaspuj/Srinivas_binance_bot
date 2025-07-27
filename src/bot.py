import os
from dotenv import load_dotenv
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.oco import place_oco_order
from src.advanced.twap import execute_twap_order

load_dotenv()

def main():
    print("\n📈 Welcome to Srinivas Binance Bot 📈")
    print("Select order type:")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. OCO Order")
    print("4. TWAP Order")

    choice = input("Enter choice (1-4): ").strip()

    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()

    if choice == "1":
        side = input("Buy or Sell? ").upper()
        quantity = float(input("Quantity: "))
        place_market_order(symbol, side, quantity)

    elif choice == "2":
        side = input("Buy or Sell? ").upper()
        quantity = float(input("Quantity: "))
        price = float(input("Limit Price: "))
        place_limit_order(symbol, side, quantity, price)

    elif choice == "3":
        side = input("Buy or Sell? ").upper()
        quantity = float(input("Quantity: "))
        price = float(input("Limit Price: "))
        stop_price = float(input("Stop Price: "))
        stop_limit_price = float(input("Stop Limit Price: "))
        place_oco_order(symbol, side, quantity, price, stop_price, stop_limit_price)

    elif choice == "4":
        side = input("Buy or Sell? ").upper()
        quantity = float(input("Total Quantity: "))
        interval = int(input("Interval (in seconds): "))
        steps = int(input("Number of Orders: "))
        execute_twap_order(symbol, side, quantity, interval, steps)

    else:
        print("❌ Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main()
