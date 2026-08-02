# Quantitative Market & Risk Analyzer

A Python-based financial data pipeline and risk engine that fetches time-series market data, cleans missing values, and evaluates risk-adjusted performance metrics across multi-asset portfolios.

## Key Features
* **Automated Ingestion:** Pulls split and dividend-adjusted closing prices via `yfinance`.
* **Data Janitoring:** Handles non-overlapping trading calendars and missing values using forward-fill (`ffill`) imputation.
* **Risk Analytics:** Calculates annualized volatility, maximum drawdowns, and Sharpe ratios against customizable risk-free rates.
* **Defensive Architecture:** Includes error handling for API timeouts and empty dataframe scenarios.

## Technical Stack
* **Language:** Python 3.x
* **Libraries:** `pandas`, `numpy`, `yfinance`

## Sample Output
```text
==================================================
      QUANTITATIVE RISK & MOMENTUM SUMMARY
      Risk-Free Rate Assumed: 4.50%
==================================================
Ticker Total Return Ann. Volatility Sharpe Ratio Max Drawdown
   SPY       45.21%          14.32%         1.82      -10.23%
   QQQ       62.10%          18.65%         1.95      -13.15%
   GLD       28.30%          12.80%         1.45       -8.40%
