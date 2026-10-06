# MarketLens PR

## Purpose

A Python command-line program that downloads daily stock data (1mo, 3mo, or 1y) with yfinance, calculates returns, volatility, drawdown, and correlation with SPY, and shows the results as Matplotlib charts. It is a learning project for Python, financial-data analysis, and Git/GitHub.

## Files

- `market_data.py`: main script. Handles prompts, downloads, statistics, and charts. Runs on import, so don't import it from other modules or tests.
- `calculations.py`: pure calculation functions (currently `calculate_returns`). New logic that can be tested without the network belongs here.
- `test_calculations.py`: plain-script tests with top-level `assert` statements (not pytest functions). Uses made-up prices, so no network is needed.
- `requirements.txt`: dependencies (`yfinance`, `matplotlib`).
- `README.md`: user-facing docs. Update it when features or usage change.

## Commands

Use the project virtual environment (`.venv`):

- Run the program: `.venv/bin/python market_data.py` (needs internet; opens chart windows)
- Run the tests: `.venv/bin/python test_calculations.py` (passing means exit code 0 and no `AssertionError`)

## Rules

- Keep changes focused. Only touch what the task needs.
- Explain your plan before editing files.
- Verify changes. Run the tests and check `git diff` before reporting a change as done.
- Only commit or push when I explicitly ask. Never do either on your own.

## Learning mode

- When I am learning, guide me with explanations and hints.
- Do not write or edit code unless I explicitly ask you to.
