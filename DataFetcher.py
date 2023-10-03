import yfinance as yf

from CacheManager import CacheManager

class DataFetcher:

    def __init__(self):
        self.cache = CacheManager()

    def fetch(self, ticker, start_date, end_date):
        # Check cache first
        data = self.cache.fetch_data(ticker, start_date, end_date)
        
        # If data is not in cache, fetch from yfinance
        if data is None:
            data = yf.download(ticker, start=start_date, end=end_date)
            self.cache.insert_data(ticker, data)
        return data
