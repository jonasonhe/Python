#Jonason He 

dict_prov_teritories = {"Alberta": "Edmonton", "British Columbia": "Victoria", "Manitoba": "Winnipeg", "New Brunswick": "Fredericton", "Newfoundland and Labrador": "St. John's", "Nova Scotia": "Halifax", "Ontario": "Toronto", "Prince Edward Island": "Charlottetown", "Quebec": "Quebec City", "Saskatchewan": "Regina", "Yukon": "Whitehorse", "Nunavut": "Iqaluit", "Northwest Territories": "Yellowknife"}

def display_all(input_dict = dict_prov_teritories):
    '''
    Prints out each capital city of each province within the dictionary "dict_prov_teritories"
    
    :param substring: None
    :type substring: string
    :return: string of all the capital city of each province
    :rtype: string 
    '''

    lst = list(input_dict.items())

    for key, value in input_dict.items():
        result_string = f"{value} is the capital city of {key}"
        print(result_string)

    count = len(lst)
    return count

def get_capital_city(province_name = None, input_dict = dict_prov_teritories):
    '''
    Asks the user to enter a province name from the existing dictionary "dict_prov_teritories". prints out the capital city of the province entered
    
    :param substring: string 
    :type substring: string
    :return: capital city of the province in a string
    :rtype: string 
    '''
    if province_name == None:
        while True: 
            province_name = (input("Enter a Canadian province:").title())
            if province_name not in input_dict:
                print("Error - Province name is not in this dictionary")
                continue
            else: 
                break

    province_name
    capital_city = input_dict[province_name]
    print(capital_city)
    return capital_city




def add_item(province_name = None, capital_city = None, input_dict = dict_prov_teritories):
    '''
    Asks the user to enter a new province and capital city. Adds the new key and value to the existing dictionary "dict_prov_teritories"
    
    :param substring: string, string
    :type substring: string
    :return: before and after number of elements within the dictionary from the user input 
    :rtype: string 
    '''
    if province_name == None: 
        while True: 
            province_name = (input("Enter a province: ").title())
            if province_name.isdigit == True:
                print("Error - province cannot contain any numbers")
                continue
            else: 
                break
    if capital_city == None: 
        while True: 
            capital_city = (input("Enter the capital city of the province: ").title())
            if capital_city.isdigit == True: 
                print("Error - capital city cannot contain any numbers")
                continue
            else:
                break


    before_numb_of_elements = len(input_dict)


    input_dict[province_name] = capital_city
    after_numb_of_elements = len(input_dict)

    
    before_after = f"Before {before_numb_of_elements} elements, after {after_numb_of_elements} elements"
    print(before_after)

    return before_after



def remove_item(province_name = None, input_dict = dict_prov_teritories):
    '''
    Aks the user to enter a province. Removes the province and caital city associated with that province from the dictionary "dict_prov_teritories". Provides
    input validation to check if the entered province exists in the dictionary
    
    :param substring: string
    :type substring: string
    :return: before and after number of elements within the dictionary from the user input 
    :rtype: string 
    '''
    if province_name == None:
        while True:
            province_name = (input("Enter a province: ").title())
            if province_name not in input_dict:
                print("Please enter a Canadian Province Name within the given dictionary: ")
                continue
            else: 
                break

    before_numb_of_elements = len(input_dict)


    del input_dict[province_name]
    after_numb_of_elements = len(input_dict)

    
    before_after = f"Before {before_numb_of_elements} elements, after {after_numb_of_elements} elements"
    print(before_after)

    return before_after

def test_function_dict():
    '''
    Test for all functions
    return: whether the functions pass/failed the test
    '''
    # display_all Test
    print("Display All Test(Dictionary Provinces and Territories)")
    cap_city_province = display_all()
    if cap_city_province == 13:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Get Capital City Test
    print("Get Capital City Test(Alberta)")
    capital_test = get_capital_city("Alberta")
    if capital_test == "Edmonton":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Get Add Item Test
    print("Add Item Test (Seattle, Washington)")
    add_dict = add_item("Seattle", "Washington")
    if add_dict == ("Before 13 elements, after 14 elements"):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    # Get Remove Item Test
    print("Remove Item (Seattle))")
    add_dict = remove_item("Seattle")
    if add_dict == ("Before 14 elements, after 13 elements"):
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")



              

    