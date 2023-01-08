#Jonason He 

set_1 = {"apple", "banana", "orange", "peach"}
set_2 = {"banana", "pineapple", "peach", "watermelon"}

dict_prov_teritories = {"Alberta": "Edmonton", "British Columbia": "Victoria", "Manitoba": "Winnipeg", "New Brunswick": "Fredericton", "Newfoundland and Labrador": "St. John's", "Nova Scotia": "Halifax", "Ontario": "Toronto", "Prince Edward Island": "Charlottetown", "Quebec": "Quebec City", "Saskatchewan": "Regina", "Yukon": "Whitehorse", "Nunavut": "Iqaluit", "Northwest Territories": "Yellowknife"}


import utilities_sets
import utilities_dicts


def main():
    '''
    User testing menu to test all functions
    returns: Function test and returns pass/fail for each function
    '''
    string_menu = '''
    =============================
    Choose an option or 0 to exit
    -----------------------------
    [1] Get Total Item Set
    [2] Display all Items Set
    [3] Add Item Set
    [4] Remove Item Set
    [5] Get Union of Sets
    [6] Display All Dictionary
    [7] Get Capital City Dictionary
    [8] Add Item Dictionary
    [9] Remove Item Dictionary
    [10] Test Functions Set
    [11] Test Functions Dictionary
    [0] Exit 
    =============================
    '''
    repeat = True
    while repeat:
        while True:
            print(string_menu)
            while True:
                try:
                    choice = int(input("Enter your option from 0-11: "))
                    if choice < 0 or choice > 11:
                        continue
                    break
                except:
                    continue

            if choice == 1:
                print("-----------------------------")
                print("Running function [1] Get Total Items Set")
                function = utilities_sets.get_total_items()

            elif choice == 2:
                print("-----------------------------")
                print("Running function [2] Display all Items Set")
                function = utilities_sets.display_all_items()

            elif choice == 3:
                print("-----------------------------")
                print("Running function [3] Add Item Set")
                function = utilities_sets.add_item()

            elif choice == 4:
                print("-----------------------------")
                print("Running function [4] Remove Item Set")
                fucntion = utilities_sets.remove_item()

            elif choice == 5:
                print("-----------------------------")
                print("Running function [5] Get Union of Set")
                function = utilities_sets.get_the_union_of()

            elif choice == 6:
                print("-----------------------------")
                print("Running function [6] Display All Dictionary")
                function = utilities_dicts.display_all()
            
            elif choice == 7:
                print("-----------------------------")
                print("Running function [7] Get Capital City Dictionary")
                function = utilities_dicts.get_capital_city()

            elif choice == 8:
                print("-----------------------------")
                print("Running function [8] Add Item Dictionary")
                function = utilities_dicts.add_item()

            elif choice == 9:
                print("-----------------------------")
                print("Running function [9] Remove item Dictionary")
                function = utilities_dicts.remove_item()
            
            elif choice == 10:
                print("-----------------------------")
                print("Running function [10] Test Set Functions")
                test = utilities_sets.test_function_set()


            elif choice == 11:
                print("-----------------------------")
                print("Running function [11] Test Dictionary Functions")
                test = utilities_dicts.test_function_dict()


            elif choice == 0:
                print("-----------------------------")
                print("Thank you for your time, Goodbye!")
                break

            print("\n")
            print("Type any key to continue...", end=' ')
            if input():
                continue

if __name__ == "__main__":
    main()