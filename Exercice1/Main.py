# coding: utf-8

# imports
import random
from Animal import Animal

# functions
def Main():
    """
    """

    print("Animaux du monde\n")

    # get number of animals to create
    NumberOfAnimals = 0
    try:
        NumberOfAnimals = int(input("Combien d'animaux dois-je faire naitre ? "))
    except:
        print("Je ne reconnais pas ce nombre")

    # create appropriate number of animals
    for Number in range(NumberOfAnimals):
        Animal(
            random.choice(Animal.Species),
            random.choice(Animal.Colors))

    # print list
    Animal.Print()
    input()

    # Animal2 = [MyAnimal for MyAnimal in Animal.List if MyAnimal.OrderNumber == 2][0]
    # Animal2.StopAll() -> works but bad idea, should not call class method on instance

    # stop animal number 2 and 5
    try:
        Animal2 = [MyAnimal for MyAnimal in Animal.List if MyAnimal.OrderNumber == 2][0]
        Animal2.Stop()
        Animal5 = [MyAnimal for MyAnimal in Animal.List if MyAnimal.OrderNumber == 5][0]
        Animal5.Stop()
    except:
        pass

    # print list
    Animal.Print()
    input()

    # stop all animals
    # Animal.Stop() -> error, cannot call instance method on class
    Animal.StopAll()

    # print list
    Animal.Print()
    input()

    # remove some animals
    Animal.List.pop(3)
    Animal.List.pop(5)
    Animal.List.pop(7)

    # add another animal
    Animal(
        random.choice(Animal.Species),
        random.choice(Animal.Colors))

    # print list
    Animal.Print()

    # print animal 3
    MyAnimal = [MyAnimal for MyAnimal in Animal.List if MyAnimal.OrderNumber == 3][0]
    print(MyAnimal)

    # end
    print("\nAu revoir")


# Code starts here
if __name__ == "__main__":
    Main()
