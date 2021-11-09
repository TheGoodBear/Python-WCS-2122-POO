# coding: utf-8

# imports
import random
import time
from Animal import Animal

# functions
def Main():
    """
    """

    print("Animaux du monde\n")

    # Exercice 1
    FaireNaitre()

    # Exercice 2
    FaireViellir()

    # end
    print("\nAu revoir")


def FaireNaitre():
    """
        Demander à l'utilisateur 
        combien d'animaux doivent naitre    
    """

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


def FaireViellir():
    """
        Demander à l'utilisateur 
        - de quelle espèce et/ou de quelle couleur (parmi les espèces et couleurs possibles)
            il souhaite faire vieillir les animaux
        - de combien d'années    
    """
  
    NbYears = None
    try:

        while(NbYears is None or NbYears > 0):
            print("\nFaire vieillir...")
            NbYears = int(input("De combien d'années : "))

            if NbYears > 0:
                Specie = None
                while(Specie != "" and Specie not in Animal.Species):
                    print(f"Espèces possibles : {', '.join(Animal.Species)}")
                    Specie = input("De quelle espèce : ")
                Color = None
                while(Color != "" and Color not in Animal.Colors):
                    print(f"Couleurs possibles : {', '.join(Animal.Colors)}")
                    Color = input("De quelle couleur : ")

                # méthode basique
                Start1 = time.time()
                for MyAnimal in Animal.List:
                    if ((Specie == "" or MyAnimal.Species == Specie)
                        and (Color == "" or MyAnimal.Color == Color)):
                        MyAnimal.Vieillir(NbYears)
                Duration1 = time.time() - Start1
                print(f"Durée Boucle For : {round(Duration1, 4)}")

                # méthode avec filter    
                # Start2 = time.time()                                           
                # AnimalsToGrowOlder = list(
                #     filter(
                #         lambda AnimalIterated:
                #         (AnimalIterated.Species.lower() == Specie.lower() or Specie =="")
                #         and 
                #         (AnimalIterated.Color.lower() == Color.lower() or Color==""),
                #         Animal.List
                #         )
                #     )
                # for AnimalIterated in AnimalsToGrowOlder:
                #     AnimalIterated.Vieillir(NbYears)
                # Duration2 = time.time() - Start2
                # print(f"Durée Filter : {round(Duration2, 4)}")
                
                # méthode avec compréhension de liste   
                # Start3 = time.time()                                             
                # [TheAnimal.Vieillir(NbYears) for TheAnimal in Animal.List if (
                #     (Specie == "" or TheAnimal.Species == Specie) and 
                #     (Color == "" or TheAnimal.Color == Color)
                #     )]
                # Duration3 = time.time() - Start3                
                # print(f"Durée Compréhension : {round(Duration3, 4)}")


    except ValueError:
        pass

    # affiche la liste
    Animal.Print()



# Code starts here
if __name__ == "__main__":
    Main()
