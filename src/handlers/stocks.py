from fastapi import APIRouter, HTTPException
from src.service.stock_details import Fundamentus, YahooFinance


from src.models.stocks import StockModel, DividenByYear
from typing import List


stocks_rout = APIRouter()

@stocks_rout.get('/fundamentus/price/{ticker}', tags=["Fundamentus"])
def get_price(ticker) -> StockModel:
    stock = Fundamentus(ticker)
    price = stock.get_price()
    if price is None:
        raise HTTPException(status_code=404, detail=f"Preço não encontrados para o ticker {ticker}. Verifique se o ticker está correto.")
    return price


@stocks_rout.get('/fundamentus/dividends/{ticker}', tags=["Fundamentus"])
def get_dividends(ticker) -> List[DividenByYear]:
    stock = Fundamentus(ticker)
    dividends = stock.get_dividends_by_year()
    if dividends is None:
        raise HTTPException(status_code=404, detail=f"Dividendos não encontrados para o ticker '{ticker}'. Verifique se o ticker está correto.")
    return dividends


@stocks_rout.get('/yahoo/history_prices/{ticker}', tags=["Yahoo Financial"])
def get_prices(ticker) -> List[StockModel]:
    stock = YahooFinance(ticker)
    prices = stock.get_data_ticker()
    if prices is None:
        raise HTTPException(status_code=404, detail=f"Preço não encontrados para o ticker {ticker}. Verifique se o ticker está correto.")
    return prices
