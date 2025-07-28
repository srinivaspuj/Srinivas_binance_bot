# Srinivas Binance Bot

A CLI-based trading bot for Binance USDT-M Futures, designed to execute multiple order types with robust input validation and logging. This bot supports market and limit orders (mandatory) and advanced orders including OCO, TWAP, and grid orders (bonus features). It uses the Binance Testnet for all API interactions.

## Project Structure

```
Srinivas_binance_bot/
├── .env
├── bot.log
├── README.md
├── Report.pdf
├── UI/
│   └── CLI.py
├── src/
│   ├── __pycache__/
│   ├── bot.py
│   ├── grid.py
│   ├── limit_orders.py
│   ├── market_orders.py
│   ├── stop_limit.py
│   └── advanced/
│       ├── oco.py
│       └── twap.py

```

## Dependencies

- Python 3.8+
- `python-binance` library (`pip install python-binance`)

## Setup Instructions

1. **Install Python**: Ensure Python 3.8 or higher is installed on your system.
2. **Install Dependencies**:
   ```bash
   pip install python-binance
   ```
3. **Register for Binance Testnet**:
   - Create an account at [Binance Testnet](https://testnet.binance.vision/).
   - Generate API key and secret.
4. **Clone the Repository**:
   - If using GitHub, clone the private repository named `[your_name]-binance-bot`.
   - Alternatively, unzip `[your_name]_binance_bot.zip` to access the project files.
5. **Set Up Project Structure**:
   - Ensure all files are placed as shown in the project structure above.
   - The `bot.log` file will be created automatically when the bot runs.

## Usage

Run the bot using the `main.py` script via the command line. The bot supports market, limit, OCO, TWAP, and grid orders. Below are the command-line arguments and examples.

### Command-Line Arguments

```bash
python main.py --api-key <API_KEY> --api-secret <API_SECRET> --symbol <SYMBOL> --order-type <TYPE> --side <SIDE> --quantity <QUANTITY> [--price <PRICE>] [--stop-price <STOP_PRICE>] [--stop-limit-price <STOP_LIMIT_PRICE>] [--duration <DURATION>] [--chunks <CHUNKS>] [--lower-price <LOWER_PRICE>] [--upper-price <UPPER_PRICE>] [--grid-levels <GRID_LEVELS>]
```

- `--api-key`: Binance Testnet API key (required).
- `--api-secret`: Binance Testnet API secret (required).
- `--symbol`: Trading pair (e.g., `BTCUSDT`) (required).
- `--order-type`: Order type (`market`, `limit`, `oco`, `twap`, `grid`) (required).
- `--side`: Order side (`BUY` or `SELL`) (required).
- `--quantity`: Total order quantity (required).
- `--price`: Limit price for `limit` or `oco` orders (optional).
- `--stop-price`: Stop price for `oco` orders (optional).
- `--stop-limit-price`: Stop-limit price for `oco` orders (optional).
- `--duration`: Duration in seconds for `twap` orders (optional).
- `--chunks`: Number of chunks for `twap` orders (optional).
- `--lower-price`: Lower price bound for `grid` orders (optional).
- `--upper-price`: Upper price bound for `grid` orders (optional).
- `--grid-levels`: Number of grid levels for `grid` orders (optional).

### Examples

1. **Market Order**:
   ```bash
   python main.py --api-key your_key --api-secret your_secret --symbol BTCUSDT --order-type market --side BUY --quantity 0.001
   ```
   Places a market buy order for 0.001 BTCUSDT.

2. **Limit Order**:
   ```bash
   python main.py --api-key your_key --api-secret your_secret --symbol BTCUSDT --order-type limit --side BUY --quantity 0.001 --price 50000.0
   ```
   Places a limit buy order for 0.001 BTCUSDT at 50,000 USDT.

3. **OCO Order**:
   ```bash
   python main.py --api-key your_key --api-secret your_secret --symbol BTCUSDT --order-type oco --side BUY --quantity 0.001 --price 50000.0 --stop-price 49000.0 --stop-limit-price 48900.0
   ```
   Places an OCO buy order with a limit price of 50,000 USDT, stop price of 49,000 USDT, and stop-limit price of 48,900 USDT.

4. **TWAP Order**:
   ```bash
   python main.py --api-key your_key --api-secret your_secret --symbol BTCUSDT --order-type twap --side BUY --quantity 0.005 --duration 60 --chunks 5
   ```
   Places a TWAP buy order for 0.005 BTCUSDT, split into 5 market orders over 60 seconds.

5. **Grid Order**:
   ```bash
   python main.py --api-key your_key --api-secret your_secret --symbol BTCUSDT --order-type grid --quantity 0.005 --lower-price 45000.0 --upper-price 55000.0 --grid-levels 5
   ```
   Places a grid of 5 limit orders for 0.005 BTCUSDT, distributed between 45,000 and 55,000 USDT.

### Logging

All actions (initialization, validation, order placement, and errors) are logged to `bot.log` in the project root with timestamps. Check this file for debugging or monitoring order execution.

### Notes

- Ensure quantities and prices comply with Binance's `LOT_SIZE` and `PRICE_FILTER` for the specified symbol.
- Use the Binance Testnet API (https://testnet.binance.vision/) for all interactions.
- For GitHub submission, push the code to a private repository named `[your_name]-binance-bot` and add the instructor as a collaborator.

### Troubleshooting

- **Invalid Symbol/Quantity/Price**: Check `bot.log` for validation errors and ensure inputs meet Binance's symbol filters.
- **API Errors**: Verify API key and secret, and ensure Testnet mode is enabled.
- **Missing Dependencies**: Install `python-binance` using pip.
