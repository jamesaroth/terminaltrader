import time
from app.orm import ORM
from app.util import hash_pass, get_price
from app.position import Position
from app.trade import Trade


SALT = "nobody will ever guess this"


class Account(ORM):
    fields = ["username", "password_hash", "balance"]
    table = "accounts"

    def __init__(self):
        self.pk = None
        self.username = None
        self.password_hash = None
        self.balance = None

    def set_password(self, password):
        self.password_hash = hash_pass(password)

    @classmethod
    def login(cls, username, password):
        account = cls.select_one("WHERE password_hash = ? AND username = ?", (hash_pass(password), username))
        if not account:
            return None
        else:
            return account

    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("cannot make negative deposit")
        self.balance += amount
        self.save()


    def get_positions(self):
        """ return a list of each Position object for this user """
        where = "WHERE account_pk = ?"
        values = (self.pk, )
        return Position.select_many(where, values)

    def get_trades(self):
        """ return a list of all Trades for this user """
        where = "WHERE account_pk = ?"
        values = (self.pk, )
        return Trade.select_many(where, values)

    def get_trades_for(self, symbol):
        """ return a list of all Trades for a given symbol for this user """
        where = "WHERE account_pk = ? AND ticker = ?"
        values = (self.pk, symbol)
        return Trade.select_many(where, values)
    
    def get_position_for(self, ticker):
        where = "WHERE account_pk = ? AND ticker = ?"
        values = (self.pk, ticker)
        result = Position.select_one(where,values)
        if result:
            return result
        
        position = Position()
        position.account_pk = self.pk
        position.ticker = ticker
        position.shares = 0
        return position

    def buy(self, ticker, amount):
        price = get_price(ticker)
        if self.balance < price * amount:
            raise ValueError("Insufficient Funds")
        self.balance -= price * amount
        trade = Trade()
        trade.account_pk = self.pk
        trade.ticker = ticker
        trade.price = price
        trade.volume = amount
        trade.time = time.time()

        position = self.get_position_for(ticker)
        position.shares += amount
        self.save()
        trade.save()
        position.save()

    def sell(self, ticker, amount):
        price = get_price(ticker)
        position = self.get_position_for(ticker)
        if position.shares < amount:
            raise ValueError("Insufficient Shares to Sell or Position Does not Exist")
        self.balance += price * amount
        trade = Trade()
        trade.account_pk = self.pk
        trade.ticker = ticker
        trade.price = price
        trade.volume = -1 * amount
        trade.time = time.time()

        position.shares -= amount
        self.save()
        trade.save()
        position.save()