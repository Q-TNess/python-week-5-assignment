# ASSIGNMENT 1

class Movies():
    def __init__(self,genre,name):
        self.genre = genre
        self.name = name

trailer1 = Movies("Sci-Fiction","Black Panther")
trailer2 = Movies("Action", "Den of Theives")
print(trailer1.genre)
print(trailer1.name)

print(trailer2.genre)
print(trailer2.name)

#encapsulation
class YearCategory:
    def __init__(self):
        self.__movieYear = 2010  

    def Choice(self):
        if self.__movieYear > 2023:
            print("Recent movie")
        else:
            print("Old movie")

catagory = YearCategory()
catagory.Choice()


#ACTIVITY 2

class Plane:
    def move(self):
        return "Flies through the sky"

class Boat:
    def move(self):
        return "Sails on the water"

# Polymorphism 
for vehicle in [Plane(), Boat()]:
    print(vehicle.move())
