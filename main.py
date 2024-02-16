from fastapi import FastAPI
import uvicorn
from decouple import config

from src.handlers.stocks import stocks_rout


app = FastAPI(title='Wallet Bazin')
app.include_router(stocks_rout)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=config('HOST'),
        port=int(config('PORT')),
        workers=int(config('WORKERS'))
    )
