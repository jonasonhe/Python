# Jonason He 

import Test_Tuples_List

# data
countries_and_capitals = (
['Afghanistan', 'Kabul'], ['Albania', 'Tirana (Tirane)'], ['Algeria', 'Algiers'], ['Andorra', 'Andorra la Vella'],
['Angola', 'Luanda'], ['Antigua and Barbuda', "Saint John's"], ['Argentina', 'Buenos Aires'], ['Armenia', 'Yerevan'],
['Australia', 'Canberra'], ['Austria', 'Vienna'], ['Azerbaijan', 'Baku'], ['Bahamas', 'Nassau'], ['Bahrain', 'Manama'],
['Bangladesh', 'Dhaka'], ['Barbados', 'Bridgetown'], ['Belarus', 'Minsk'], ['Belgium', 'Brussels'],
['Belize', 'Belmopan'], ['Benin', 'Porto Novo'], ['Bhutan', 'Thimphu'], ['Bolivia', 'Sucre'],
['Bosnia and Herzegovina', 'Sarajevo'], ['Botswana', 'Gaborone'], ['Brazil', 'Brasilia'],
['Brunei', 'Bandar Seri Begawan'], ['Bulgaria', 'Sofia'], ['Burkina Faso', 'Ouagadougou'], ['Burundi', 'Gitega'],
['Cambodia', 'Phnom Penh'], ['Cameroon', 'Yaounde'], ['Canada', 'Ottawa'], ['Cape Verde', 'Praia'],
['Central African Republic', 'Bangui'], ['Chad', "N'Djamena"], ['Chile', 'Santiago'], ['China', 'Beijing'],
['Colombia', 'Bogota'], ['Comoros', 'Moroni'], ['Congo, Democratic Republic of the', 'Kinshasa'],
['Congo, Republic of the', 'Brazzaville'], ['Costa Rica', 'San Jose'], ["CÃ´te d'Ivoire (Ivory Coast)", 'Yamoussoukro'],
['Croatia', 'Zagreb'], ['Cuba', 'Havana'], ['Cyprus', 'Nicosia'], ['Czech Republic (Czechia)', 'Prague'],
['Denmark', 'Copenhagen'], ['Djibouti', 'Djibouti'], ['Dominica', 'Roseau'], ['Dominican Republic', 'Santo Domingo'],
['East Timor', 'Dili'], ['Ecuador', 'Quito'], ['Egypt', 'Cairo'], ['El Salvador', 'San Salvador'],
['England', 'London'], ['Equatorial Guinea', 'Malabo'], ['Eritrea', 'Asmara'], ['Estonia', 'Tallinn'],
['Eswatini (Swaziland)', 'Mbabana'], ['Ethiopia', 'Addis Ababa'], ['Federated States of Micronesia', 'Palikir'],
['Fiji', 'Suva'], ['Finland', 'Helsinki'], ['France', 'Paris'], ['Gabon', 'Libreville'], ['Gambia', 'Banjul'],
['Georgia', 'Tbilisi'], ['Germany', 'Berlin'], ['Ghana', 'Accra'], ['Greece', 'Athens'], ['Grenada', "Saint George's"],
['Guatemala', 'Guatemala City'], ['Guinea', 'Conakry'], ['Guinea-Bissau', 'Bissau'], ['Guyana', 'Georgetown'],
['Haiti', 'Port au Prince'], ['Honduras', 'Tegucigalpa'], ['Hungary', 'Budapest'], ['Iceland', 'Reykjavik'],
['India', 'New Delhi'], ['Indonesia', 'Jakarta'], ['Iran', 'Tehran'], ['Iraq', 'Baghdad'], ['Ireland', 'Dublin'],
['Israel', 'Jerusalem'], ['Italy', 'Rome'], ['Jamaica', 'Kingston'], ['Japan', 'Tokyo'], ['Jordan', 'Amman'],
['Kazakhstan', 'Nur-Sultan'], ['Kenya', 'Nairobi'], ['Kiribati', 'Tarawa Atoll'], ['Kosovo', 'Pristina'],
['Kuwait', 'Kuwait City'], ['Kyrgyzstan', 'Bishkek'], ['Laos', 'Vientiane'], ['Latvia', 'Riga'], ['Lebanon', 'Beirut'],
['Lesotho', 'Maseru'], ['Liberia', 'Monrovia'], ['Libya', 'Tripoli'], ['Liechtenstein', 'Vaduz'],
['Lithuania', 'Vilnius'], ['Luxembourg', 'Luxembourg'], ['Madagascar', 'Antananarivo'], ['Malawi', 'Lilongwe'],
['Malaysia', 'Kuala Lumpur'], ['Maldives', 'Male'], ['Mali', 'Bamako'], ['Malta', 'Valletta'],
['Marshall Islands', 'Majuro'], ['Mauritania', 'Nouakchott'], ['Mauritius', 'Port Louis'], ['Mexico', 'Mexico City'],
['Moldova', 'Chisinau'], ['Monaco', 'Monaco'], ['Mongolia', 'Ulaanbaatar'], ['Montenegro', 'Podgorica'],
['Morocco', 'Rabat'], ['Mozambique', 'Maputo'], ['Myanmar (Burma)', 'Nay Pyi Taw'], ['Namibia', 'Windhoek'],
['Nauru', 'No official capital'], ['Nepal', 'Kathmandu'], ['Netherlands', 'Amsterdam'], ['New Zealand', 'Wellington'],
['Nicaragua', 'Managua'], ['Niger', 'Niamey'], ['Nigeria', 'Abuja'], ['North Korea', 'Pyongyang'],
['North Macedonia (Macedonia)', 'Skopje'], ['Northern Ireland', 'Belfast'], ['Norway', 'Oslo'], ['Oman', 'Muscat'],
['Pakistan', 'Islamabad'], ['Palau', 'Melekeok'], ['Panama', 'Panama City'], ['Papua New Guinea', 'Port Moresby'],
['Paraguay', 'Asuncion'], ['Peru', 'Lima'], ['Philippines', 'Manila'], ['Poland', 'Warsaw'], ['Portugal', 'Lisbon'],
['Qatar', 'Doha'], ['Romania', 'Bucharest'], ['Russia', 'Moscow'], ['Rwanda', 'Kigali'],
['Saint Kitts and Nevis', 'Basseterre'], ['Saint Lucia', 'Castries'], ['Saint Vincent and the Grenadines', 'Kingstown'],
['Samoa', 'Apia'], ['San Marino', 'San Marino'], ['Sao Tome and Principe', 'Sao Tome'], ['Saudi Arabia', 'Riyadh'],
['Scotland', 'Edinburgh'], ['Senegal', 'Dakar'], ['Serbia', 'Belgrade'], ['Seychelles', 'Victoria'],
['Sierra Leone', 'Freetown'], ['Singapore', 'Singapore'], ['Slovakia', 'Bratislava'], ['Slovenia', 'Ljubljana'],
['Solomon Islands', 'Honiara'], ['Somalia', 'Mogadishu'], ['South Africa', 'Pretoria, Bloemfontein, Cape Town'],
['South Korea', 'Seoul'], ['South Sudan', 'Juba'], ['Spain', 'Madrid'], ['Sri Lanka', 'Colombo'], ['Sudan', 'Khartoum'],
['Suriname', 'Paramaribo'], ['Sweden', 'Stockholm'], ['Switzerland', 'Bern'], ['Syria', 'Damascus'],
['Taiwan', 'Taipei'], ['Tajikistan', 'Dushanbe'], ['Tanzania', 'Dodoma'], ['Thailand', 'Bangkok'], ['Togo', 'Lome'],
['Tonga', "Nuku'alofa"], ['Trinidad and Tobago', 'Port of Spain'], ['Tunisia', 'Tunis'], ['Turkey', 'Ankara'],
['Turkmenistan', 'Ashgabat'], ['Tuvalu', 'Funafuti'], ['Uganda', 'Kampala'], ['Ukraine', 'Kiev'],
['United Arab Emirates', 'Abu Dhabi'], ['United Kingdom', 'London'], ['United States', 'Washington D.C.'],
['Uruguay', 'Montevideo'], ['Uzbekistan', 'Tashkent'], ['Vanuatu', 'Port Vila'], ['Vatican City', 'Vatican City'],
['Venezuela', 'Caracas'], ['Vietnam', 'Hanoi'], ['Wales', 'Cardiff'], ['Yemen', "Sana'a"], ['Zambia', 'Lusaka'],
['Zimbabwe', 'Harare'])

