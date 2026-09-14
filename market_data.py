import yfinance as yf
import matplotlib.pyplot as plt
symbol = "AAPL"  # Example stock symbol

# Download one month of daily stock data for the specified symbol using 
# yfinance
data = yf.download(symbol, period="1mo", interval="1d") 

# Close prices are extracted from data and used by matplotlib
close_prices = data["Close"][symbol]
close_prices.plot()

# Chart Modifications: Add title, labels, and grid to the plot
plt.title(f"{symbol} Closing Price - Last Month")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
# Creates grid in the chart for better visualization of points
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
