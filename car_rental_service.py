class RentalVehicle:
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
        self.seats = seats

    def display_cost(self,days):
        total_cost = self.calculate_rental_cost(days)
        print(f"Rental cost for {self.brand} {self.model} for {days} days is ${total_cost}")

    def display_vehicle_info(self):
        # super().display_vehicle_info()
        print(f"Car: {self.brand} {self.model}, Year :{self.year}"
              f" , Seats: {self.seats}, Rental price: ${self.get_rental_price_per_day()}/day")
        
       
class Bike(RentalVehicle):
    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity):
        super().__init__(brand,model,year,rental_price_per_day)
        self.engine_capacity = engine_capacity
    def display_cost(self,days):
        total_cost = self.calculate_rental_cost(days)
        print(f"Rental cost for {self.brand} {self.model} for {days} days is ${total_cost}")
    def display_vehicle_info(self):
        print(f"Bike: {self.brand} {self.model}, Year :{self.year}"
              f" , Engine: {self.engine_capacity}, Rental price: ${self.get_rental_price_per_day()}/day")
        
        #show polymorphism
def show_vehicle_info(vehicle):
    vehicle.display_vehicle_info()


car=Car("Toyota","Corolla",2020,50,3)
bike=Bike("Yamaha ","R1", 2019,30,"998cc")
show_vehicle_info(car)
show_vehicle_info(bike)
print()
car.display_cost(3)
bike.display_cost(5)

car.set_rental_price_per_day(55)
print(f"Updated rental price for {car.brand} {car.model}: ${car.get_rental_price_per_day()}/day")