countries = (
'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "CÃ´te d'Ivoire (Ivory Coast)",
'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea', 'Eritrea', 'Estonia',
'Eswatini (Swaziland)', 'Ethiopia', 'Federated States of Micronesia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica',
'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon',
'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia',
'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia',
'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia (Macedonia)', 'Northern Ireland', 'Norway', 'Oman',
'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan',
'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania',
'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
'Venezuela', 'Vietnam', 'Wales', 'Yemen', 'Zambia', 'Zimbabwe')

capitals = (
'Kabul', 'Tirana (Tirane)', 'Algiers', 'Andorra la Vella', 'Luanda', "Saint John's", 'Buenos Aires', 'Yerevan',
'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan', 'Porto Novo',
'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasilia', 'Bandar Seri Begawan', 'Sofia', 'Ouagadougou', 'Gitega',
'Phnom Penh', 'Yaounde', 'Ottawa', 'Praia', 'Bangui', "N'Djamena", 'Santiago', 'Beijing', 'Bogota', 'Moroni',
'Kinshasa', 'Brazzaville', 'San Jose', 'Yamoussoukro', 'Zagreb', 'Havana', 'Nicosia', 'Prague', 'Copenhagen',
'Djibouti', 'Roseau', 'Santo Domingo', 'Dili', 'Quito', 'Cairo', 'San Salvador', 'London', 'Malabo', 'Asmara',
'Tallinn', 'Mbabana', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki', 'Paris', 'Libreville', 'Banjul', 'Tbilisi',
'Berlin', 'Accra', 'Athens', "Saint George's", 'Guatemala City', 'Conakry', 'Bissau', 'Georgetown', 'Port au Prince',
'Tegucigalpa', 'Budapest', 'Reykjavik', 'New Delhi', 'Jakarta', 'Tehran', 'Baghdad', 'Dublin', 'Jerusalem', 'Rome',
'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa Atoll', 'Pristina', 'Kuwait City', 'Bishkek',
'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli', 'Vaduz', 'Vilnius', 'Luxembourg', 'Antananarivo',
'Lilongwe', 'Kuala Lumpur', 'Male', 'Bamako', 'Valletta', 'Majuro', 'Nouakchott', 'Port Louis', 'Mexico City',
'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica', 'Rabat', 'Maputo', 'Nay Pyi Taw', 'Windhoek', 'No official capital',
'Kathmandu', 'Amsterdam', 'Wellington', 'Managua', 'Niamey', 'Abuja', 'Pyongyang', 'Skopje', 'Belfast', 'Oslo',
'Muscat', 'Islamabad', 'Melekeok', 'Panama City', 'Port Moresby', 'Asuncion', 'Lima', 'Manila', 'Warsaw', 'Lisbon',
'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre', 'Castries', 'Kingstown', 'Apia', 'San Marino', 'Sao Tome',
'Riyadh', 'Edinburgh', 'Dakar', 'Belgrade', 'Victoria', 'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara',
'Mogadishu', 'Pretoria, Bloemfontein, Cape Town', 'Seoul', 'Juba', 'Madrid', 'Colombo', 'Khartoum', 'Paramaribo',
'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma', 'Bangkok', 'Lome', "Nuku'alofa", 'Port of Spain',
'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala', 'Kiev', 'Abu Dhabi', 'London', 'Washington D.C.', 'Montevideo',
'Tashkent', 'Port Vila', 'Vatican City', 'Caracas', 'Hanoi', 'Cardiff', "Sana'a", 'Lusaka', 'Harare')


