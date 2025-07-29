# Simple Quant Calculator

A modular Python tool for basic quantitative finance calculations. Compute moving averages, volatility, and Sharpe ratios on price/return data. Ideal for aspiring quant devs or startups prototyping trading analytics—reusable functions for easy integration.

## Why This Tool?
- Applies to real-world quant tasks: Risk assessment in trading firms (e.g., Jane Street-inspired metrics).
- Reusable: Functions like `compute_sharpe()` can plug into bigger apps (e.g., backtesters or AI models).
- Beginner-friendly: Focuses on core concepts with error handling and examples.
- Efficient: Quick calcs without heavy libs, scalable to production.

## Features
- **Moving Average**: Smooths price data over a window (e.g., 5-day avg).
- **Volatility**: Calculates standard deviation of returns.
- **Sharpe Ratio**: Risk-adjusted return metric (returns minus risk-free rate over volatility).
- **Modular**: Standalone functions with docstrings—import and use anywhere.
- **Error Handling**: Validates inputs (e.g., non-empty lists, numeric data).

## Installation
1. Clone the repo: `git clone https://github.com/ronniefr/quant-calculator.git`
2. Install dependencies: `pip install numpy` (optional for advanced math)
3. Run: `python quant_calculator.py` for examples.

## Usage
Import and call functions:
from quant_calculator import simple_moving_average, calculate_volatility, sharpe_ratio

prices =
sma = simple_moving_average(prices, window=2) # Output: [101.0, 101.5, 103.0]
returns = [0.02, -0.01, 0.04]
vol = calculate_volatility(returns) # Std dev
sharpe = sharpe_ratio(returns, risk_free_rate=0.01) # Risk-adjusted metric

See script for full examples.

## Security Notes
- Input validation prevents crashes from bad data.
- No external data handling—safe for local use.

## Contributing
Add new metrics via PR! Inspired by TA-Lib—let's build it out.

## License
MIT—open for all.
