#Jonason He 

#1
def sum_avg_two_numbers(first_number = None, second_number = None):
    '''
    Asks the user to input two numbers and returns the sum and average of the two numbers.
    params: first number, second number
    returns: sum/average of the two numbers
    '''
    if first_number == None or second_number == None:

        while True:  
            first_number = input("Enter your first number:")
            if first_number.isdigit() == False:
                error = "Invalid entry. Please enter a number value."
                print(error)
                continue
            else: 
                break

        while True:
            second_number = input("Enter your second number:")
            if second_number.isdigit() == False: 
                error = "Invalid entry. Please enter a number value."
                print(error)
                continue
            else: 
                break
    else: 
        if first_number.isdigit() == False: 
            error = "Invalid entry. Please enter a number value."
            return error
        elif second_number.isdigit() == False:
            error = "Invalid entry. Please enter a number value."
            return error 
    
    first_number_formatted = int(first_number)
    second_number_formatted = int(second_number)

    sum = first_number_formatted + second_number_formatted
    sum_message = f"The sum is: {sum}"
    print(sum_message)

    average = (first_number_formatted + second_number_formatted)/2
    average_message = f"The average is: {average}"
    print(average_message)

    return sum_message, average_message

#2
def max_min(number_of_times = None):
    '''
    Asks the user to input a number and based on the number the user 
    enters, will ask the user to input n amount of numbers 
    and will output the sum of all the numbers entered 
    
    params: initial number of times the user should enter
    returns: sum of the total n numbers the user enters
    '''
    if number_of_times == None: 
        while True: 
            number_of_times = input("How many numbers do you want to enter: ")
            if number_of_times.isdigit() == False: 
                error = "Invalid Entry. Please enter a number value."
                print(error)
                continue
            else:
                break
    else: 
        if number_of_times.isdigit() == False: 
            error = "Invalid Entry. Please enter a number value."
            return error
    
    
    number_of_times_formatted = int(number_of_times)

    lst = []
    for n in range (number_of_times_formatted):
        numbers = input("Enter number: ")
        if numbers.isdigit() == False: 
                print("Invalid Entry. Please enter a number value.")
                continue
        
    number_of_times_formatted_list = int(numbers)
    lst.append(number_of_times_formatted_list)
    
    max_numb = max(lst)
    max_numb_message = f"The maximium number is {max_numb}"
    print(max_numb_message)
    min_numb = min(lst)
    min_numb_messsage = f"The minimum number is {min_numb}"
    print(min_numb_messsage)


    return max_numb_message, min_numb_messsage
    

#3
def area_perimeter_rectangle(width = None, length = None):
    '''
    Takes the width and lenght that the user enters and returns the area and perimeter of a rectangle.
    \
    params: width and length
    returns: rectangle area, rectangle perimeter
    '''
    if width == None or length == None: 

        while True: 
            width = input("Enter the width of the rectangle: ")
            if width.isdigit() == False: 
                error = "Invalid entry. Please enter a number value."
                print(error)
                continue
            else:
                break
        while True: 
            length = input("Enter the length of the triange: ")
            if length.isdigit() == False: 
                error = "Invalid entry. Please enter a number value."
                print(error)
                continue
            else: 
                break
    else: 
        if width.isdigit() == False: 
            error = "Invalid entry. Please enter a number value."
            return error
        elif length.isdigit() == False: 
            error = "Invalid entry. Please enter a number value."
            return error
    
    width_formatted = float(width)
    length_formatted = float(length)

    area = width_formatted * length_formatted
    area_message = f"The area of the rectangle is {area}"
    print(area_message)

    perimeter = 2 * (width_formatted + length_formatted)
    perimeter_message = f"The perimeter of the rectangle is {perimeter}"
    print(perimeter_message)

    return area_message, perimeter_message


