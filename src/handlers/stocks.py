from fastapi import APIRouter, HTTPException
from src.service.stock_details import Stock

from src.models.stocks import StockModel, DividenByYear
from typing import List


stocks_rout = APIRouter()

@stocks_rout.get('/fundamentus/price/{ticker}', tags=["Fundamentus"])
def get_prices(ticker) -> StockModel:
    stock = Stock(ticker)
    price = stock.get_price()
    if price is None:
        raise HTTPException(status_code=404, detail=f"Preço não encontrados para o ticker {ticker}. Verifique se o ticker está correto.")
    return price


@stocks_rout.get('/fundamentus/dividends/{ticker}', tags=["Fundamentus"])
def get_dividends(ticker) -> List[DividenByYear]:
    stock = Stock(ticker)
    dividends = stock.get_dividends_by_year()
    if dividends is None:
        raise HTTPException(status_code=404, detail=f"Dividendos não encontrados para o ticker '{ticker}'. Verifique se o ticker está correto.")
    return dividends
