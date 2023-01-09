#Jonason He 
import re

import json

#global variable in json format
car_list = [
{"make": "BMW","model": "328","year": 2020, "license" : "ARH100" }, {"make": "Toyota", "model": "Camry", "year": 2016, "license" : "GHT456"}]

def load_data():
    '''function to return a list 
    of all data read from cars.txt file in list format'''

    # opening file in read mode
    cars = open("cars.txt")

    # creating an empty car list
    car_list = []

    # loading json data
    data = json.load(cars)

    # loading data into list
    for i in data:
        car = {"make": i["make"], "model": i["model"],
               "year": i["year"], "license": i["license"]}
        car_list.append(car)

    # closing file
    cars.close()
    return car_list


def write_data(car_list):
    '''Function to write data to json file 
    by accepting a list of car details'''

    cars = open("cars.txt", "w")
    # dumping data to file
    json.dump(car_list, cars, indent=4)
    cars.close()  # closing file


#Add a car
def add_car(make = None, model = None, year = None, license = None):
    '''
    Adds a car/details to the cars.txt json formatted parking lot. Provides validation error
    which does not allow for a car to be added that has the same license plate as one already 
    within the parking lot

    params: make, model, year, license
    returns: True/False
    '''
    if make is None or model is None or year is None: 
        #user inputs for string values regex all uppercase and 
        #lowercase, lettters, numbers, and spaces
        make = input("Please enter the make of the car: ")
        if not re.fullmatch("[a-z0-9A-Z\s]+", make):
            raise ValueError("The make is invalid")
        model = input("Please enter the model of the car: ")
        if not re.fullmatch("[a-z0-9A-Z\s]+", model):
            raise ValueError("The model is invalid")
        year = input("Please enter a year of the car: ")
        if not re.fullmatch("^19[0-9][0-9]|^20[0-1][0-9]|202[0-9]$", year):
           raise ValueError("The Year is invalid")        
        license = input("Please enter the liscense plate of the car: ")
        if not re.fullmatch("[a-z0-9A-Z]+", license):
            raise ValueError("The License is invalid")

    year_formatted = int(year)
    license_formatted = license.upper()

    #check if license exists in the list dictionary
    if any(dictionary['license'] == license
        for dictionary in car_list):
        # 👇️ this runs
        print("Car already exists in the Parking Lot")
        return False
    else: 
        #add the car details to the list
        new_dict = {"make": make, "model": model, "year": year_formatted, "license" : license_formatted}
        car_list.append(new_dict)  # appending to list
        write_data(car_list)  # writing to json file
        print("Car details added successfully")
        return True 
    
    

#display the list of cars in the parking lot
def display_cars_parking_lot():
    '''
    Displays all the cars and their details in the parking lot

    params: None
    returns: parking lot details 
    '''
    for car in car_list:
        message = (car["year"], car["make"], car["model"],
                      "with license plate", car["license"])
        print(message)

    return True

#find a display a car based on the license plate number
def display_cars_license_plate_number(license = None):
    '''
    Finds the car/details in the current parking based on its license plate which 
    is entered by the user. The match can be partial such as ARH can match with ARH100. 
    User input is not affected by case sensitivity

    params: user inputted license plate
    returns: car details that matches license plate entered
    '''
    if license == None:
        while True: 
            license = input("Enter a license plate to find a car (ARH or ARH100): ")
            break

    license_formatted = license.upper()
    
    count = 0
    for car in car_list: 
        if car["license"].startswith(license_formatted):
            message = [car["year"], car["make"], car["model"],
                      "with license plate", car["license"]]
            print(message)
            count = count + 1 
            return True
        
    
    if count == 0:
        print("No car found")
        return False
        

#remove a car from the parking lot based on the license plate number
def remove_car(license = None):
    '''
    Remove a car from the parking lot by License. 
    This should remove the car with the License entered by the user. 
    The match on License must be exact.

    params: user inputted license plate
    returns: car details of the car being removed that matches license plate entered
    '''
    if license == None: 
        while True: 
            license = input("Enter a license plate to remove a car from the list (license plate must match exactly): ")
            break

    license_formatted = license.upper()

    count = 0
    for car in car_list:
        if license_formatted in car["license"]:
            message = [car["year"], car["make"], car["model"],
                      "with license plate", car["license"]]
            print(message)
            car_list.remove(car)
            write_data(car_list)
            count = count + 1
            return True
                
    
    if count == 0: 
        print("No car found")
        return False
        
    
#menu
def main():
    '''
    User testing menu to test all functions
    returns: Function test and returns pass/fail for each function
    '''
    string_menu = '''
    =============================
    Choose an option or 0 to exit
    -----------------------------
    [1] Add a Car to the parking lot
    [2] Display the list of cars in the parking lot
    [3] Find and display a car based on the license plate number
    [4] Remove a car from the parking lot based on the license plate number
    [0] Exit
    =============================
    '''
    repeat = True
    while repeat:
        while True:
            print(string_menu)
            while True:
                try:
                    choice = int(input("Enter your option from 0-4: "))
                    if choice < 0 or choice > 4:
                        continue
                    break
                except:
                    continue

            if choice == 1:
                print("-----------------------------")
                print("Running function [1] Add a Car to the parking lot")
                try:
                    load = load_data()
                    add = add_car()
                except ValueError as ve:
                    print("Value Error:", ve)

            elif choice == 2:
                print("-----------------------------")
                print("Running function [2] Display the list of cars in the parking lot")
                display = display_cars_parking_lot()
                

            elif choice == 3:
                print("-----------------------------")
                print("Running function [3] Find and display a car based on the license plate number")
                plate = display_cars_license_plate_number()
                
                

            elif choice == 4:
                print("-----------------------------")
                print("Running function [4] Remove a car from the parking lot based on the license plate number")
                remove = remove_car()
        

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