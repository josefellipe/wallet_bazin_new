from src.talkers.fundamentus import Fundamentus

stocks = Fundamentus().get_price('PETR14')

print(stocks)