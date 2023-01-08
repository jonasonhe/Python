#Jonason He

import unittest
import sys
from utilities_sets import * 


class TestUtilitiesSets(unittest.TestCase):

    def test_get_total_items(self):
        '''
        Tests the get_total_items function from utilities set module
        '''
        try:
            #checks if the function exists – raises NameError
            self.test=get_total_items(set_1.copy())
            #checking for number of items in set_1
            self.assertEqual(get_total_items(set_1.copy()),4,)
            print("Function 1 - OK")
        except NameError:
            print("Function 1 missing - get_total_items")
        except:
            print("Error Function 1" + str(sys.exc_info()))

    def test_display_all_items(self):
        '''
        Tests the display_all_items function from utilities set module
        '''
        try:
            #checks if the function exists – raises NameError
            self.test=display_all_items(set_1.copy())
            #checking if the function is returning the result as a list
            returned_list=display_all_items(set_1.copy())
            self.assertTrue(returned_list, list)
            # checking for number of items in set
            self.assertListEqual(returned_list, list(set_1))
            print("Function 2 - OK")
        except NameError:
            print("Function 2 missing - display_all_items")
        except:
            print("Error Function 2" + str(sys.exc_info()))
    
    def test_add_item(self):
        '''
        Tests the add_item function from utilities set module
        '''
        try:
            item = 'pineapple'
            #checks if the function exists – raises NameError
            self.test=add_item(item, set_1.copy())
            #checking if the function is returning the result as a list
            return_list=add_item(item, set_1.copy())
            self.assertTrue(type(return_list), list)
            # checking for number of items in modified set
            result_set=set_1.copy()
            result_set.add(item)
            self.assertSetEqual(set(return_list), result_set,)
            print("Function 3 - OK")
        except NameError:
            print("Function 3 missing - add_items")
        except:
            print("Error Function 3" + str(sys.exc_info()))


    def test_remove_item(self):
        '''
        Tests the remove_item function from utilities set module
        '''
        try:
            item = 'orange'
            #checks if the function exists – raises NameError
            self.test=remove_item(item, set_1.copy())
            #checking if the function is returning the result as a list
            return_list=remove_item(item,set_1.copy())
            self.assertTrue(type(return_list), list)
            # checking for number of items in modified set
            self.assertSetEqual(set(return_list), {'apple', 'banana', 'peach'},)
            print("Function 4 - OK")
        except NameError:
            print("Function 4 missing - remove_item")
        except:
            print("Error Function 4" + str(sys.exc_info()))


    def test_get_the_union_of(self):
        '''
        Tests the get_the_union_of function from utilities set module
        '''
        try:
            #checks if the function exists – raises NameError
            self.test=get_the_union_of(set_1.copy(), set_2.copy())
            result_set=set_1.union(set_2.copy())
            result_list = list(result_set)
            returned_list=get_the_union_of(set_1.copy(), set_2.copy())
            self.assertTrue(type(returned_list), list)
            self.assertListEqual(returned_list, result_list,)
            print("Function 5 - OK")
        except NameError:
            print("Function 5 missing - get_the_union_of")
        except:
            print("Error Function 5" + str(sys.exc_info()))

if __name__ == "__main__":
    unittest.main()
