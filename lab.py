from src.talkers.fundamentus import Fundamentus
from src.talkers.yahoo_finance import YahooFinance

stocks = YahooFinance('PETR4').get_data_ticker()

print(stocks)