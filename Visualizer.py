import matplotlib.pyplot as plt

class Visualizer:
    def plot(self, df, strategy_df):
        plt.figure(figsize=(12, 6))
        plt.plot(df['Close'], label='Close Price', alpha=0.5)
        
        if 'Short_MA' in strategy_df.columns and 'Long_MA' in strategy_df.columns:
            plt.plot(strategy_df['Short_MA'], label='Short MA', alpha=0.8)
            plt.plot(strategy_df['Long_MA'], label='Long MA', alpha=0.8)

        if 'RSI' in strategy_df.columns:
            plt.plot(strategy_df['RSI'], label='RSI', alpha=0.8)
            plt.axhline(70, color='red', linestyle='dashed', alpha=0.6)
            plt.axhline(30, color='green', linestyle='dashed', alpha=0.6)

        buy_signals = strategy_df[strategy_df['Signal'] == 1.0]
        sell_signals = strategy_df[strategy_df['Signal'] == -1.0]

        plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='g', label='Buy Signal', alpha=1)
        plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='r', label='Sell Signal', alpha=1)

        plt.title('Stock Price and Buy/Sell Signals')
        plt.legend()
        plt.show()

    def plot_earnings(self, prices, strategy_df, analysis):
        cumulative_returns = (prices / prices.iloc[0] - 1) * 100  # in percentage
        buy_signals = strategy_df[strategy_df['Signal'] == 1.0]
        sell_signals = strategy_df[strategy_df['Signal'] == -1.0]

        plt.figure(figsize=(12, 6))
        plt.plot(cumulative_returns, label='Stock Returns', alpha=0.5)
        plt.scatter(buy_signals.index, cumulative_returns.loc[buy_signals.index], marker='^', color='g', label='Buy Signal', alpha=1)
        plt.scatter(sell_signals.index, cumulative_returns.loc[sell_signals.index], marker='v', color='r', label='Sell Signal', alpha=1)
        plt.title('Stock Cumulative Returns and Buy/Sell Signals')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns (%)')
        plt.legend()
        plt.show()

        # Print the analysis results
        for key, value in analysis.items():
            print(f"{key}: {value:.2f}")