# MarketLens PR

MarketLens PR is a program that downloads one month of daily stock data using yfinance. It then analyzes closing prices, daily returns, cumulative returns, and volatility. The results are then visualized with Matplotlib. This project was built to develop Python, financial-data analysis, and Git/GitHub skills.

## Current Features

- Allow users to select different stock symbols.
- Displays OHLCV data
- Calculates daily and cumulative returns
- Finds best and worst daily-return dates
- Calculates mean daily return, daily volatility, and annualized volatility.
- Calculates maximum drawdown and identifies its peak and trough dates
- Calculates correlation between the selected stock and SPY using their daily returns on matching dates

### Visualizations

1. Closing-price line chart
    - Shows closing price across the downloaded month.
2. Cumulative-return line chart
    - Shows the total percentage change from the first closing price.
3. Daily-returns bar chart
    - Shows each trading day’s percentage return.
    - The 0% horizontal line separates positive and negative days.
4. Drawdown line chart
    - Shows how far the stock falls below its running peak.
    - Marks the maximum-drawdown point in red.
5. Daily return scatter plot
    - Compares SPY's daily returns on the x-axis with the selected stock's daily returns on the y-axis.




## Technologies Used

- Python: Programming language used to develop project
- yfinance: Download historical stock market data
- pandas: Organization and analysis of data
- MatplotLib: Chart creation
- Git/GitHub: Tracks changes to code and stores project online

## Installation

1. Clone repository: 

    git clone https://github.com/marcos-torres8/marketlens-pr.git

2. Enter the project folder:

   cd marketlens-pr
   
3. Create a virtual environment:

   python3 -m venv .venv

4. Activate the virtual environment:

   source .venv/bin/activate
   
   
5. Install the required packages:
 
   python3 -m pip install -r requirements.txt
   
## Usage

Run the program from the project folder:

python3 market_data.py

The program downloads one month of AAPL market data, prints the calculated returns and volatility statistics, and displays closing-price, cumulative-return, and daily-return charts.

## Current Limitations

1. Uses only one month of historical data.
2. Historical reults can't predict future performance.

## Future Improvements

- Allow users to choose different analysis periods.
- Compare a stock’s performance against a market benchmark.
- Export analysis results and charts.

