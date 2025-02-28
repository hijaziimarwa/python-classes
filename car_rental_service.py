class RentalVehicle():
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def display_vehicle_info(self):
        print(f"Brand : {self.brand}, Model : {self.model} , Year : {self.year}"
              f" , Rental price : ${self.__rental_price_per_day}/day")    