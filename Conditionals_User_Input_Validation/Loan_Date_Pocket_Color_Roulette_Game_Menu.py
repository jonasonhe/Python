# Jonason He

def loan_qualifier(yearly_salary=None, years_employed=None):
    '''
    Determines if a user qualifies for a loan based on their yearly salary and number of years employed.

    :param yearly_salary:
    :param years_employed:
    :return: if the employee qualifies for the loan/error message
    :rtype: str
    '''
    # asks the users to enter yearly salary/years employed and provides a validation input check
    if yearly_salary is None or years_employed is None:  
        while True:
            try:
                yearly_salary = float(input("Enter your yearly salary: "))
                if yearly_salary <= 0:
                    message = "Please enter a salary greater than 0: "
                    print(message)
                    continue
                break
            except:
                print("Please enter a numerical value!")
                continue
        while True:
            try:
                years_employed = float(input("Enter the number of years employed: "))
                if years_employed <= 0:
                    message = "Please enter a years employed greater than 0: "
                    print(message)
                    continue
                break
            except:
                print("Please enter a numerical value!")
                continue
    
    # prints/return a sucess or failure for qualification of a loan
    if yearly_salary >= 50000 and years_employed >= 3:  
        message = "You qualify for a loan."
        print(message)
    elif yearly_salary < 50000:
        message = "Your income must be $50000 or more, you don't qualify for a loan."
        print(message)
    elif years_employed < 3:
        message = "You must be employed for 3 years or more, you don't qualify for a loan."
        print(message)
    return message


def is_magic_date(month=None, day=None, year=None):
    '''
    Determines if a date is a magic date or not based on the user inputs: month/day/year

    :param: month
    :param: day
    :param: year
    :return: A magic Date
    :return: Not a Magic Date
    :rtype: str
    '''
    # asks user to enter a month, day, and year and provides a validation input check
    if month is None or day is None or year is None:  
        while True:
            try:
                month = int(input("Enter a month between 1 and 12: "))
                if month < 1 or month > 12:
                    message = "Please enter a month between 1 and 12: "
                    print(message)
                    continue
                break
            except:
                print("Please enter a numerical value!")
                continue

        while True:
            try:
                day = int(input("Enter a year between 1 and 31: "))
                if day < 1 or day > 31:
                    message = "Please enter a day between 1 and 31: "
                    print(message)
                    continue
                break
            except:
                print("Please enter a numerical value!")
                continue

        while True:
            try:
                year = int(input("Enter the last two positive digits of a year: "))
                if (len(str(year)) != 2) and (year <= 0 or year >= 100):
                    message = "Please enter the last two positive digits of a year: "
                    print(message)
                    continue
                break
            except:
                print("Please enter a numerical value!")
                continue
    
    #Input validation error message
    else:
        if month < 1 or month > 12:
            message = "Please enter a month between 1 and 12:"
            print(message)
            return message
        elif day < 1 or day > 31:
            message = "Please enter a day between 1 and 31:"
            print(message)
            return message
        elif (len(str(year)) != 2) and (year <= 0 or year >= 100):
            message = "Please enter the last two positive digits of a year:"
            print(message)
            return message

    # returns message if its a magic date or not based on the 3 user inputs
    if (day * month) == year:  
        result = "The date %i-%i-%i is a magic date!" % (month, day, year)
        print(result)
    else:
        result = "The date %i-%i-%i is not a magic date!" % (month, day, year)
        print(result)
    return result


def is_even(number=None):
    '''
    Determines if the number the user enters is an even or an odd number

    params: number input as an integer
    return: True if number is even
    return: False if the number is odd
    rtype: str
    '''
    #asks user to input a number and provides a validation check
    if number is None:
        while True:
            try:
                number = int(input("Enter a number: "))
                break
            except:
                print("Please enter a numerical value!")
                continue

    if (number % 2) == 0:
        print("The number", number, "is even.")
        return True, number
    else:
        print("The number", number, "is odd.")
        return False, number


