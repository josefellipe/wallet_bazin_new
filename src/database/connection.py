from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config
from urllib.parse import quote

from .tables import Base
from .tables import Stock, Price, Investor, Wallet

class DatabaseManager:
    def __init__(self):
        self.engine = self.__create_engine_instance()
        self.session = None
    
    def __create_engine_instance(self):
        try:
            db_config = {
                'database': config('DB_NAME'),
                'user': config('DB_USER'),
                'password': config('DB_PASSWORD'),
                'host': config('DB_HOST'),
                'port': config('DB_PORT')      
            }
            encoded_password = quote(db_config['password'])
            db_url = config('DB_PATH', default=f'sqlite:///{db_config["database"]}.db')
            #db_url = f"postgresql://{db_config['user']}:{encoded_password}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
            engine = create_engine(db_url)
            return engine
        except Exception as e:
            print(f"Error creating database engine: {e}")
            return None

    def create_tables(self):
        try:
            Base.metadata.create_all(self.engine)
            print("Tables created successfully.")
        except Exception as e:
            print(f"Error creating tables: {e}")

    def open_session(self):
        try:
            if self.session is None:
                Session = sessionmaker(bind=self.engine)
                self.session = Session()
            return self.session
        except Exception as e:
            print(f"Error opening session: {e}")
            return None

    def close_session(self):
        try:
            if self.session is not None:
                self.session.close()
                self.session = None
        except Exception as e:
            print(f"Error closing session: {e}")