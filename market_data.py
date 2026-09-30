import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


benchmark_symbol = "SPY"

# User inputs what stock ticker to analyze. If ticker is invalid, user is prompted to re-enter a ticker.
# User also chooses what period of time of data they want to download.

def get_stock_data():
    while True:
        symbol = input("Enter a stock ticker: ").strip().upper()
        period = input("Choose a period (1mo, 3mo, 1y): ").strip().lower() 

        if period not in ["1mo", "3mo", "1y"]:
            print("Invalid period. Choose 1mo, 3mo, or 1y.")
            continue

        data = yf.download(symbol, period=period, interval="1d") 

        # Verify if stock ticker is valid
        if data.empty:
            print(f"No data found for {symbol}. Verify the ticker or your connection.")
        else:
            return symbol, period, data

def calculate_returns(close_prices):
    daily_returns = close_prices.pct_change() * 100
    first_closing_price = close_prices.iloc[0]
    cumulative_returns = (close_prices / first_closing_price - 1) * 100

    return daily_returns, cumulative_returns

symbol, period, data = get_stock_data()
benchmark_data = yf.download(benchmark_symbol, period=period, interval="1d")

# Close prices are extracted from data and used by matplotlib
close_prices = data["Close"][symbol]
benchmark_close_prices = benchmark_data["Close"][benchmark_symbol]

# Calculate daily and cumulative returns
daily_returns, cumulative_returns = calculate_returns(close_prices)
# Running peak
running_peak = close_prices.cummax()
print("Running peak($): ")
print(running_peak.round(2))
      
# Drawdown
drawdown = (close_prices - running_peak)/running_peak * 100
print("Drawdown (%):")
print(drawdown.round(2))

maximum_drawdown = drawdown.min()
maximum_drawdown_date = drawdown.idxmin()
print("Maximum drawdown date: ", maximum_drawdown_date)
print("Maximum drawdown: ", round(maximum_drawdown, 2), "%")

# Peak and trough dates

# Series containing prices only through the maximum-drawdown date
prices_before_trough = close_prices.loc[:maximum_drawdown_date]
trough_date= drawdown.idxmin()
peak_date = close_prices.loc[:trough_date].idxmax()
print("Peak date: ", peak_date)
print("Trough date", trough_date)
# Get cumulative return
first_closing_price = close_prices.iloc[0]
print("First closing price: $", round(first_closing_price, 2))
print("Cumulative returns (%):")
print(cumulative_returns)
final_cumulative_return = cumulative_returns.iloc[-1]
print("Final cumulative return: ", round(final_cumulative_return, 2), "%")
print("Daily returns (%):")
print(daily_returns)

benchmark_daily_returns = benchmark_close_prices.pct_change() * 100

aligned_returns = pd.DataFrame({"Stock": daily_returns,
"SPY": benchmark_daily_returns})
aligned_returns = aligned_returns.dropna()
print(aligned_returns)

correlation = aligned_returns["Stock"].corr(aligned_returns["SPY"])
print("Correlation: ", round(correlation, 2))
#Calculate MDR
mean_daily_return = daily_returns.mean()
print("Mean daily return: ", round(mean_daily_return, 2), "%")

#Calculate Daily Volatility
daily_volatility = daily_returns.std()
print("Daily volatility: ", round(daily_volatility, 2), "%")

#Calculate Annualized Volatility
annualized_volatility = daily_volatility * (252 ** 0.5)
print("Annualized volatility: ", round(annualized_volatility, 2), "%")
# Print best and worst days of daily returns
best_day = daily_returns.idxmax()
best_return = daily_returns.max()
print("Best day: ", best_day)
print("Best return: ", round(best_return, 2), "%")

worst_day = daily_returns.idxmin()
worst_return = daily_returns.min()
print("Worst day :", worst_day)
print("Worst return: ", round(worst_return, 2), "%")

close_prices.plot()

# Chart Modifications: Add title, labels, and grid to the plot
plt.title(f"{symbol} Closing Price - {period}")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
# Creates grid in the chart for better visualization of points
plt.grid(True)

#First show
plt.show() 

#Creates chart area for cumulative returns
plt.figure()
cumulative_returns.plot()
plt.title(f"{symbol} Cumulative Returns - {period}")
plt.xlabel("Trading Date")
plt.ylabel("Cumulative Return (%)")
plt.grid(True)
plt.axhline(y=0, color="black", linewidth=1)
plt.show()
# Display daily returns as a bar chart
plt.figure()
plt.bar(daily_returns.index, daily_returns.values)
plt.gcf().autofmt_xdate()
plt.axhline(y=0, color="black", linewidth=1)
plt.title(f"{symbol} Daily Returns - {period}")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.show()

# Display month's drawdown as a line chart
plt.figure()
drawdown.plot(kind="line")
plt.scatter(trough_date, maximum_drawdown, color="red", label="Maximum Drawdown")
plt.title(f"{symbol} Drawdown - {period}")
plt.axhline(y=0, color="black", linewidth=1)
plt.xlabel("Date")
plt.ylabel("Drawdown (%)")
plt.grid(True)
plt.legend()
plt.show()

# Display months aligned returns
plt.figure()
plt.scatter(aligned_returns["SPY"], aligned_returns["Stock"])
plt.xlabel("SPY Daily Return (%)")
plt.ylabel(f"{symbol} Daily Return (%)")
plt.title(f"{symbol} vs SPY - {period}")
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)
plt.grid(True)
plt.show()

print(data)

# Outputs the shape of "Table"
print("Data shape:", data.shape)
print("Columns:", data.columns)

print("Data types:")
# Returns data types of each of the columns
print(data.dtypes)

# Checks every cell and returns the number of missing values in each column
print("Missing values in data: ")
print(data.isnull().sum())

