class Vehicle:
    def __init__(self, make, model):
        self.make = make     
        self.model = model
        self.__engine_status = "Off" 
    
    def start_engine(self):
        self.__engine_status = "On"
        print(f"{self.make} {self.model}'s engine started.")
    
    def stop_engine(self):
        self.__engine_status = "Off"
        print(f"{self.make} {self.model}'s engine stopped.")
    
    def describe(self):
        return f"Vehicle: {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    
    def describe(self):
        return f"Car: {self.make} {self.model}, Doors: {self.num_doors}"


class Bike(Vehicle):
    def __init__(self, make, model, has_sidecar=False):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar
    
  
    def describe(self):
        sidecar_info = "with Sidecar" if self.has_sidecar else "without Sidecar"
        return f"Bike: {self.make} {self.model}, {sidecar_info}"


car = Car("Toyota", "bzx", 4)
bike = Bike("Davidson", "s750", has_sidecar=True)

print(car.describe())  
print(bike.describe()) 

car.start_engine()
bike.start_engine() 