# 1
def how_many_countries():
    '''
    Counts the number of countries in the countries tupple
    
    params: country tuple
    type: tuple
    returns: number of countries
    rtype: int
    '''
    print(len(countries))
    return len(countries)


# 2
def get_name_of_longest_country():
    '''
    Returns the longest string in the countries tuple
    
    params: country tuple
    type: tuple
    returns: the longest string in the tuple
    rtype: str
    '''
    print(max(countries, key=len))
    return (max(countries, key=len))


# 3
def get_number_of_capitals_containing(substring = None):
    '''
    Returns the number of capitals containing a string or subset of a string in the capital tuple
    
    params: user input
    type: string
    returns: number of capitals containing a string or subset of a string 
    rtype: int
    '''
    if substring == None:
        while True:
            substring = input("Enter a string to search for a capital: ").lower()
            if substring == "":
                print("Please enter something:")
                continue
            elif substring.isdigit() == True: 
                print("Please enter a non-numeric text")
                continue
            else:
                break
    else:
        if substring == "":
            return ("Please enter something:")
        elif substring.isdigit() == True: 
            return print("Please enter a non-numeric text")

    total = 0
    for capital in capitals:
        if substring in capital.lower():
            print(total, end = " ")
            total = total + 1
    return total


# 4
def get_capital_of(capital = None):
    '''
    Gets the capital of a country from the country capital tuple list
    
    params: country name
    type: str
    returns: capital 
    rtype: str
    '''
    if capital == None:
        while True:
            capital = input("Please enter a country name: ")
            if capital.isdigit() == True:
                print("Please enter the capital without any numbers: ")
                continue
            else:
                break
    else:
        if capital.isdigit() == True:
            return "Please enter the capital without any numbers: "

    

    for country_capital in countries_and_capitals:
            if country_capital[0].lower() == capital.lower():
                print(country_capital[1])
                return country_capital[1]
    return None       

