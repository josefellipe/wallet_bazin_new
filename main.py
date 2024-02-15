from fastapi import FastAPI
import uvicorn

from src.handlers.test import test_rout

app = FastAPI()
app.include_router(test_rout)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8000
    )