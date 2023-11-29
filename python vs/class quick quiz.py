# example of single inheritence :-

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}"
        
class Cat(Animal):
    def __init__(self, name, breed, food):
        Animal.__init__(self, name, species = "cat")
        self.breed = breed
        self.food = food
        
    def __str__(self):
        return f"{self.species},{self.name}\nBreed: {self.breed}\nFood: {self.food}"
        
a = Animal("Muku", "Dog")
print("from animal class:")
print(a,"\n")

c = Cat("Skitty", "Ace", "Fish")
print("from cat class:")
print(c,"\n")