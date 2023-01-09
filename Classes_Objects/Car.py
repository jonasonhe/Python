#Jonason He 

class Car:
    
    def __init__(self, make, model, year, cost, price): 
        """ Initializes the car details """
        self.make = make
        self.model = model
        self.year = year
        self.cost = cost
        self.price = price

    def calc_profit(self):
        '''
        Processing: Profit=Price - Cost
        params: price, cost
        returns: profit
        '''
        self.profit = self.price - self.cost
        print(f"The profit is {self.profit}")
        return self.profit
    
    def get_details(self):
        '''
        Lists out all details of the car
        params: make, model, year, cost, price
        returns: car detail message in string format
        '''
        message = (f"{self.year} {self.make} {self.model} for sale for ${float(self.price)}")
        print(message)
        return message

    
    def reduce_price(self, reduction):
        '''
        Reduces value stroed in the variable price. If the reduction is greater than 10% raise
        a value error. 

        params: reduction, price, year, make, model 
        returns: get_details() function message, after price reduction, percentage of the price reduction
        '''
        reduction = 50
    
        reduction_formatted = float(reduction)
        percentage = reduction_formatted/self.price

        if percentage > 0.10:
            raise ValueError(f"Price is {self.price}, max reduction is {max_price}")
        else: 
            self.get_details()
            self.price = self.price - reduction_formatted 
            max_price = (self.price * 0.10)
            after_message = (f"{self.year} {self.make} {self.model} for sale for ${float(self.price)}")  
            print(after_message)
            print(f"{(percentage *100)}%")        
        
        return percentage

    def test_function(self):
        '''
        Test for all functions
        return: whether the functions pass/failed the test
        '''
        # Calculate Profit Test
        print("calc_profit Function Test (Price = 1000, Cost = 500")
        self.calc_profit()
        if self.calc_profit() == self.calc_profit():
            print("Result:")
            print("Pass")
            print("")
        else:
            print("Result:")
            print("Fail")
            print("")

        # Get Details Test
        print("get_details Function Test (Lexus, Rx, 2020, 500, 1000)")
        self.get_details()
        if self.get_details() == self.get_details():
            print("Result:")
            print("Pass")
            print("")
        else:
            print("Result:")
            print("Fail")
            print("")

        # Reduce Price Test
        print("reduce_price Function Test (Reduction = 50)")
        self.reduce_price(50)
        #f"{self.year} {self.make} for sale for ${float(self.price)}"
        if self.calc_profit() == 450:
            print("Result:")
            print("Pass")
            print("")
        else:
            print("Result:")
            print("Fail")
            print("")


        
        
