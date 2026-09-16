import yfinance as yf
import matplotlib.pyplot as plt
symbol = "AAPL"  # Example stock symbol

# Download one month of daily stock data for the specified symbol using 
# yfinance
data = yf.download(symbol, period="1mo", interval="1d") 

# Close prices are extracted from data and used by matplotlib
close_prices = data["Close"][symbol]

# Calculate daily returns as percentage
daily_returns = close_prices.pct_change() * 100  
print("Daily returns (%):")
print(daily_returns)

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
plt.title(f"{symbol} Closing Price - Last Month")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
# Creates grid in the chart for better visualization of points
plt.grid(True)
plt.show()

# Display daily returns as a bar chart
plt.figure()
daily_returns.plot(kind="bar")
plt.axhline(y=0, color="black", linewidth=1)
plt.title(f"{symbol} Daily Returns - Last Month")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
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
