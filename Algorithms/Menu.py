#Jonason He 

import Algorithms

def test_algorithms():
    '''
    Test the functions found in algorithms module
    '''
    #Sum_avg_test 1
    print("Test 1 sum_avg_two_numbers (tt, 100)")
    sum_avg_test = Algorithms.sum_avg_two_numbers("tt", "100")
    if sum_avg_test == "Invalid entry. Please enter a number value.":
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #Sum_avg_test 2
    print("Test 2 sum_avg_two_numbers (100, tt)")
    sum_avg_test = Algorithms.sum_avg_two_numbers("100", "tt")
    if sum_avg_test == "Invalid entry. Please enter a number value.":
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #Sum_avg_test 3
    print("Test 3 sum_avg_two_numbers (50, 100)")
    sum_avg_test = Algorithms.sum_avg_two_numbers("50", "100")
    if sum_avg_test == ("The sum is: 150", "The average is: 75.0"):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")

    #max_min test 1
    print("max_min test 1 (t)")
    max_min_test = Algorithms.max_min("t")
    if max_min_test == ("Invalid Entry. Please enter a number value."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #max_min test 2
    print("max_min test 2 (3), 3,2,1")
    max_min_test = Algorithms.max_min("3")
    if max_min_test == ("The maximium number is 3", "The minimum number is 1"):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")

    #area_perimeter_rectangle test 1
    print("area_perimter_rectangle test 1 (tt,100)")
    area_perimeter_test = Algorithms.area_perimeter_rectangle("tt", "100")
    if area_perimeter_test == ("Invalid entry. Please enter a number value."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #area_perimeter_rectangle test 2
    print("area_perimter_rectangle test 2 (100,tt)")
    area_perimeter_test = Algorithms.area_perimeter_rectangle("100", "tt")
    if area_perimeter_test == ("Invalid entry. Please enter a number value."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #area_perimeter_rectangle test 3
    print("area_perimter_rectangle test 3 (100,50)")
    area_perimeter_test = Algorithms.area_perimeter_rectangle("100", "50")
    if area_perimeter_test == ("The area of the rectangle is 5000.0", "The perimeter of the rectangle is 300.0"):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")

    #sum_product_number test 1
    print("sum_product_number test 1 (tt)")
    sum_product_test = Algorithms.sum_product_number("tt")
    if sum_product_test == ("Invalid entry. Please enter a number value."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #sum_product_number test 2
    print("sum_product_number test 2 (3)")
    sum_product_test = Algorithms.sum_product_number("3")
    if sum_product_test == ("The sum of first n numbers is: 6", "The product of first n numbers is: 6"):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")

    #string_info test 1
    print("string_info test 1 (3)")
    string_info_test = Algorithms.string_info("house of the dragon 3")
    if string_info_test == ("Invalid entry. Text cannot contain numbers."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #string_info test 2
    print("string_info test 2 (house of the dragon)")
    string_info_test = Algorithms.string_info("house of the dragon")
    if string_info_test == ("The number of characters in this string is: 19", 
    "The number of words in this string is: 4","HOUSE OF THE DRAGON", 
    "house of the dragon"):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #Calculator test 1
    print("Calculator test 1 (t, +, 2)")
    calculator_test = Algorithms.calculator("t", "+", "2")
    if calculator_test == ("Invalid entry. Please enter a number."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")

    #Calculator test 2
    print("Calculator test 2 (1, t, 2)")
    calculator_test = Algorithms.calculator("1", "t", "2")
    if calculator_test == ("Invalid entry. Please enter an operand (+,-, *,/)."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #Calculator test 3
    print("Calculator test 3 (1, +, t)")
    calculator_test = Algorithms.calculator("1", "+", "t")
    if calculator_test == ("Invalid entry. Please enter a number."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #Calculator test 4
    print("Calculator test 4 (1, +, 2)")
    calculator_test = Algorithms.calculator("1", "+", "2")
    if calculator_test == ("The sum of the two numbers are 3.0."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #Calculator test 5
    print("Calculator test 5 (1, -, 2)")
    calculator_test = Algorithms.calculator("1", "-", "2")
    if calculator_test == ("The difference of the two numbers are -1.0."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")
    
    #Calculator test 6
    print("Calculator test 6 (1, *, 2)")
    calculator_test = Algorithms.calculator("1", "*", "2")
    if calculator_test == ("The product of the two numbers are 2.0."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")

    #Calculator test 7
    print("Calculator test 7 (1, /, 2)")
    calculator_test = Algorithms.calculator("1", "/", "2")
    if calculator_test == ("The division of the two numbers are 0.5."):
        print("Result:")
        print("Pass")
        print("")
    else:
        print("Result:")
        print("Fail")
        print("")


def main():
    '''
    User testing menu to test all functions
    returns: Function test and returns pass/fail for each function
    '''
    string_menu = '''
    =============================
    Please select an option from [0-7] or 0 to exit
    -----------------------------
    [1] Sum and Average of Two Numbers
    [2] Maximum and minimum of 5 numbers
    [3] Area and Perimeter of a rectangle
    [4] Sum and product of first N natural numbers
    [5] String Info
    [6] Calculator
    [7] Test Functions
    [0] Exit 
    =============================
    '''
    repeat = True
    while repeat:
        while True:
            print(string_menu)
            while True:
                try:
                    choice = int(input("Enter your option from 0-7: "))
                    if choice < 0 or choice > 7:
                        continue
                    break
                except:
                    continue

            if choice == 1:
                print("-----------------------------")
                print("Running function [1] Sum/Avg of two numbers Functino")
                sum_avg = Algorithms.sum_avg_two_numbers()

            elif choice == 2:
                print("-----------------------------")
                print("Running function [2] Max Min Function")
                max_min_loop = Algorithms.max_min()

            elif choice == 3:
                print("-----------------------------")
                print("Running function [3] Rectangle Area and Perimeter Function")
                rectangle = Algorithms.area_perimeter_rectangle()

            elif choice == 4:
                print("-----------------------------")
                print("Running function [4] Sum/Product function")
                sum_product = Algorithms.sum_product_number()

            elif choice == 5:
                print("-----------------------------")
                print("Running function [5] String Info Function")
                string_info = Algorithms.string_info()
            
            elif choice == 6:
                print("-----------------------------")
                print("Running function [6] Calculator")
                calc = Algorithms.calculator()
            
            elif choice == 7:
                print("-----------------------------")
                print("Running function [7] Display Test Functions")
                test = test_algorithms()
            
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

