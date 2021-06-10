class Stock:

    # Constructor for the Stock class
    def __init__(self, stock_name, stock_price, stock_symbol, price_history):
        self._stock_name = stock_name
        self._stock_price = stock_price
        # The symbol is unique to every stock, so we can use it as an identifier. We are ignoring
        # the existence of exchanges.
        self._stock_symbol = stock_symbol
        self._price_history = price_history

    # Scenario: We need a way to compare two stocks.
    # This is very Java way of comparing two instances of a class
    def compare_to(self, other):
        return self._stock_price - other._stock_price

    # Python has a much cleaner way of comparing two instances of a class. We can do this using "dunder"
    # methods. "Dunder" is an abbreviation for "double underscore" since these methods are preceded and
    # followed by double underscores.
    # __gt__ is a dunder method inherited from the object class that allows us to override the behavior of
    # the ">" symbol so that we can use it to compare instances of our class.
    # This essentially provides operator overloading.
    def __gt__(self, other):
        if self._stock_price > other._stock_price:
            return True
        else:
            return False

stock1 = Stock('stock 1', 12, 'DERP', list())
stock2 = Stock('stock 2', 343, 'JAJA', list())

print(stock1.compare_to(stock2))

if stock1 < stock2:
    print('Stock 1 has a higher stock price than stock 2')