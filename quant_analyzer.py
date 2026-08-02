import numpy as np
import pandas as pd
import yfinance as yf


def analyze_basket(tickers, start_date="2023-01-01", rf_rate=0.045):
    """Calculates basic risk and return metrics for a ticker basket."""
    print(f"Downloading market data for: {', '.join(tickers)}...")

    # Grab auto-adjusted close prices and handle missing data
    data = yf.download(tickers, start=start_date, auto_adjust=True)
    prices = data["Close"] if "Close" in data else data

    if isinstance(prices, pd.Series):
        prices = prices.to_frame()

    prices = prices.ffill().dropna()

    if prices.empty:
        print("Error: No price data returned. Check tickers or date range.")
        return None

    # Calculate daily returns
    daily_rets = prices.pct_change().dropna()

    # Core Metrics (Vectorized)
    total_ret = (prices.iloc[-1] / prices.iloc[0]) - 1
    ann_ret = daily_rets.mean() * 252
    ann_vol = daily_rets.std() * np.sqrt(252)

    # Risk-adjusted metrics
    sharpe = (ann_ret - rf_rate) / ann_vol

    # Max Drawdown calculation
    cum_rets = (1 + daily_rets).cumprod()
    peak = cum_rets.cummax()
    drawdown = (cum_rets - peak) / peak
    max_dd = drawdown.min()

    # Combine into summary DataFrame
    df_results = pd.DataFrame(
        {
            "Total Return": total_ret,
            "Ann. Volatility": ann_vol,
            "Sharpe Ratio": sharpe,
            "Max Drawdown": max_dd,
        }
    )

    # Format output for printing
    print(f"\n--- Portfolio Summary (Rf = {rf_rate:.2%}) ---")
    out = df_results.copy()
    out["Total Return"] = out["Total Return"].map("{:.2%}".format)
    out["Ann. Volatility"] = out["Ann. Volatility"].map("{:.2%}".format)
    out["Sharpe Ratio"] = out["Sharpe Ratio"].map("{:.2f}".format)
    out["Max Drawdown"] = out["Max Drawdown"].map("{:.2%}".format)

    print(out.to_string())
    return df_results


if __name__ == "__main__":
    assets = ["SPY", "QQQ", "IWD", "GLD", "TLT"]
    analyze_basket(assets)
