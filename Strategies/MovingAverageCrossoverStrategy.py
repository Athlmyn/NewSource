import talib
from .Strategy import Strategy

#Explai
class MovingAverageCrossoverStrategy(Strategy):
    def __init__(self, short_window=40, long_window=100):
        self.short_window = short_window
        self.long_window = long_window

    def apply(self, df):
        signals = df.copy()
        signals['Short_MA'] = talib.SMA(df['Close'], timeperiod=self.short_window)
        signals['Long_MA'] = talib.SMA(df['Close'], timeperiod=self.long_window)
        signals['Signal'] = 0.0
        signals.loc[signals['Short_MA'] > signals['Long_MA'], 'Signal'] = 1.0
        signals.loc[signals['Short_MA'] <= signals['Long_MA'], 'Signal'] = -1.0
        return signals
    
    def get_parameters(self):
        return {
            "short_window": ("Enter the short window size [default: 40]: ", 40),
            "long_window": ("Enter the long window size [default: 100]: ", 100)
        }

    def set_parameters(self, **params):
        self.short_window = params.get("short_window", self.short_window)
        self.long_window = params.get("long_window", self.long_window)