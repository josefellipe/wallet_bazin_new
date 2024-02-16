from pydantic import BaseModel
from typing import List, Optional


class DividenByYear(BaseModel):
    year: int
    value: float


class StockModel(BaseModel):
    name: str
    ticker: str
    price: float
    dividends: Optional[List[DividenByYear]] = []