# 5
def get_list_of_countries_with_this_many_letters_in_name(num_letters=None):
    '''
    Gets the user to enter a number and returns a list of countires with the 
    same number of characters.
    
    params: number of letters
    type: str
    returns countries in a list format
    rtype: list
    '''
    if num_letters == None:
        while True:
            num_letters = input(
                "Enter a number to print out a list of countries with the same number of characters as you inputted: ")
            if num_letters.isdigit() == False:
                print("Please enter a numerical value: ")
                continue
            else:
                break
    else:
        if num_letters.isdigit() == False:
            return "Please enter a numerical value: "

    num_letters = int(num_letters)

    country_list = []
    for country in countries:
        if num_letters == len(country):
            country_list.append(country)
            print(country)
    return country_list

#6
def get_num_countries_and_capitals_that_begin_with_same_letter():
    '''
    gets the total number of capitals and countries that begin with the same name
    returns integer
    
    params: country capital tuple list
    type: tuple list
    returns total number of capitals and countries that begin with the same name
    type: int
    '''

    num_countries_capitals = 0
    # loop all list items
    for country_capital in countries_and_capitals:
       if country_capital[0][0] == country_capital[1][0]:
           print(num_countries_capitals)
           num_countries_capitals = num_countries_capitals + 1
    return num_countries_capitals

#for loop will go through each item in the tuple ex. 1 item [Afganistan, Kabal],
# so if put [0][0] it will search for the first 1 in the list afganistan
# and then the first letter in the first item which is A
# Then [1][0] it will search for the second item in the list which will search for kabal and then find the first letter of the second item which is K

#7
def get_countries_and_capitals_that_begin_with_same_letter():
    '''
    Check each pair of country and capital
    to see if they have the same starting letter,
    and return a list of the capitals and countries
    that are the same
    
    params: country capital tuple list
    type: tuple list 
    return: list of the capitals and countries
    rtype: list
    '''
    # Create list
    countries_capitals = []
    # loop all list items
    for country_capital in countries_and_capitals:
        # Check each country and capital for same starting letter
        if country_capital[0][0] == country_capital[1][0]:
            # Add capital and country (as a string) to list
            countries_capitals.append(f"{country_capital[1]} - {country_capital[0]}")
            print(countries_capitals)
    # Return list
    return countries_capitals

#8
def print_countries_in_reverse_alphabetical_order():
    '''
    prints out the countries in reverse alphabetical order
    
    params: countries tuple
    type: tuple
    returns: list of countries printed in reverse alphapetical order 
    rtype: list
    '''
    counter = len(countries)
    reverse_countries = []
    while counter > 0: #starts from the bottom to the top which is 200
        reverse_countries.append(countries[counter-1]) #add a country from the bottom of the list, everytime u add a country, you are subtracting 1
        counter = counter - 1                          # (i.e 200-1 = 199, then the loop starts so 199 - 1. The counter = counter - 1 will go until its 2-1 = 1.
    print(reverse_countries)                           # Then when it hits 1-0 = 0 it will invalidate the while counter > 0 and it will stop the loop.
    return reverse_countries                           # Then you would just print the list reverse_countires


def main():
    '''
    User testing menu to test all functions
    returns: Function test and returns pass/fail for each function
    '''
    string_menu = '''
    =============================
    Choose an option or 0 to exit
    --------------------------------------------
    [1] How many countries?
    [2] What is the longest country name?
    [3] Get number of capitals containing substring
    [4] Get capital of country
    [5] Print countries in reverse order
    [6] Test Functions
    [0] Exit
    ============================

    '''
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
                print("[1] How many countries?")
                number_country = how_many_countries()

            elif choice == 2:
                print("-----------------------------")
                print("[2] What is the longest country name?")
                longest_country_name = get_name_of_longest_country()

            elif choice == 3:
                print("-----------------------------")
                print("[3] Get number of capitals containing substring")
                capital_containing = get_number_of_capitals_containing()

            elif choice == 4:
                print("-----------------------------")
                print("[4] Get capital of country")
                capital_of = get_capital_of()

            elif choice == 5:
                print("-----------------------------")
                print("[5] Print countries in reverse order")
                reverse = print_countries_in_reverse_alphabetical_order()

            elif choice == 6:
                print("-----------------------------")
                print("[6] Test Functions")
                function_test = Lab5Test.test_function()

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
