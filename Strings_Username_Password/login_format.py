def generate_login(first_name = None, last_name = None, bcit_id = None):
    if first_name == None or last_name == None or bcit_id == None:
        while True:
            first_name = input("Enter your first name: ").capitalize()
            if first_name.isalpha() == False:
                error_message = "Invalid entry. Please enter your first name using all texts and no spaces."
                print(error_message)
                continue
            else:
                break
        
        while True:
            last_name = input("Enter your last name: ").capitalize()
            if last_name.isalpha() == False:
                error_message = "Invalid entry. Please enter your last name using all texts and no spaces."
                print(error_message)
                continue
            else:
                break
        
        while True:
            bcit_id = input("Enter your BCIT ID: ")
            if bcit_id.isdigit() == True:
                error_message = "Invalid entry. Please enter your BCIT ID with the following format (A01339550). "
                print(error_message)
                continue
            else: 
                break 

     
    #generate username
    username = first_name + last_name
    print(username)

    #generate password
    if len(first_name) < 3:
        first_name_pass = first_name
    else:
        first_name_pass = first_name[:3]
    
    if len(last_name) < 3: 
        last_name_pass = last_name
    else: 
        last_name_pass = last_name [:3]

    if len(bcit_id) < 3: 
        bcit_id_pass = bcit_id
    else: 
        bcit_id_pass = bcit_id[-3:]
    
    password = first_name_pass + last_name_pass + bcit_id_pass
    print(password)

    return username, password

def has_upper(entry):
    """Checks if an input string contains at least one uppercase letter.

    :param entry: the input string
    :type entry: str
    :return: True if there is at least one uppercase letter; False otherwise
    :rtype: bool
    """
    for char in entry:
        if char.isupper():
            return True
    return False


def has_lower(entry):
    """Checks if an input string contains at least one lowercase letter.

        :param entry: the input string
        :type entry: str
        :return: True if there is at least one lowercase letter; False otherwise
        :rtype: bool
        """
    for char in entry:
        if char.islower():
            return True
    return False


def has_digit(entry):
    """Checks if an input string contains at least one numeric digit.

        :param entry: the input string
        :type entry: str
        :return: True if there is at least one digit; False otherwise
        :rtype: bool
        """
    for char in entry:
        if char.isdigit():
            return True
    return False

def change_password(new_password = None):
    if new_password == None: 
        while True: 
            new_password = input("Enter a new password: ")
            if len(new_password) < 7: 
                length_error = "Error - password should be at least 7 characters long!"
                print(length_error)
                continue
            elif (not has_upper(new_password)) or (not has_lower(new_password)):
                case_error = "Error - password should contain at least one uppercase and one lowercase character!"
                print(case_error)
                continue
            elif not has_digit(new_password):
                digit_error= "Error - password should contain at least one digit!"
                print(digit_error)
                continue
            else: 
                print(new_password)
                break
    else:
        if len(new_password) < 7:
            return length_error
        elif (not has_upper(new_password)) or (not has_lower(new_password)):
            return case_error
        elif not has_digit(new_password):
            return digit_error
        else:
            return new_password





