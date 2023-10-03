from Strategies.Backtest.Portfolio import Portfolio


class Backtester:

    def __init__(self, initial_balance=10000, transaction_fee=5.0):
        self.initial_balance = initial_balance
        self.transaction_fee = transaction_fee

    def simulate(self, price_data, signal_data):
        portfolio = Portfolio(self.initial_balance)
        for ticker in price_data.columns:
            portfolio.add_asset(ticker)

        trade_log = []

        for date, prices in price_data.iterrows():
            for ticker in prices.index:
                price = prices[ticker]
                signal = signal_data[ticker].loc[date]
                if signal == 1:  # Buy signal
                    quantity = (portfolio.balance / len(price_data.columns)) // price
                    portfolio.buy(ticker, price, quantity)
                    trade_log.append((date, ticker, 'Buy', price, portfolio.total_value(price_data.loc[date])))
                elif signal == -1:  # Sell signal
                    quantity = portfolio.assets[ticker].quantity
                    portfolio.sell(ticker, price, quantity)
                    trade_log.append((date, ticker, 'Sell', price, portfolio.total_value(price_data.loc[date])))

        return portfolio, trade_log, self.initial_balance

    def analyze(self, price_data, signal_data):
        portfolio, trade_log, initial_balance = self.simulate(price_data, signal_data)

        ending_balance = portfolio.total_value(price_data.iloc[-1])
        difference = ending_balance - initial_balance
        
        analysis = {
            "Initial Balance": initial_balance,
            "Difference (Profit/Loss)": difference,
            "Ending Balance": ending_balance,
            "Trade Log": trade_log
        }
        
        return analysis
