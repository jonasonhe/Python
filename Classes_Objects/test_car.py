#Jonason He 

import unittest
import sys

from Car import Car


class TestCar(unittest.TestCase):
    """ Tests for the Car class """

    @classmethod
    def tearDownClass(cls):
        """ Tears down the Test Case """
        print("Tears down the Test Case")

    def setUp(self):
        """ Sets up the car objects to test in the subsequent tests """
        self.car1 = Car("Lexus", "Rx", 2014, 5000.0, 20000.0)
        

    def test_constructor(self):
        self.assertIsNotNone(self.car1)
        

    def test_details(self):
        try:
            test = self.car1.get_details()
            print("Function 1, get_details() - exists\n")
        except AttributeError:
            print("*** Function 1, get_details() - missing\n")
        try: 
            self.assertEqual("2014 Lexus Rx for sale for $20000.0", self.car1.get_details())
            print("Function1 - OK")
            print("")
        except: 
            print("*** Error Function 1" + str(sys.exc_info()[0]))
            print("")

    def test_profit(self):
        try:
            test = self.car1.calc_profit()
            print("Function 2, calc_profit() - exists\n")
        except AttributeError:
            print("*** Function 2, calc_profit() - missing\n")
        try:
            self.assertEqual(self.car1.calc_profit(), 15000.0)
            print("Function2 - OK")
            print("")
        except: 
            print("*** Error Function 2" + str(sys.exc_info()[0]))
            print("")
    
    def test_price_reduction(self):
        try:
            test = self.car1.reduce_price(50)
            print("Function 3, reduce_price() - exists\n") 
        except AttributeError:
            print("*** Function 3, reduce_price() - missing\n")
        try: 
            self.assertEqual(self.car1.calc_profit(), 14950.0)
            print("Function3 - OK")
            print("")
        except: 
            print("*** Error Function 3" + str(sys.exc_info()[0]))
            print("")
        
    
if __name__ == "__main__":
    unittest.main()


