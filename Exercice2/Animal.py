# coding: utf-8

# imports

# model
class Animal():
    """
    """

    # class properties
    List = []
    Species = ["Lapin", "Chat", "Mésange", "Python", "Chien", "Tourterelle", "Coccinelle", "Abeille"]
    Colors = ["Blanc", "Vert", "Bleu", "Rouge", "Jaune"]

    # methods
    def __init__(
        self,
        Species,
        Color,
        MaxSpeed = 1):
        """
            Constructor
            (instance method)
        """

        # instance properties
        self.OrderNumber = (
            max([MyAnimal.OrderNumber for MyAnimal in Animal.List]) + 1 
            if Animal.List 
            else 1)
        self.Species = Species
        self.Color = Color
        self.MaxSpeed = MaxSpeed 
        self.Age = 1

        # add new animal to list
        Animal.List.append(self)


    def __repr__(self):
        """
            Returns a string representation of object
            (instance method)
        """

        return f"{self.Species} {self.OrderNumber} {self.Color.lower()} a {self.Age} an(s) et se déplace à {self.MaxSpeed}km/h"


    def Stop(self):
        """
            Stop an animal
            (instance method)
        """

        self.MaxSpeed = 0
        print(f"{self.Species} {self.Color} est maintenant à l'arrêt")


    def Vieillir(self, NbYears : int=1):
        """
            Fait vieillir un animal de x années
            (instance method)
        """

        self.Age += NbYears
        print(f"{self.Species} {self.Color} a maintenant {self.Age} années")


    @classmethod
    def StopAll(cls):
        """
            Stop all animals
            (class method)
        """

        for MyAnimal in cls.List:
            MyAnimal.MaxSpeed = 0


    @classmethod
    def Print(cls):
        """
            Prints all animals in list
            (class method)
        """

        print(f"\nListe des {len(cls.List)} animaux")
        for MyAnimal in cls.List:
            print(MyAnimal)
            # print(f"{MyAnimal.Species} {MyAnimal.OrderNumber} {MyAnimal.Color.lower()} a {MyAnimal.Age} an(s) et se déplace à {MyAnimal.MaxSpeed}km/h")
