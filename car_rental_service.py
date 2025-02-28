class RentalVehicle():
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

    def set_rental_price_per_day(self,rental_price_per_day):
        self.__rental_price_per_day = rental_price_per_day

    def calculate_rental_cost(self,days):
        return self.__rental_price_per_day * days
    
    def display_vehicle_info(self):
        print(f"Brand : {self.brand}, Model : {self.model} , Year : {self.year}"
              f" , Rental price : ${self.__rental_price_per_day}/day")    
        

class Car(RentalVehicle):
    def __init__(self,brand,model,year,rental_price_per_day,seats):
        super().__init__(brand,model,year,rental_price_per_day)
        self.seats = 

    def display_cost(self,days):
        total_cost = self.calculate_rental_cost(days)
        print(f"Rental cost for {self.brand} {self.model} for {days} days is ${total_cost}")
