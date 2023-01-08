#Jonason He A01339550

import login
import data_format

def test_function():
    '''
    Test for all functions
    return: whether the functions pass/failed the test
    '''
    # Test Login 1
    print("generate_login (jonason1, he, A0133333)")
    user_pass = login.generate_login("jonason1", "he", "A0133333")
    if user_pass == "Invalid entry. Please enter your first name using all texts and no spaces.":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Login 2
    print("generate_login (jonason, he1, A0133333)")
    user_pass = login.generate_login("jonason", "he1", "A0133333")
    if user_pass == "Invalid entry. Please enter your last name using all texts and no spaces.":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Login 3
    print("generate_login (jonason, he, 0133333)")
    user_pass = login.generate_login("jonason", "he", "0133333")
    if user_pass == "Invalid entry. Please enter your BCIT ID with the following format (A01339550). ":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Login 4
    print("generate_login (jonason, he, A01339550)")
    user_pass = login.generate_login("jonason", "he", "A01339550")
    if user_pass == ("JonasonHe", "JonHe550"):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Test Login 5
    print("generate_login (jo, he, A01339550)")
    user_pass = login.generate_login("jo", "he", "A01339550")
    if user_pass == ("JoHe", "JoHe550"):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Login 6
    print("generate_login (daemon, targaryen, A01339550)")
    user_pass = login.generate_login("Daemon", "Targaryen", "A01339550")
    if user_pass == ("DaemonTargaryen", "DaeTar550"):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Login 7
    print("generate_login (daemon, targaryen, A0)")
    user_pass = login.generate_login("Daemon", "Targaryen", "A0")
    if user_pass == ("DaemonTargaryen", "DaeTarA0"):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Change Password 1
    print("Change Password (12345)")
    change_pass = login.change_password("12345")
    if change_pass == "Error - password should be at least 7 characters long!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Change Password 2
    print("Change Password (1234567)")
    change_pass = login.change_password("1234567")
    if change_pass == "Error - password should contain at least one uppercase and one lowercase character!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Change Password 3
    print("Change Password (Gameofthrones)")
    change_pass = login.change_password("Gameofthrones")
    if change_pass == "Error - password should contain at least one digit!":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    # Test Change Password 4
    print("Change Password (Houseofthedragon1)")
    change_pass = login.change_password("Houseofthedragon1")
    if change_pass == "Houseofthedragon1":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Test Book Info 1
    print("Get Book Info (house of the dragon, 12345, martin, hbo, 1996, 30)")
    book_info = data_format.get_book_info("house of the dragon", "12345", "martin", "hbo", "1996", 30)
    if book_info == "house of the dragon/12345/martin/hbo/1996/30.00":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Test CSV Function 1
    print("Convert to CSV (house of the dragon/12345/martin/hbo/1996/30.00)")
    book_csv = data_format.convert_to_csv_format("house of the dragon/12345/martin/hbo/1996/30.00")
    if book_csv == "house of the dragon,12345,martin,hbo,1996,30.00":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Test JSON Function 1
    print("Conver to JSON (house of the dragon,12345,martin,hbo,1996,30.00)")
    book_json = data_format.convert_to_json_format("house of the dragon,12345,martin,hbo,1996,30.00")
    if book_json == '''{"book_title":"house of the dragon","book_isbn":"12345","book_author":"martin","book_publisher":"hbo","year_published":"1996","book_price":"30.00"}''':
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    

    



   