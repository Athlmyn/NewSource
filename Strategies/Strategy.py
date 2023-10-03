from abc import ABC, abstractmethod
import talib

class Strategy(ABC):
    @abstractmethod
    def apply(self, df):
        pass

    @abstractmethod
    def get_parameters(self):
        pass

    @abstractmethod
    def set_parameters(self, **params):
        pass