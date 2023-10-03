import pandas as pd
from Strategies.Backtest.Backtester import Backtester
from DataFetcher import DataFetcher
from Strategies.MovingAverageCrossoverStrategy import MovingAverageCrossoverStrategy
from Strategies.RSIOverboughtOversoldStrategy import RSIOverboughtOversoldStrategy
from StrategyManager import StrategyManager
from Visualizer import Visualizer

def get_tickers():
    tickers = input("Enter stock tickers separated by comma (e.g., AAPL,MSFT) [default: AAPL]: ") or "AAPL"
    return [ticker.strip().upper() for ticker in tickers.split(",")]

def get_date_range():
    start_date = input("Enter the start date (YYYY-MM-DD) [default: 2022-01-01]: ") or "2022-01-01"
    end_date = input("Enter the end date (YYYY-MM-DD) [default: 2023-01-01]: ") or "2023-01-01"
    return start_date, end_date

def choose_strategy(strategies):
    print("\nAvailable Strategies:")
    for key, strategy in strategies.items():
        print(f"{key}: {strategy.__class__.__name__}")
    strategy_choice = input("Choose a strategy: ") or "1"
    strategy = strategies.get(strategy_choice)
    if not strategy:
        return None

    # Get strategy parameters
    params = {}
    for param, (prompt, default) in strategy.get_parameters().items():
        value = input(prompt) or default
        params[param] = int(value)
    strategy.set_parameters(**params)
    return strategy

def fetch_data_for_tickers(tickers, fetcher, start_date, end_date):
    data = {}
    for ticker in tickers:
        data[ticker] = fetcher.fetch(ticker, start_date, end_date)
    return data

def display_analysis_results(analysis_results):
    print("\nPortfolio Analysis:")
    print(f"Initial Balance: ${analysis_results['Initial Balance']:.2f}")
    print(f"Profit/Loss: ${analysis_results['Difference (Profit/Loss)']:.2f}")
    print(f"Ending Balance: ${analysis_results['Ending Balance']:.2f}")
    print("\nTrade Log:")
    for log in analysis_results['Trade Log']:
        print(log)

def main():
    # Initialization
    fetcher = DataFetcher()
    strategy_manager = StrategyManager()
    visualizer = Visualizer()
    backtester = Backtester(transaction_fee=1.0)

    strategies = {
        "1": MovingAverageCrossoverStrategy(),
        "2": RSIOverboughtOversoldStrategy()
    }

    while True:
        tickers = get_tickers()
        start_date, end_date = get_date_range()
        strategy = choose_strategy(strategies)
        if not strategy:
            print("Invalid strategy choice!")
            continue
        data = fetch_data_for_tickers(tickers, fetcher, start_date, end_date)
        
        # Apply strategy to each ticker
        signal_data = pd.DataFrame(index=data[tickers[0]].index)
        for ticker in tickers:
            strategy_df = strategy_manager.apply_and_store(ticker, data[ticker], strategy)
            signal_data[ticker] = strategy_df['Signal']
            visualizer.plot(data[ticker], strategy_df)  # visualize each ticker's strategy result

        # Backtest on the portfolio
        price_data = pd.concat({ticker: df['Close'] for ticker, df in data.items()}, axis=1)
        analysis_results = backtester.analyze(price_data, signal_data)

        # Display results
        display_analysis_results(analysis_results)

        cont = input("Would you like to test another strategy or ticker? (yes/no) [default: no]: ").lower() or "no"
        if cont != "yes":
            break

if __name__ == "__main__":
    main()
