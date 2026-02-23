#Leon Kobia
#23/02/26
#Program to show classes in python


class Car():
    #attributes of the car
    def __init__(self,model,make,color,year):
        self.model = model
        self.make = make
        self.color = color
        self.year = year

    #print car details
    model = "Atenza"
    make = "Mazda"
    color = "Burgundy"
    year = 2017
    def print_details(self, model, make, color, year):
        print (f"{make} {model} of {color} color was manufactured in {year}")

    
#instantiate a class object

my_car = Car("Atenza", "Mazda", "Burgundy",2017)
dads_car =Car("C250", "Mercedes","Blue",2022)

my_car.print_details("Atenza","Mazda","Burgundy",2017)



