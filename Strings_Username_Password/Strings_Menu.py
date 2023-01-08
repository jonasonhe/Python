#Jonason He 

import login
import data_format
import test_functions

def main():
    '''
    User testing menu to test all functions
    returns: Function test and returns pass/fail for each function
    '''
    string_menu = '''
    =============================
    Choose an option or 0 to exit
    -----------------------------
    [1] Generate Login
    [2] Change Password
    [3] Get Book Info
    [4] Display Book Info CSV
    [5] Display Book Info JSON
    [6] Test Function
    [0] Exit 
    =============================
    '''
    book_info = None
    csv_data = None
    repeat = True
    while repeat:
        while True:
            print(string_menu)
            while True:
                try:
                    choice = int(input("Enter your option from 0-6: "))
                    if choice < 0 or choice > 6:
                        continue
                    break
                except:
                    continue

            if choice == 1:
                print("-----------------------------")
                print("Running function [1] Generate Login")
                user_pass = login.generate_login()

            elif choice == 2:
                print("-----------------------------")
                print("Running function [2] Change Password")
                change_pass = login.change_password()

            elif choice == 3:
                print("-----------------------------")
                print("Running function [3] Get Book Info")
                book_info = data_format.get_book_info()

            elif choice == 4:
                print("-----------------------------")
                print("Running function [4] Display Book Info CSV")
                if book_info != None:
                    csv_data = data_format.convert_to_csv_format(book_info)
                    print(csv_data)
                else:
                    print("Missing book info: Call function [3]")

            elif choice == 5:
                print("-----------------------------")
                print("Running function [5] Display Book Info JSON")
                if csv_data != None:
                    json_format = data_format.convert_to_json_format(csv_data)
                    print(json_format)
                else:
                    print("Missing csv data: Call function [4]")
            
            elif choice == 6:
                print("-----------------------------")
                print("Running function [6] Display Test Functions")
                test = test_functions.test_function()
            

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