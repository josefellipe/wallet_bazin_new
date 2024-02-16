import yfinance as yf


class YahooFinance:
    def __init__(self, ticker:str) -> None:
        self.ticker = ticker.upper()

    def get_data_ticker(ticker: str):
        data = yf.Ticker(ticker)
        data.info

        price = data.history(interval="3mo", start="2000-01-01")

        return price
# get_data_ticker('PETR4.SA')
print(YahooFinance('PETR4.SA'))