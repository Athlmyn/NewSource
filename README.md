# Stock Analysis and Backtesting Tool

## Features

- **Variety of Trading Strategies:** Supports a range of trading strategies including Moving Average Crossover, RSI Overbought/Oversold, and allows for the easy integration of custom strategies.
- **Interactive Visualization:** Offers interactive and intuitive visualizations of stock data and trading signals, aiding in better analysis and decision-making.
- **Backtesting Engine:** Features a powerful backtesting engine that simulates trading based on strategy signals, providing insights into potential performance and profitability.
- **Real-Time Data Analysis:** Integrates real-time data, enabling users to analyze and test trading strategies with the most current market information.
- **Portfolio Management:** Allows the management of multiple assets, capital allocation, and portfolio rebalancing, offering a holistic view of portfolio performance over time.


## Usage

### Running the Tool

1. Execute the main script by running the following command in your terminal or command prompt:
    ```sh
    python main.py
    ```

2. You will be prompted to enter the stock tickers of interest, separated by commas:
    ```sh
    Enter stock tickers separated by comma (e.g., AAPL,MSFT) [default: AAPL]:
    ```

3. Specify the date range for fetching historical data:
    ```sh
    Enter the start date (YYYY-MM-DD) [default: 2022-01-01]:
    Enter the end date (YYYY-MM-DD) [default: 2023-01-01]:
    ```

4. Choose a trading strategy from the available options and configure its parameters as prompted.

5. The tool will fetch the data, apply the selected strategy, and visualize the signals on a plot. It will then backtest the strategy and provide performance metrics including profit/loss, and other analytics.

6. You have the option to test another strategy or ticker or exit the tool.

### Example Analysis

After following the interactive prompts, you will receive visualizations of the applied trading strategy, showcasing buy/sell/hold signals on the stock data. The backtesting engine will provide a detailed analysis of the strategy's performance, including the initial balance, total profit/loss, and ending balance, offering insights into the strategy's effectiveness and potential profitability.

For advanced users, the tool's modular design allows for the easy integration of custom trading strategies and additional data sources, enabling comprehensive and tailored stock market analysis.

Example of the tool's default output:
[Images/default_settings.png]