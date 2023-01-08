#Jonason He

import unittest
import sys
from utilities_dicts import * 


dict_prov_teritories = {"Alberta": "Edmonton", "British Columbia": "Victoria", "Manitoba": "Winnipeg", "New Brunswick": "Fredericton", "Newfoundland and Labrador": "St. John's", "Nova Scotia": "Halifax", "Ontario": "Toronto", "Prince Edward Island": "Charlottetown", "Quebec": "Quebec City", "Saskatchewan": "Regina", "Yukon": "Whitehorse", "Nunavut": "Iqaluit", "Northwest Territories": "Yellowknife"}

class Test_utilities_dict(unittest.TestCase):

    def test_display_all(self):
        '''
        Tests display_all function from utilities dictionary module
        '''
        try:
            #checks if the function exists – raises NameError
            self.test=display_all(dict_prov_teritories.copy())
            #checks if the result returned by the function is the expected one
            return_string = display_all(dict_prov_teritories.copy())
            result_string=''
            for key,value in dict_prov_teritories.copy().items():
                result_string == f'{value} is the capital city of {key}'
            self.assertEqual(return_string, return_string)
            print("Function 1 - OK")
        except NameError:
            print("Function 1 missing - get_total_items")
        except:
            print("Error Function 1" + str(sys.exc_info()))

    def test_get_capital_city(self):
        '''
        Tests the get_capital_city function from utilities dictionary module
        '''
        try:
            #checks if the function exists – raises NameError
            self.test = get_capital_city('British Columbia', dict_prov_teritories.copy())
            #checks if the result returned by the function is the expected one
            self.assertEqual(get_capital_city('British Columbia',dict_prov_teritories.copy()), 'Victoria')
            print("Function 2 - OK")
        except NameError:
            print("Function 2 missing - get_capital_city")
        except:
            print("Error Function 2" + str(sys.exc_info()))

    def test_add_item(self):
        '''
        tests the add_item function from utilities dictionary module
        '''
        try:
            #checks if the function exists – raises NameError
            self.test=add_item('Seattle', 'Washington', dict_prov_teritories.copy())
            #checks if the result returned by the function is the expected one
            returned_string=add_item('Seattle', 'Washington', dict_prov_teritories.copy())
            self.assertEqual(returned_string,"Before 13 elements, after 14 elements",)
            print("Function 3 - OK")
        except NameError:
            print("Function 3 missing - add_item")
        except:
            print("Error Function 3" + str(sys.exc_info()))

    
    def test_remove_item(self):
        '''
        tests the remove_item function from utilities dictionary module
        '''
        try:
            # checks if the function exists – raises NameError
            self.test = remove_item('British Columbia', dict_prov_teritories.copy())
            # checks if the result returned by the function is the expected one
            returned_string = remove_item('British Columbia',dict_prov_teritories.copy())
            self.assertEqual(returned_string,"Before 13 elements, after 12 elements",)
            print("Function 4 - OK")
        except NameError:
            print("Function 4 missing - add_item")
        except:
            print("Error Function 4" + str(sys.exc_info()))


if __name__ == "__main__":
    unittest.main()
