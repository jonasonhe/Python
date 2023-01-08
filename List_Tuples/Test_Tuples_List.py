#Jonason He

import Tuples_List_Functions_Menu

def test_function():
    '''
    Test function
    '''
    # How many Countries Test
    print("Number of Countries Test ()")
    number_country = Lab5.how_many_countries()
    if number_country == 200:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    print("Longest Country Test ()")
    longest_country = Lab5.get_name_of_longest_country()
    if longest_country == "Congo, Democratic Republic of the":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    print("Number of Capitals Containing Test (e)")
    capitals_containing = Lab5.get_number_of_capitals_containing("e")
    if capitals_containing == 75:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Number of Capitals Containing Test (z)")
    capitals_containing = Lab5.get_number_of_capitals_containing("z")
    if capitals_containing == 3:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    print("Number of Capitals Containing Test (')")
    capitals_containing = Lab5.get_number_of_capitals_containing("'")
    if capitals_containing == 5:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    
    print("Number of Capitals Containing Test (an)")
    capitals_containing = Lab5.get_number_of_capitals_containing("an")
    if capitals_containing == 35:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    print("Countries and Capitals that Begin with the Same Letter Test ()")
    same_letter = Lab5.get_num_countries_and_capitals_that_begin_with_same_letter()
    if same_letter == 29:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("Countries and Capitals that begin with the Same Letter Test ()")
    same_letter_list = Lab5.get_countries_and_capitals_that_begin_with_same_letter()
    print(same_letter_list)

    print("Capital of Country Test (canada)")
    capital_country = Lab5.get_capital_of("canada")
    if capital_country == "Ottawa":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    print("Capital of Country Test (nEW zeALAND))")
    capital_country = Lab5.get_capital_of("nEW zeALAND")
    if capital_country == "Wellington":
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")
    
    print("Capital of Country Test (xyz)")
    capital_country = Lab5.get_capital_of("xyz")
    if capital_country == None:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

    print("List of Countries with many Letters in Name Test (11)")
    list_country = Lab5.get_list_of_countries_with_this_many_letters_in_name("11")
    if list_country == ['Afghanistan', 'El Salvador', 'Netherlands', 'New Zealand', 'North Korea', 'Philippines', 'Saint Lucia', 'South Korea', 'South Sudan', 'Switzerland']:
        print("Pass")
        print("")
    else:
        print("Fail")
        print("")

def main():
    test = test_function()

if __name__ == "__main__":
    main()