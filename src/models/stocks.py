from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class DividenByYear(BaseModel):
    year: int
    value: float


class StockModel(BaseModel):
    name: Optional[str] = ''
    ticker: Optional[str] = ''
    date: Optional[str] = datetime.now().strftime('%Y-%m-%d')
    price: float
    dividends: Optional[List[DividenByYear]] = []
