# This is a simple class declaration. Please note that the colon is required and that the indentation
# matters in Python.
class Portfolio:

    # Someone initially suggested that we create an "id" field, but "id" is actually a built-in function
    # in Python. As such, we would be "shadowing" that built-in function if we called this field "id".
    # As a result, we chose a different name.
    # A unique identifier for our portfolio
    # portfolio_id = 0
    # # A portfolio name for our portfolio
    # portfolio_name = 'n/a'
    # # A list of stocks in this portfolio
    # portfolio_stocks = []
    # # A balance for portfolio
    # portfolio_balance_history = []

    # This is the syntax for creating a constructor in Python. Note that the "def" keyword is used to
    # define methods and functions. The first parameter for methods in a class is conventionally called
    # "self". This first argument refers to the current instance of the class.
    # Also note that we do not have to define our own constructor in Python as we are given a default,
    # no-args constructor.
    # We are using mix of both positional and keyword arguments. Note that you must pass in the positional
    # arguments when this constructor is called, but you do not have to pass in the keyword args.
    # All of the keyword arguments must be AFTER the positional arguments.
    def __init__(self, portfolio_id, portfolio_name, portfolio_stocks=[2, 3], portfolio_balance_history=[]):
        # We have prefixed the property names with an underscore "_" to indicate that we intend to use
        # them as private members of the class, but this does not prevent direct access to the properties.
        self._portfolio_id = portfolio_id
        self._portfolio_name = portfolio_name
        self._portfolio_stocks = portfolio_stocks
        self._portfolio_balance_history = portfolio_balance_history

    # Generally speaking, you will have getters and setters for your properties.
    def get_portfolio_stocks(self):
        return self._portfolio_stocks

    def set_portfolio_stocks(self, _portfolio_stocks):
        # This self keyword allows us reference the property "_portfolio_stocks", which has the same
        # name as the parameter that we have defined here.
        self._portfolio_stocks = _portfolio_stocks