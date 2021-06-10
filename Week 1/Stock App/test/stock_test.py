# We are importing the Stock class from the stock module. An instance will be our "object under test".
from src.models.stock import Stock

# We'll also import "unittest" as it readily available as a part of our standard library.
import unittest

# In order to write unit tests, we must create a test class that extends the unittest module's TestCase
# class. The unittest framework will create an instance of this test class for us when we run our application.

class StockTest(unittest.TestCase):

    # Conventionally, when we design our test cases, we do some "set up" and "teardown". We use our setup
    # to establish prerequisites to running a test (e.g. opening a connection to a testing, in-memory database,
    # opening a stream from which you need to pull to dummy data, or even just initializing an array of dummy
    # data our creating an instance of your object under test). We use our teardown to close any resources
    # that we opened during testing.

    # Many testing frameworks have conventional methods that we use to perform set up and teardown.
    # unittest uses the "setUp" method. If you have a method called setUp, it will be run first.

    def setUp(self):
        # The only setup that we currently have is the initialization of our object under test.
        # We've create two stocks because we need to pass another instance of stock to the compare_to
        # method.
        self.dummy_stock = Stock('dummy stock', 100, 'MOCK', list())
        self.other_dummy_stock = Stock('other dummy stock', 222, 'STO2', list())

    def test_compare_to(self):
        returned_integer = self.dummy_stock.compare_to(self.other_dummy_stock)
        # I need to verify that this method returns what I think it returns (a negative number)
        # We are using assertLess because we expect our returned_integer to be less than 0 in this case
        self.assertLess(returned_integer, 0)
        # We are using assertEquals because we expect the returned_integer to equal -122 per our method's
        # implementation.
        self.assertEquals(returned_integer, -122)

    # Our tear down method has to be called tearDown. This method will be run last, after all of our test
    # cases have been run.
    def tearDown(self):
        # If we had teardown, it would be something along the lines of closing the connection to our DB,
        # closing files, quitting of instances of web browsers (this assumes that you performed an automated
        # task in a browser)
        pass