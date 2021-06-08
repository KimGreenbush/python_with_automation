class Stock:

    # Constructor for the Stock class
    def __init__(self, stock_name, stock_price, stock_symbol, price_history):
        self._stock_name = stock_name
        self._stock_price = stock_price
        # The symbol is unique to every stock, so we can use it as an identifier. We are ignoring
        # the existence of exchanges.
        self._stock_symbol = stock_symbol
        self._price_history = price_history