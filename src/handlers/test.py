from fastapi import APIRouter

prices_rout = APIRouter()

@prices_rout.get('/get_prices')
def get_prices():
    return