import pandas as pd
from calculations import calculate_returns

# Test daily prices and cumulative returns
test_prices = pd.Series([100, 100, 100])
test_daily , test_cumulative = calculate_returns(test_prices)

print("Test daily returns: ", test_daily)
print("Test cumulative Returns: ", test_cumulative)

assert test_cumulative.iloc[-1] == 0