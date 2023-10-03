
import talib
from .Strategy import Strategy


class RSIOverboughtOversoldStrategy(Strategy):
    """
    A strategy that generates buy and sell signals based on the RSI indicator.
    
    Parameters:
    overbought (float): The overbought level for the RSI indicator. Default is 70.
    oversold (float): The oversold level for the RSI indicator. Default is 30.
    """
    def __init__(self, overbought=70, oversold=30):
        self.overbought = overbought
        self.oversold = oversold

    
    def apply(self, df):
        """
        Applies the RSIOverboughtOversoldStrategy to the given DataFrame.
        
        Parameters:
        df (pandas.DataFrame): The DataFrame to apply the strategy to.
        
        Returns:
        pandas.DataFrame: A DataFrame with buy and sell signals based on the RSI indicator.
        """
        signals = df.copy()
        signals['RSI'] = talib.RSI(df['Close'])
        signals['Signal'] = 0.0
        signals.loc[signals['RSI'] > self.overbought, 'Signal'] = -1.0  # Overbought hence sell signal
        signals.loc[signals['RSI'] < self.oversold, 'Signal'] = 1.0  # Oversold hence buy signal
        return signals
    
    def get_parameters(self):
        return {
            "overbought": ("Enter the overbought threshold [default: 70]: ", 70),
            "oversold": ("Enter the oversold threshold [default: 30]: ", 30)
        }

    def set_parameters(self, **params):
        self.overbought = params.get("overbought", self.overbought)
        self.oversold = params.get("oversold", self.oversold)