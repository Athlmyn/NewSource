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
