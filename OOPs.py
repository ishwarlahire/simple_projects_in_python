class Vehicle:
    color = "Black"
    veels = "4 + 1"
    fule = "Petrol"

bike = Vehicle()
print(bike.color)
airplain = Vehicle()
print(airplain.veels) 

class Car:
    brands ="Scorpio"

C1 = Car()
print(C1.brands)

class Laptop:
    brands = "defoult"
    RAM =  "8.0GB"
    Price = "20k"

laptop1 = Laptop()
laptop1.brands = "lenovo"
laptop1.RAM = "4.5GB"
laptop1.Price = "45000/-"

laptop2 = Laptop()
laptop2.brands = "Dell"
laptop2.RAM = "8.1GB"
laptop2.Price = "90000/-"

print(laptop1.brands,laptop1.RAM,laptop1.Price)
print(laptop2.brands,laptop2.RAM,laptop2.Price)