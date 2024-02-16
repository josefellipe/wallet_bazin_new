from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import fundamentus
from src.models.stocks import StockModel, DividenByYear
from typing import List

class Fundamentus:
    def __init__(self, ticker:str) -> None:
        self.ticker = ticker.upper()
        self.all_tickers = fundamentus.list_papel_all()

    def get_price(self) -> StockModel|None:
        if self.ticker not in self.all_tickers:
            return 
        
        stock_detail = fundamentus.get_detalhes_papel(f'{self.ticker}')
        name = stock_detail['Empresa'][0]
        price = stock_detail['Cotacao']
        stock = StockModel(ticker=self.ticker, price=price, name=name)
        del stock.dividends
        return stock

    def get_dividends_by_year(self) -> List[DividenByYear]|None:
        if self.ticker not in self.all_tickers:
            return 

        req = Request(
            url=f'https://www.fundamentus.com.br/proventos.php?papel={self.ticker}&tipo=2',
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html5lib')
        table = soup.find("table", id="resultado-anual")

        # Join all lists in just one
        lines = sum([item.text.split('\n') for item in table], [])

        dividends = []
        for i in range(len(lines)//2):
            if lines[2*i].isnumeric():
                dividends.append(
                    DividenByYear(
                        year=int(lines[2*i]),
                        value=float(lines[2*i+1].replace(',', '.'))
                    )
                )

        return dividends
    