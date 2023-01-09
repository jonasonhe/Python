#Jonason He 

import Car

def main():
    '''
    User testing menu to test all functions
    returns: Function test and returns pass/fail for each function
    '''
    string_menu = '''
    =============================
    Choose an option or 0 to exit
    -----------------------------
    [1] Create the car object
    [2] List the car's details
    [3] Display the car's profit
    [4] Reduce the car's price
    [5] Delete the car object
    [6] Test - create car1 and car2
    [0] Exit
    =============================
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
                print("Running function [1] Create the car object")
                car1 = Car.Car("Honda", "Civic", 2020, 500, 1000)
                print("Car object for class Car has been created.")
                

            elif choice == 2:
                print("-----------------------------")
                print("Running function [2] List the car's details")
                car1.get_details()


            elif choice == 3:
                print("-----------------------------")
                print("Running function [3] Display the car's profit")
                car1.calc_profit()

            elif choice == 4:
                print("-----------------------------")
                print("Running function [4] Reduce the car's price")
                car1.reduce_price(50)

            elif choice == 5:
                print("-----------------------------")
                print("Running function [5] Delete the car object")
                del car1

            elif choice == 6:
                print("-----------------------------")
                print("Running function [6] Test – create car1")
                car1 = Car.Car("Lexus", "Rx", 2020, 500, 1000)
                car1.test_function()
                

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