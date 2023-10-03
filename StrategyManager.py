
from CacheManager import CacheManager


class StrategyManager:
    
    def __init__(self):
        self.cache = CacheManager()

    def apply_and_store(self, ticker, data, strategy):
        strategy_df = strategy.apply(data)
        strategy_name = strategy.__class__.__name__  # Get the name of the strategy class
        self.cache.insert_trips(ticker, strategy_name, strategy_df)
        return strategy_df