import pandas as pd
from calculations import calculate_returns
from math import isclose

# Test daily prices and cumulative returns
test_prices = pd.Series([100, 100, 100])
test_daily, test_cumulative = calculate_returns(test_prices)

assert test_cumulative.iloc[-1] == 0

test_prices = pd.Series([100,110,99])
test_daily, test_cumulative = calculate_returns(test_prices)
assert isclose(test_cumulative.iloc[-1], -1.0)

# assert isclose(test_cumulative.iloc[-1], -1.0, abs_tol=1e-9)

print("Test daily returns: ", test_daily)
print("Test cumulative Returns: ", test_cumulative)

