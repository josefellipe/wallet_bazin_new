from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import declarative_base, relationship

from datetime import datetime

Base = declarative_base()


class Stock(Base):
    __tablename__ = 'stocks'

    id          = Column(Integer, primary_key=True, autoincrement=True)
    ticket      = Column(String(8), nullable=False)
    name        = Column(String(200), nullable=True)

    is_bazin    = Column(Boolean, default=False)

    created_at  = Column(DateTime, default=datetime.now())
    updated_at  = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    prices      = relationship('Price', back_populates='stocks')


class Price(Base):
    __tablename__ = 'prices'

    id          = Column(Integer, primary_key=True, autoincrement=True)

    date        = Column(String(10), default='AAAA-MM-DD', nullable=False)
    value_day   = Column(Float(2), nullable=True)

    fk_stock    = Column(Integer, ForeignKey('stocks.id'), nullable=False)

    created_at  = Column(DateTime, default=datetime.now())
    updated_at  = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    stock       = relationship('Stock', back_populates='prices')


class Wallet(Base):
    __tablename__ = 'wallets'

    id          = Column(Integer, primary_key=True, autoincrement=True)

    fk_investor = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    fk_stock    = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    quantity    = Column(Integer, nullable=False)
    price       = Column(Float(2), nullable=False)

    created_at  = Column(DateTime, default=datetime.now())
    updated_at  = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    stock       = relationship('Stock', back_populates='wallets')
    investor    = relationship('Investor', back_populates='wallets')


class Investor(Base):
    __tablename__ = 'investors'

    id              = Column(Integer, primary_key=True, autoincrement=True)

    name            = Column(String(100), nullable=False)
    email           = Column(String(100), nullable=False)
    password_hash   = Column(String(20), nullable=False)

    created_at      = Column(DateTime, default=datetime.now())
    updated_at      = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
