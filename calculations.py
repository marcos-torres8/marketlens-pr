#Calculate returns 

def calculate_returns(close_prices):
    daily_returns = close_prices.pct_change() * 100
    first_closing_price = close_prices.iloc[0]
    cumulative_returns = (close_prices / first_closing_price - 1) * 100

    return daily_returns, cumulative_returns