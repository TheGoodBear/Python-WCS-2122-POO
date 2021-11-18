# coding: utf-8

# imports

# model
class Animal():
    """
    """

    # class properties
    List = []

    # methods
    def __init__(
        self,
        Species: str,
        Color: str,
        Name: str,
        Gender: str,
        MaxSpeed: int = 1) -> None:
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
        self.Name = Name
        self.Prefix = ("l'" if self.Species[0] 
            in "aeiouy" else (
            "le " if Gender == "m" else "la "
            ))
        self.MaxSpeed = MaxSpeed 
        self.Age = 1

        # add new animal to list
        Animal.List.append(self)


    def __repr__(self) -> str:
        """
            Returns a string representation of object
            (instance method)
        """

        return f"{self.Name} {self.Prefix}{self.Species} {self.Color.lower()} a {self.Age} an(s) et se déplace à {self.MaxSpeed}km/h"


    def Stop(self) -> None:
        """
            Stop an animal
            (instance method)
        """

        self.MaxSpeed = 0
        print(f"{self.Species} {self.Color} est maintenant à l'arrêt")


    def Vieillir(self, NbYears: int = 1) -> None:
        """
            Fait vieillir un animal de x années
            (instance method)
        """

        self.Age += NbYears
        print(f"{self.Species} {self.Color} a maintenant {self.Age} années")


    @classmethod
    def StopAll(cls) -> None:
        """
            Stop all animals
            (class method)
        """

        for MyAnimal in cls.List:
            MyAnimal.MaxSpeed = 0


    @classmethod
    def Print(cls, ToSort) -> None:
        """
            Prints all animals in list
            (class method)
        """
        if ToSort == 'y':
            cls.List.sort(
                key=lambda CurrentAnimal: CurrentAnimal.Species
                )

        print(f"\nListe des {len(cls.List)} animaux")
        for MyAnimal in cls.List:
            print(MyAnimal)
            # print(f"{MyAnimal.Species} {MyAnimal.OrderNumber} {MyAnimal.Color.lower()} a {MyAnimal.Age} an(s) et se déplace à {MyAnimal.MaxSpeed}km/h")
