#Jonason He 

from os.path import exists
import re


#1
def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    '''
    This function will validate each of the order details, represented by the parameters.

    params: order number
    returns: order number, title, author, isbn, year, quantity, cost
    '''
    #One or more integer values. Note that both 1 and 0001 would be valid
    order_num_rules = re.search("^[0-9]+$", order_num)
    
    #One or more lower or upper case letters or spaces
    title_rules = re.search("^[a-zA-Z ]+$", title)

    #Zero or more lower or upper case letters, spaces or apostrophes
    author_rules = re.search("^[a-zA-Z \']*$", author)

    #Must be between 4 and 20 digits, inclusive
    isbn_rules = re.search("^[0-9]{4,20}$", isbn)

    #Must be 4 digits exactly
    year_rules = re.search("^[1-9]{1}[0-9]{3}$", year)

    #Must be between 0 and 1000, inclusive
    quantity_rules = re.search("^([0-1]{1}|[0-9]{2,3}|1[0]{3})$", quantity)

    #Must be a floating point value with exactly 2 decimal places
    cost_rules = re.search("^[0-9]+\.{1}[0-9]{2}$", cost)

    #Must be integers
    integer_rules_isbn = re.search("^[0-9]+", isbn)

    #Must be integers
    integer_rules_year = re.search("^[0-9]+", year)

    #Must be integers
    integer_rules_quantity = re.search("^[0-9]+", quantity)


    #check if there is any ValueError or TypeError
    if not order_num_rules:
        raise ValueError("Order Number is invalid")
    if not title_rules:
        raise ValueError("Title is invalid")
    if not author_rules:
        raise ValueError("Author is invalid")

    if not integer_rules_isbn:
        raise(TypeError("ISBN must be an integer"))
    elif not isbn_rules:
        raise (ValueError("ISBN is invalid"))

    if not integer_rules_year:
        raise (TypeError("Year must be an integer"))
    elif not year_rules:
        raise(ValueError("Year is invalid"))

    if not integer_rules_quantity:
        raise(TypeError("Quantity must be an integer"))
    
    if not quantity_rules:
        raise(ValueError("Quantity is invalid"))
    
    if not cost_rules:
        raise ValueError("Cost is invalid")
    
    print(order_num, title, author,isbn, year, quantity,cost)
    return order_num, title, author,isbn, year, quantity,cost

#2
def calculate_per_book_cost(cost, quantity):
    '''
    Return a floating point value that is the cost per book in the order 
    (i.e., the cost divided by the quantity). 
    Note that this function will raise a ZeroDivisionError exception 
    (done automatically by Python) when the quantity (i.e., thePage 4 of 6 Sept 2022 denominator) is zero.

    params: quantity
    returns: cost per book
    '''
    if quantity == 0: 
        raise ZeroDivisionError("float division by zero")
    else: 
        cost_formatted = float(cost)
        quantity_formatted = int(quantity)
        per_book_cost = float(cost_formatted/quantity_formatted)
        print(per_book_cost)
        return per_book_cost


#3
def write_book_order_details (filename, order_num, title, author, isbn, year, quantity, cost, unit_cost):
    '''
    This function will create a file with the given filename and write the 
    order details as follows:

    If a file with the provided filename already exists, 
    it should raise a ValueError exception with the message 
    “Order file name already exists!”.
    
    BOOK ORDER
    order_no=
    title=
    author=
    isbn=
    year=
    quantity=
    cost=
    unit_cost=
    Save the values of the parameters after the = signs
    '''
    
    if exists(filename):
        raise ValueError("Order file name already exists!")
        
    else:
        content = f"order_no = {order_num}\ntitle = {title}\nauthor = {author}\nisbn = {isbn}\nyear = {year}\nquantity = {quantity}\ncost = {cost}\nunit_cost = {unit_cost}"

        f = open(filename, "w")
        f.write(content)
        f.close()
    
    print(filename, order_num, title, author, isbn, year, quantity, cost, unit_cost)
    return filename, order_num, title, author, isbn, year, quantity, cost, unit_cost


#4
def test_functions():
    '''
    Test for all functions
    return: whether the functions pass/failed the test
    '''
    # Validate Book Order Details Test
    print("Validate Book Order Details Test")
    book_test = validate_book_order_details("1", "Fire and Blood", "George RR Martin", "12345", "2011", "190", "25.00")
    if book_test == ("1", "Fire and Blood", "George RR Martin", "12345", "2011", "190", "25.00"):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")  
    
    # Calculate Cost Per Book Test
    print("Calculate Cost Per Book Test")
    cost_test = calculate_per_book_cost(20, 5)
    if cost_test == 4:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Book Order Details Test
    print("Book Order Details Test")
    book_details_test = write_book_order_details("game of thrones" ,"0001", "Intro to Python", "Bill Smith", "123456", "2010", "10", "$500.50", "$50.05")
    if book_details_test == ("game of thrones" , "0001", "Intro to Python", "Bill Smith", "123456", "2010", "10", "$500.50", "$50.05"):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

