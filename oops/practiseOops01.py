#Create a class pets from a class animals and further create a class dogs from pets.add a method bark to dogs.

class Animals:
    animalType= "Mammal"

class Pets:
    petcolor= "White"

class Dogs:
    @staticmethod
    def bark():
        print("Bow bow")

d= Dogs()
d.bark()        
