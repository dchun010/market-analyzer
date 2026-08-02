import yfinance as yf
import pandas as pd
import numpy as np


def run_quant_analysis(tickers, start_date="2023-01-01", risk_free_rate=0.045):
    """
    Fetches market data, calculates momentum returns, annual volatility,
    Sharpe ratio, and Maximum Drawdown for a basket of assets.

    Parameters
    ----------
    tickers : list of str
        Ticker symbols to analyze.
    start_date : str
        Start date for historical data (YYYY-MM-DD).
    risk_free_rate : float
        Annualized risk-free rate used in the Sharpe ratio calculation.
        Update this to reflect current conditions (e.g., 3-month T-bill rate).
    """
    print(f"Fetching market data for: {', '.join(tickers)}...")

    # 1. Fetch price data
    # auto_adjust=True returns split/dividend-adjusted prices under the
    # 'Close' column. Set explicitly so it's clear which series we're using
    # (yfinance's default for this flag has changed across versions).
    try:
        df = yf.download(tickers, start=start_date, auto_adjust=True)['Close']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

    if df is None or df.empty:
        print("No data returned. Check your tickers and date range.")
        return None

    # Handle single vs multiple tickers (yfinance returns a Series for one ticker)
    if isinstance(df, pd.Series):
        df = df.to_frame(name=tickers[0])

    # Clean missing values
    df = df.ffill().dropna()

    if df.empty:
        print("No overlapping data after cleaning. Try a different date range.")
        return None

    # 2. Calculate Daily Returns
    daily_returns = df.pct_change().dropna()

    metrics = []

    for ticker in tickers:
        if ticker not in daily_returns.columns:
            print(f"Warning: no data for {ticker}, skipping.")
            continue

        asset_returns = daily_returns[ticker]

        # Total Return over the sample period
        total_return = (df[ticker].iloc[-1] / df[ticker].iloc[0]) - 1

        # Annualized Return
        # Note: this uses arithmetic mean daily return * 252 trading days,
        # not compounded/geometric (CAGR) return. For volatile assets or
        # short samples these can diverge noticeably -- worth flagging if
        # comparing against CAGR-based figures elsewhere.
        ann_return = asset_returns.mean() * 252

        # Annualized Volatility (Risk)
        ann_vol = asset_returns.std() * np.sqrt(252)

        # Sharpe Ratio
        sharpe_ratio = (ann_return - risk_free_rate) / ann_vol if ann_vol != 0 else np.nan

        # Maximum Drawdown Calculation
        cumulative = (1 + asset_returns).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        max_drawdown = drawdown.min()

        metrics.append({
            "Ticker": ticker,
            "Total Return": f"{total_return:.2%}",
            "Ann. Volatility": f"{ann_vol:.2%}",
            "Sharpe Ratio": round(sharpe_ratio, 2) if not np.isnan(sharpe_ratio) else "N/A",
            "Max Drawdown": f"{max_drawdown:.2%}"
        })

    if not metrics:
        print("No metrics could be calculated.")
        return None

    # 3. Output Clean Summary Table
    results_df = pd.DataFrame(metrics)
    print("\n" + "=" * 50)
    print("      QUANTITATIVE RISK & MOMENTUM SUMMARY")
    print(f"      Risk-Free Rate Assumed: {risk_free_rate:.2%}")
    print("=" * 50)
    print(results_df.to_string(index=False))
    return results_df


if __name__ == "__main__":
    # Test basket: S&P 500, Tech, Value, Gold, Bonds
    basket = ["SPY", "QQQ", "IWD", "GLD", "TLT"]
    run_quant_analysis(basket)