# Market Data & Risk Analyzer

Python script using `yfinance` to pull historical market prices and calculate volatility, max drawdown, and Sharpe ratios for stocks or ETFs.

## Features

- Pulls adjusted closing prices and fills missing trading dates (`ffill`).
- Calculates annualized volatility, peak-to-trough max drawdown, and risk-adjusted returns against a set risk-free rate.
- Error handling for API timeouts, bad tickers, and empty dataframes.

## Dependencies

- Python 3
- pandas
- numpy
- yfinance

## Sample Output

| Ticker | Ann. Volatility | Max Drawdown | Sharpe Ratio | Risk-Free Rate |
| :---   | :---            | :---         | :---         | :---           |
| AAPL   | 22.40%          | -14.20%      | 1.45         | 4.25%          |
| SPY    | 15.10%          | -8.70%       | 1.12         | 4.25%          |
| QQQ    | 19.80%          | -11.50%      | 1.28         | 4.25%          |

## How to Run

# Clone the repository
git clone https://github.com/dchun010/market-analyzer.git
cd market-analyzer

# Install dependencies
pip install yfinance pandas numpy

# Run the analyzer
python quant_analyzer.py
