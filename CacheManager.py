import sqlite3
from datetime import datetime

import pandas as pd

class CacheManager:

    def __init__(self, db_name="stock_data_cache.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
        self.create_trips_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_data (
            ticker TEXT,
            date DATE,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            adj_close FLOAT,
            volume INTEGER,
            PRIMARY KEY (ticker, date)
        )
        ''')
        self.conn.commit()

    def insert_data(self, ticker, data):
        cursor = self.conn.cursor()
        for index, row in data.iterrows():
            date_str = index.strftime('%Y-%m-%d')
            cursor.execute('''
            INSERT OR REPLACE INTO stock_data
            (ticker, date, open, high, low, close, adj_close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (ticker, date_str, row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']))
        self.conn.commit()

    def fetch_data(self, ticker, start_date, end_date):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT date, open, high, low, close, adj_close, volume
        FROM stock_data
        WHERE ticker = ? AND date BETWEEN ? AND ?
        ORDER BY date
        ''', (ticker, start_date, end_date))
        rows = cursor.fetchall()

        if rows:
            df = pd.DataFrame(rows, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            return df
        return None

    def create_trips_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS trading_signals (
            ticker TEXT,
            date DATE,
            strategy TEXT,
            signal INT,
            PRIMARY KEY (ticker, date, strategy)
        )
        ''')
        self.conn.commit()

    def insert_trips(self, ticker, strategy_name, strategy_df):
        cursor = self.conn.cursor()
        for index, row in strategy_df.iterrows():
            date_str = index.strftime('%Y-%m-%d')
            if row['Signal'] != 0:  # Only insert if there's a buy or sell signal
                cursor.execute('''
                INSERT OR REPLACE INTO trading_signals
                (ticker, date, strategy, signal)
                VALUES (?, ?, ?, ?)
                ''', (ticker, date_str, strategy_name, int(row['Signal'])))
        self.conn.commit()

    def fetch_trips(self, ticker, strategy_name):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT date, signal
        FROM trading_signals
        WHERE ticker = ? AND strategy = ?
        ORDER BY date
        ''', (ticker, strategy_name))
        rows = cursor.fetchall()

        if rows:
            df = pd.DataFrame(rows, columns=['Date', 'Signal'])
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            return df
        return None