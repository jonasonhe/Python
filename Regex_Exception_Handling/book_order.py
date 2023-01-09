#Jonason He 

import book_order_utils
import sys

def main(display_menu=False):
    """Main function, menu to call other functions"""
    try:
        if len(sys.argv) != 8:
            sys.argv = [
                "book_test",
                "0001",
                "Intro to Python",
                "Sally Lee",
                "123456",
                "1990",
                "10",
                "101.10"
            ]
        order_no = sys.argv[1]
        title = sys.argv[2]
        author = sys.argv[3]
        isbn = sys.argv[4]
        year = sys.argv[5]
        quantity = sys.argv[6]
        cost = sys.argv[7]
    finally:
        unit_cost = ""
    string_menu = '''
    ==============================================================
                Book Order - Name
    --------------------------------------------------------------
    [1] Validate book order details
    [2] Calculate cost per book
    [3] Save book order details
    [4] Test Functions
    [0] Exit 
    ==============================================================
    '''
    # Loop menu till 0 entered for exit
    if display_menu:
        while True:
            print(string_menu)
            # loop till integer 0 to 4 entered
            while True:
                choice = input("please choose between [1-4], or [0] to exit: ")
                # Check if choice an integer 0 to 4
                if choice.isdigit() and int(choice) in range(5):
                    # make choice an int
                    choice = int(choice)
                    # Exit choice loop
                    break

            if choice == 1:
                print("----------------------------------------------------------------------")
                print("Running [1] Validate book order details\n")
                # Call function [1]
                try:
                    book_order_utils.validate_book_order_details("1", "Fire and Blood", "George RR Martin", "12345", "2011", "190", "25.00")
                except ValueError as e:
                    print("Value Error:", e)
                except TypeError as e:
                    print("Type Error:", e)

            elif choice == 2:
                print("----------------------------------------------------------------------")
                print("Running [2] Calculate cost per book\n")
                # Call function [2]
                try:
                    unit_cost = book_order_utils.calculate_per_book_cost(20, 5)
                except ZeroDivisionError:
                    print("No Books in Order")
                except ValueError as e:
                    print("Value Error:", e)

            elif choice == 3:
                print("----------------------------------------------------------------------")
                print("Running [3] Save book order details\n")
                # Call function [3]
                filename = "BookOrder.txt"
                try:
                    book_order_utils.write_book_order_details("test.txt", "0001", "Intro to Python", "Bill Smith", "12345", "2000", "10", "100.45", 10.045)
                except ValueError as e:
                    print("Value Error:", e)

            elif choice == 4:
                print("----------------------------------------------------------------------")
                print("Running [4] Test functions\n")
                # Test all functions
                test = book_order_utils.test_functions()

            elif choice == 0:
                print("----------------------------------------------------------------------")
                print("Thanks for your time, good bye!")
                # Exit main loop
                break

            input("\nType enter key to continue...")
            # Loops back to start of menu loop
    # No menu
    else:
        # setup variable
        error = False
        # Function [1]
        try:
            book_order_utils.validate_book_order_details(order_no, title, author, isbn, year, quantity, cost)
        # Check for errors
        except ValueError as e:
            print("Value Error:", e)
            # set error to True to skip other functions
            error = True
        # Check for errors
        except TypeError as e:
            print("Type Error:", e)
            # set error to True to skip other functions
            error = True
        # check if error is True
        if not error:
            # function [2]
            try:
                unit_cost = book_order_utils.calculate_per_book_cost(cost, quantity)
            # Check for errors
            except ZeroDivisionError:
                print("No Books in Order")
                # set error to True to skip other functions
                error = True
        # set file name
        filename = f"{order_no}.txt"
        # check if error is True
        if not error:
            # function [3]
            try:
                book_order_utils.write_book_order_details(filename, order_no, title, author, isbn, year, quantity, cost,
                                                          unit_cost)
            # Check for errors
            except ValueError as e:
                print("Value Error:", e)


if __name__ == "__main__":
    main(display_menu=True)