def get_pocket_color(number=None):
    '''
    Returns a pocket color of red, green, or black based on the number a user enters

    :param: number input as an integer
    :return: green, red, or black based on user input
    '''
    #asks user to input a number and provides a validation check
    if number is None:  
        while True:
            try:
                number = int(input("Enter a number between 0 and 36: "))
                if number < 0 or number > 36:
                    message = "Input error"
                    print(message)
                    continue
                break
            except:
                print("Please enter a numerical value!")
                continue
    # for the test case
    else:  
        if number < 0 or number > 36:
            message = "Input error"
            return message

    # returns color (red, green, black) based on the number and what range (1-36) the number falls in
    if number == 0:  
        message = "Green"
        print(message)
    elif 1 <= number <= 10:
        if (number % 2) != 0:
            message = "Red"
            print(message)
        else:
            message = "Black"
            print(message)
    elif 11 <= number <= 18:
        if (number % 2) != 0:
            message = "Black"
            print(message)
        else:
            message = "Red"
            print(message)
    elif 19 <= number <= 28:
        if (number % 2) != 0:
            message = "Red"
            print(message)
        else:
            message = "Black"
            print(message)
    elif 29 <= number <= 36:
        if (number % 2) != 0:
            message = "Black"
            print(message)
        else:
            message = "Red"
            print(message)
    return message


def play_roulette(pocket_no=None, bet=None):
    '''
    This is a roulette function game which will ask the user to enter a pocket number and the amount of a bet, 
    which will also be optional input parameters to the function. 
    On a roulette wheel, the pockets are numbered from 0 to 36. 
    The function displays whether the pocket is green, red, or black and 
    weather the user wins or loses. Returns the message displayed for the user.
    
    params: pocket number
    params: bet
    return: roulette color
    return: amount a user wins/loses and total bet remaining 
    rtype: str
    '''
    #asks user to input a pocket number and a bet
    if pocket_no is None or bet is None:
        test_mode = False
        while True:
            try:
                pocket_no = int(input("Enter a number between 0-36: "))
                if pocket_no < 0 or pocket_no > 36:
                    message = "Please enter a number between 0-36: "
                    print(message)
                    continue
                break
            except:
                print("Please enter a numerical value!")
                continue

        while True:
            try:
                bet = int(input("Enter a bet:"))
                if bet <= 0:
                    message = "Please enter a bet amount higher than 0: "
                    print(message)
                    continue
                break
            except:
                print("Please enter a numerical value!")
                continue
    else:
        test_mode = True

    pocket_print = get_pocket_color(pocket_no)  # finds out if the color is green, red, or black based on the pocket number
    even_number = is_even(pocket_no)[0]  # finds out if the number is even or odd based on the pocket number

    #if the pocket color is green, you end with your original bet
    if pocket_print == "Green":
        result = "You did not win nor lose, you have $%i!" % bet
        print(result)

    #if the pocket color is black and if the number is even, you win 1.5x your original bet
    elif pocket_print == "Black" and even_number is True:
        result = "You won half, you have $%i!" % (bet * 1.5)
        print(result)

    #if the pocket color is red and if the number is even you win double your original bet
    elif pocket_print == "Red" and even_number is True:
        result = "You won double, you have $%i!" % (bet * 2)
        print(result)

    #if the pocket color is black and if the number is odd, you lose your original bet
    elif pocket_print == "Black" and even_number is False:
        result = "Sorry, you lost, you have $%i!" % (bet * 0)
        print(result)

    #asks user if they would like to play the roulette again, 
    if test_mode != True:
        play_again = input("Play again? Y/N: ")
        #if user selects Y, roulette will play again, if the user selects N it will exit the roulette game
        if play_again.upper() == "Y":
            play_roulette()
        else:
            exit
    else:
        return result