#4
def sum_product_number(number = None):
    '''
    Asks the user to enter a number and will sum the total number in the range from 1 to the number the user originally entered.
    
    params: number
    return: sum of the total numbers from range 1 to the number the user originally entered 
    '''
    if number == None: 
        while True: 
            number = input("Enter a number: ")
            if number.isdigit() == False:
                error = "Invalid entry. Please enter a number value."
                print(error)
                continue
            else: 
                break
    else: 
        if number.isdigit() == False: 
            error = "Invalid entry. Please enter a number value."
            return error
    
    number_formatted = int(number)

    sum = 0 
    for num in range (1, number_formatted+1, 1):
        sum = sum + num
    sum_message = f"The sum of first n numbers is: {sum}"
    print(sum_message)

    product = 1
    for num in range (1, number_formatted+1, 1):
        product = product * num
    product_message = f"The product of first n numbers is: {product}"
    print(product_message)

    return sum_message, product_message


#5 
def string_info(text = None):
    '''
    Asks the user to enter a string and returns with the number of 
    characters, number of words, uppercases/lowercases the string
    
    params: string that a user inputs
    returns: number of characters, number of words, uppercases/lowercases the string
    '''
    if text == None: 
        while True: 
            text = input("Enter a word: ")
            if any(char.isdigit() for char in text) == True: 
                error = "Invalid entry. Text cannot contain numbers."
                print(error)
                continue
            else: 
                break
    else: 
        if any(char.isdigit() for char in text) == True: 
            error = "Invalid entry. Text cannot contain numbers."
            return error
    
    char_number = len(text)
    message_char = f"The number of characters in this string is: {char_number}"
    print(message_char)

    word_number = len(text.split())
    message_word = f"The number of words in this string is: {word_number}"
    print(message_word)

    text_upper = text.upper()
    print(text_upper)

    text_lower = text.lower()
    print(text_lower)

    return message_char, message_word, text_upper, text_lower


#6 
def calculator(first_number = None, operand = None, second_number = None):
    '''
    calculator that takes 2 numbers and one operand from the user 
    and allows the user to either play again or quit 
    
    params: first number, operand, second number
    return: result of the two numbers based on which operand was inputted
    '''
    if first_number == None or operand == None or second_number == None:
        test_mode = False
        while True: 
            first_number = input("Enter your first number: ")
            if first_number.isdigit() == False: 
                error = "Invalid entry. Please enter a number."
                print(error)
                continue
            else: 
                break
        while True: 
            operand = input("Please enter an operand (+,-, *,/): ")
            if operand not in ("+", "-", "*", "/"): 
                error = "Invalid entry. Please enter an operand (+,-, *,/)."
                print(error)
                continue
            else: 
                break
        while True: 
            second_number = input("Enter your second number: ")
            if second_number.isdigit() == False: 
                error = "Invalid entry. Please enter a number."
                print(error)
                continue
            else: 
                break
    else:
        test_mode = True 
        if first_number.isdigit() == False: 
            error = "Invalid entry. Please enter a number."
            return error
        elif operand not in ("+", "-", "*", "/"): 
            error = "Invalid entry. Please enter an operand (+,-, *,/)."
            return error
        elif second_number.isdigit() == False: 
            error = "Invalid entry. Please enter a number."
            return error
    
    first_number_formatted = float(first_number)
    second_number_formatted = float(second_number)
    operand_formatted = str(operand)

    if operand_formatted == "+":
        add = first_number_formatted + second_number_formatted
        add_message = f"The sum of the two numbers are {add}."
        print(add_message)
        return add_message
    elif operand_formatted == "-":
        subtract = first_number_formatted - second_number_formatted
        subtract_message = f"The difference of the two numbers are {subtract}."
        print(subtract_message)
        return subtract_message
    elif operand == "*":
        mul = first_number_formatted * second_number_formatted
        mul_message = f"The product of the two numbers are {mul}."
        print(mul_message)
        return mul_message
    elif operand_formatted == "/" and second_number_formatted != 0:
        divide = first_number_formatted / second_number_formatted 
        divide_message = f"The division of the two numbers are {divide}."
        print(divide_message)
        return divide_message
        
    
    if test_mode != True:
        play_again = input("Play again? Y/N: ")
        if play_again.upper() == "Y":
            calculator()
        else:
            exit




