import yfinance as yf
import pandas as pd
from src.models.stocks import StockModel
from typing import List
from src.talkers import Stock


class YahooFinance(Stock):
    def __init__(self, ticker: str) -> None:
        super().__init__(ticker)

    def get_data_ticker(self) -> List[StockModel]:
        ticker = f'{self.ticker.upper().split(".")[0]}.SA'
        data = yf.Ticker(ticker)
        data.info

        history = data.history(interval="3mo", start="2000-01-01")
        history.reset_index(inplace=True)

        history = history.rename(columns={'Open': 'price', 'Date':'date'})
        columns_to_include = ['price', 'date']

        history['date'] = history['date'].dt.strftime('%Y-%m-%d')
        history['price'] = history['price'].astype(float)
        history_list = history[columns_to_include].to_dict(orient='records')

        return [StockModel(**stock) for stock in history_list]


