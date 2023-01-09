#Jonason He 

import unittest
import sys
import Lab11b

class Testlab11(unittest.TestCase):
    #Add Car - Successful
    def test_function1(self):
        try:
            self.test = Lab11b.add_car("Mercedes", "sls", 1996, "LP3MWF")
            print("Function 1, add_car() - exists\n")
        except AttributeError:
            print("*** Function 1, add_car() - missing\n")
        try:
            self.assertEqual(Lab11b.add_car("Mercedes", "sls", 1996, "LP3MWT"), True)
            print("Function1 - OK")
            print("")
        except:
            print("*** Error Function 1" + str(sys.exc_info()[0]))
            print("")
    
    #Add Car - Car Already Exists
    def test_function2(self):
        try:
            self.test = Lab11b.add_car("Mercedes", "sls", 1996, "LP3MWF")
            print("Function 2, add_car() - exists\n")
        except AttributeError:
            print("*** Function 2, add_car() - missing\n")
        try:
            self.assertEqual(Lab11b.add_car("BMW", "sls", 1996, "LP3MWT"), False)
            print("Function2 - OK")
            print("")
        except:
            print("*** Error Function 2" + str(sys.exc_info()[0]))
            print("")

    #display all cars in parking lot
    def test_function3(self):
        try:
            self.test = Lab11b.display_cars_parking_lot()
            print("Function 3, display_cars_parking_lot() - exists\n")
        except AttributeError:
            print("*** Function 3, display_cars_parking_lot() - missing\n")
        try:
            self.assertEqual(Lab11b.display_cars_parking_lot(), True)
            print("Function3 - OK")
            print("")
        except:
            print("*** Error Function 3" + str(sys.exc_info()[0]))
            print("")

    #Find and display car based on license plate number - Successful
    def test_function4(self):
        try:
            self.test = Lab11b.display_cars_license_plate_number("ABC123")
            print("Function 4, display_cars_license_plate_number() - exists\n")
        except AttributeError:
            print("*** Function 4, display_cars_license_plate_number() - missing\n")
        try:
            self.assertEqual(Lab11b.display_cars_license_plate_number("ARH"), True)
            print("Function4 - OK")
            print("")
        except:
            print("*** Error Function 4" + str(sys.exc_info()[0]))
            print("")

    #Find and display car based on license plate number - No car Found 
    def test_function5(self):
        try:
            self.test = Lab11b.display_cars_license_plate_number("TTTTT")
            print("Function 5, display_cars_license_plate_number() - exists\n")
        except AttributeError:
            print("*** Function 5, display_cars_license_plate_number() - missing\n")
        try:
            self.assertEqual(Lab11b.display_cars_license_plate_number("LP325f"), False)
            print("Function5 - OK")
            print("")
        except:
            print("*** Error Function 5" + str(sys.exc_info()[0]))
            print("")

    #Remove Car - Successful
    def test_function6(self):
        try:
            self.test = Lab11b.remove_car("ABC123")
            print("Function 6, remove_car() - exists\n")
        except AttributeError:
            print("*** Function 6, remove_car() - missing\n")
        try:
            self.assertEqual(Lab11b.remove_car("LP3MWT"), True)
            print("Function6 - OK")
            print("")
        except:
            print("*** Error Function 6" + str(sys.exc_info()[0]))
            print("")
    
    #Remove Car - Fail
    def test_function7(self):
        try:
            self.test = Lab11b.remove_car("ABC123")
            print("Function 7, remove_car() - exists\n")
        except AttributeError:
            print("*** Function 7, remove_car() - missing\n")
        try:
            self.assertEqual(Lab11b.remove_car("ABC123"), False)
            print("Function7 - OK")
            print("")
        except:
            print("*** Error Function 7" + str(sys.exc_info()[0]))
            print("")

if __name__ == "__main__":
    unittest.main()