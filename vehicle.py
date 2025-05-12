
class Vehicule:
    def __init__(self, type):
        self.type = type

    def move(self, movement):
        return f"{self.type} {movement}"
    
    def accelerating():
        pass
    

class Car(Vehicule):
    wheels = 4
    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make
        super().__init__(type="Car")


class Plane(Vehicule):
    engines = 2
    def __init__(self, manufacturer,aircraft_type, color, company):
        self.manufacturer = manufacturer
        self.aircrafttype = aircraft_type
        self.color = color
        self.company = company
        super().__init__(type="Plane")

class Train(Vehicule):
    def __init__(self, engine_type,max_speed, country):
        self.engine_type = engine_type
        self.max_speed = max_speed
        self.country = country


class Motorbike(Vehicule):
    wheels = 2
    def __init__(self, manufacturer,model, ):
        self.manufacturer = manufacturer
        self.model = model



#cars
toyota = Car('Prado', 2020, "Toyota")
print(toyota.type)

#planes
boeing_737 = Plane("Boeing","Commercial", "White", "Aircanada")
print(boeing_737.engines)
print(boeing_737.company)

#Train
madaraka_express = Train("diesel", "120km/h", "Kenya")
print(madaraka_express.engine_type)

fuxing_hao =Train ("electric","350km/h","China")
print(fuxing_hao.country)

#Motorbike
yamaha = Motorbike("Yamaha", "YSZ-R15")
print(yamaha.model)
print(yamaha.wheels)