def test_function():
    '''
    Test for all functions
    return: whether the functions pass/failed the test
    rtype: str
    '''
    # Loan qualifier Test
    print("Loan Qualifier Test (1000,2)")
    is_loan_qualified = loan_qualifier(1000, 2)
    if is_loan_qualified == "Your income must be $50000 or more, you don't qualify for a loan.":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Loan Qualifier Test (1000, 10)")
    is_loan_qualified = loan_qualifier(1000, 10)
    if is_loan_qualified == "Your income must be $50000 or more, you don't qualify for a loan.":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Loan Qualifier Test (60000, 1)")
    is_loan_qualified = loan_qualifier(60000, 1)
    if is_loan_qualified == "You must be employed for 3 years or more, you don't qualify for a loan.":
        print("Pass")
        print("")

    else:
        print("Fail")
        print("")

    print("Loan Qualifier Test (50004,5)")
    is_loan_qualified = loan_qualifier(50004, 5)
    if is_loan_qualified == "You qualify for a loan.":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Magic Date Test
    print("Magic Date Test (30, 30, 30)")
    magic_date = is_magic_date(30, 30, 30)
    if magic_date == "Please enter a month between 1 and 12:":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Magic Date Test (4, 100, 30)")
    magic_date = is_magic_date(4, 100, 30)
    if magic_date == "Please enter a day between 1 and 31:":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Magic Date Test (4, 30, 1900)")
    magic_date = is_magic_date(4, 30, 1900)
    if magic_date == "Please enter the last two positive digits of a year:":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Magic Date Test (3, 5, 15)")
    magic_date = is_magic_date(3, 5, 15)
    if magic_date == "The date 3-5-15 is a magic date!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Magic Date Test (4, 3, 15)")
    magic_date = is_magic_date(4, 3, 15)
    if magic_date == "The date 4-3-15 is not a magic date!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # even number test
    print("Is Even Test (4)")
    even_odd = is_even(4)[0]
    if even_odd == True:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Is Even Test (7)")
    even_odd = is_even(7)[0]
    if even_odd == False:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # test pocket color
    print("Pocket Color Test (-3)")
    pocket_color = get_pocket_color(-3)
    if pocket_color == "Input error":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (37)")
    pocket_color = get_pocket_color(37)
    if pocket_color == "Input error":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (0)")
    pocket_color = get_pocket_color(0)
    if pocket_color == "Green":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (3)")
    pocket_color = get_pocket_color(3)
    if pocket_color == "Red":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (10)")
    pocket_color = get_pocket_color(10)
    if pocket_color == "Black":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (11)")
    pocket_color = get_pocket_color(11)
    if pocket_color == "Black":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (16)")
    pocket_color = get_pocket_color(16)
    if pocket_color == "Red":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (18)")
    pocket_color = get_pocket_color(18)
    if pocket_color == "Red":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (19)")
    pocket_color = get_pocket_color(19)
    if pocket_color == "Red":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (26)")
    pocket_color = get_pocket_color(26)
    if pocket_color == "Black":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (28)")
    pocket_color = get_pocket_color(28)
    if pocket_color == "Black":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (29)")
    pocket_color = get_pocket_color(29)
    if pocket_color == "Black":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (34)")
    pocket_color = get_pocket_color(34)
    if pocket_color == "Red":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Pocket Color Test (36)")
    pocket_color = get_pocket_color(36)
    if pocket_color == "Red":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # test roulette
    print("Roulette Test (0, 100)")
    roulette = play_roulette(0, 100)
    if roulette == "You did not win nor lose, you have $100!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Roulette Test (10, 100)")
    roulette = play_roulette(10, 100)
    if roulette == "You won half, you have $150!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Roulette Test (18, 1000)")
    roulette = play_roulette(18, 1000)
    if roulette == "You won double, you have $2000!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Roulette Test (29, 100)")
    roulette = play_roulette(29, 100)
    if roulette == "Sorry, you lost, you have $0!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")


def main():
    '''
    User testing menu to test all functions
    returns: Function test and returns pass/fail for each function
    '''
    string_menu = '''
    =============================
    Choose an option or 0 to exit
    -----------------------------
    [1] Loan Qualifier
    [2] Is Magic Date
    [3] Is Even
    [4] Get Pocket Color
    [5] Play Roulette
    [6] Test Functions
    [0] Exit 
    =============================
    '''
    
    while True:
        print(string_menu)
        # loop till integer 0 to 4 entered
        while True:
            choice = input("please choose between [1-6], or [0] to exit: ")
            # Check if choice an integer 1 - 6
            if choice.isdigit() and int(choice) in range(7):
                # make choice an int
                choice = int(choice)
                # Exit choice loop
                break

        if choice == 1:
            print("----------------------------------------------------------------------")
            print("Running [1] Loan Qualifier\n")
            # Call function [1]
            call = loan_qualifier()

        elif choice == 2:
            print("----------------------------------------------------------------------")
            print("Running [2] Is Magic Date\n")
            # Call function [2]
            call = is_magic_date()

        elif choice == 3:
            print("----------------------------------------------------------------------")
            print("Running [3] Is Even\n")
            # Call function [3]
            call = is_even()

        elif choice == 4:
            print("----------------------------------------------------------------------")
            print("Running [4] Get Pocket Color\n")
            # Call function [4]
            call = get_pocket_color()
        
        elif choice == 5:
            print("----------------------------------------------------------------------")
            print("Running [5] Play Roulette\n")
            # Call function [5]
            call = play_roulette()
        
        elif choice == 6:
            print("----------------------------------------------------------------------")
            print("Running [6] Test Functions\n")
            # Call function [6]
            test = test_function()
            

        elif choice == 0:
            print("----------------------------------------------------------------------")
            print("Thanks for your time, good bye!")
            # Exit main loop
            break

        input("\nType enter key to continue...")


if __name__ == "__main__":
    main()
