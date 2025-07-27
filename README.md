# 💹 Crypto Trading Bot

This project is a real-time, modular, and CLI-based trading bot built to interact with the **Binance Testnet API**. It supports multiple order types, strategies, and a basic user interface. The project is structured and written for IT industry-level backend development.

---

## 📦 Features

- ✅ Market Orders (Buy/Sell)
- ✅ Limit Orders
- ✅ Stop-Limit Orders
- ✅ OCO (One-Cancels-the-Other) Orders
- ✅ TWAP (Time Weighted Average Price)
- ✅ Grid Trading Strategy
- ✅ CLI Interface for interaction
- ✅ Logging, error handling, and API key security
- ✅ Final Report with screenshots and logs

---

## 🧠 Project Structure

Srinivas_binance_bot/
│
├── src/
│ ├── market_orders.py # Place market buy/sell orders
│ ├── limit_orders.py # Place limit buy/sell orders
│ ├── grid.py # Grid strategy logic
│ ├── stop_limit.py # Stop-limit functionality
│ ├── bot.py # Main runner
│ └── advanced/
│ ├── oco.py # OCO logic
│ └── twap.py # TWAP order logic
│
├── ui/
│ └── cli_ui.py # CLI interface for user input
│
├── .env # API key/secret (secure)
├── bot.log # Logs of activities/errors
├── report.pdf # Documentation with screenshots
└── README.md # This file

yaml
Copy
Edit

---

## 🔐 Setup Instructions

### 1. Clone the Repo
```bash
git clone <your-repo-url>
cd Srinivas_binance_bot
2. Install Dependencies
bash
Copy
Edit
pip install python-binance python-dotenv
3. Configure API Keys
Create a .env file in the root folder:

env
Copy
Edit
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_api_secret
🔐 These keys are Testnet-only and do not affect real assets.

🚀 Running the Bot
Use the CLI to interact with the bot:

bash
Copy
Edit
python ui/cli_ui.py
Then follow the prompt to select the order type:

mathematica
Copy
Edit
Choose an option:
1. Market Order
2. Limit Order
3. Stop-Limit Order
4. OCO Order
5. TWAP Strategy
6. Grid Trading Strategy
📸 Report & Logs
report.pdf contains screenshots, API calls, order confirmations, and error handling examples.

bot.log includes all raw logs of trading attempts and responses for audit.

📘 Example Order Log
pgsql
Copy
Edit
[INFO] 2025-07-27 12:04:01 - Placed MARKET BUY order for BTCUSDT at 100.00 USDT
[INFO] 2025-07-27 12:05:10 - TWAP order triggered: 5 chunks of 0.001 BTC every 5s
🛠️ Built With
Python 3.10+

python-binance

dotenv

Logging, CLI, REST API, and Real-time order simulation

📈 Future Improvements
Web dashboard using Flask/React

Telegram alerts on order execution

DB integration (MongoDB/PostgreSQL)

Backtesting module for strategies

👤 Author
Pujala Srinivas
MTech in Computer Science | Backend Developer
📧 Email: [YourEmail@example.com]
📎 Resume: [Resume Link]

📜 License
MIT License. For educational and demo use on Binance Testnet only.

yaml
Copy
Edit

---

Let me know if you want:
- A **ZIP file** of the full project
- **Screenshots** added to the README
- An **auto-run script** for first-time setup

Ready for submission! ✅
