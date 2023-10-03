class Asset:
    def __init__(self, ticker, quantity=0):
        self.ticker = ticker
        self.quantity = quantity

    def value(self, current_price):
        return self.quantity * current_price

    def __repr__(self):
        return f"{self.ticker}: {self.quantity}"