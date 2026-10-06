# MarketLens PR

MarketLens PR is a program that downloads daily stock data (1 month, 3 months, or 1 year) using yfinance. It then analyzes closing prices, daily returns, cumulative returns, volatility, drawdown, and correlation with SPY. The results are then visualized with Matplotlib. This project was built to develop Python, financial-data analysis, and Git/GitHub skills.

## Current Features

- Allow users to select different stock symbols.
- User can select periods 1mo, 3mo and 1y
- Retry prompts for invalid periods or empty stock downloads
- Displays OHLCV data
- Calculates daily and cumulative returns
- Finds best and worst daily-return dates
- Calculates mean daily return, daily volatility, and annualized volatility.
- Calculates maximum drawdown and identifies its peak and trough dates
- Calculates correlation between the selected stock and SPY using their daily returns on matching dates

### Visualizations

1. Closing-price line chart
    - Shows closing price across the selected period.
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

The program asks for a ticker and period of time of data to be downloaded, prints the calculated returns, volatility, drawdown, and correlation statistics, and displays the closing-price, cumulative-return, daily-return, drawdown, and SPY-comparison charts.

## Project Structure

- `market_data.py`: Main program. Handles user input, downloads data, prints statistics, and displays charts.
- `calculations.py`: Contains `calculate_returns`, which computes daily and cumulative returns.
- `test_calculations.py`: Tests for `calculate_returns` using sample prices (no internet connection needed).

## Running Tests

With the virtual environment activated, run from the project folder:

python3 test_calculations.py

If no `AssertionError` appears, all tests passed.

## Current Limitations

1. Historical results can't predict future performance.

## Future Improvements

- Export analysis results and charts.

