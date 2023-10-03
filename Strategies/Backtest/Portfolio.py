from Strategies.Backtest.Asset import Asset


class Portfolio:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.assets = {}

    def add_asset(self, ticker, quantity=0):
        self.assets[ticker] = Asset(ticker, quantity)

    def buy(self, ticker, price, quantity):
        self.assets[ticker].quantity += quantity
        self.balance -= price * quantity

    def sell(self, ticker, price, quantity):
        self.assets[ticker].quantity -= quantity
        self.balance += price * quantity

    def total_value(self, price_map):
        total = self.balance
        for ticker, asset in self.assets.items():
            total += asset.value(price_map[ticker])
        return total

    def __repr__(self):
        return f"Balance: ${self.balance:.2f}, Assets: {self.assets}"