# Trading Strategy Project

## Strategy Used

This project uses a simple moving average crossover strategy.

Buy Rule:
- Buy when 20 SMA crosses above 50 SMA

Sell Rule:
- Sell when 20 SMA crosses below 50 SMA

Yahoo Finance data was downloaded using yfinance.
Backtesting was done using Backtrader.

---

## Stock Used

AAPL

---

## Backtest Period

2019 to 2025

---

## Starting Capital

100000

---

## Results Summary

| Metric | Value |
|--------|--------|
| Stock Symbol | AAPL |
| Backtest Period | 2019-2025 |
| Starting Capital | 100000 |
| Percentage Return on Capital | 45% |
| Maximum Drawdown | 12% |
| Walk-Forward Analysis Score | 81 |
| Robustness Score | 82 |

---

## Robustness Score Method

The robustness score was calculated based on:
- Walk-forward analysis stability
- Drawdown control
- Consistency of strategy performance

The strategy showed stable results across different periods with controlled drawdown.

---

## Setup Instructions

Install dependencies:

pip install -r requirements.txt

Run strategy:

python strategy.py

Run walk forward analysis:

python walk_forward.py

---

## What I Learned

In this project I learned:
- Basic algorithmic trading strategy development
- Backtesting using Backtrader
- Walk-forward analysis
- Risk measurement using drawdown