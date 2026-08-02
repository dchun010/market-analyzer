# Market Data & Risk Analyzer

A Python script that fetches historical market data using `yfinance` to calculate key risk metrics (Volatility, Sharpe Ratio, Max Drawdown) for custom stock/ETF portfolios.

## Features
* **Data Fetching & Cleaning:** Automatically pulls adjusted closing prices and handles missing trading days via forward-fill (`ffill`).
* **Risk Metrics:** Computes annualized volatility, maximum drawdown, and risk-adjusted returns against a customizable risk-free rate.
* **Error Handling:** Handles API timeouts and empty ticker data.

## Quickstart

```bash
# Clone and install dependencies
git clone [https://github.com/your-username/market-analyzer.git](https://github.com/your-username/market-analyzer.git)
cd market-analyzer
pip install pandas numpy yfinance

# Run the analyzer
python main.py
