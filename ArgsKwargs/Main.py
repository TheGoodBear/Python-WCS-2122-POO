
# def Func11(Names: tuple):
#     for Name in Names:
#         print(Name)

def Func1(DataType, *args):
    """
        *args correspond à une liste d'arguments
        dont on ne connais pas la taille par avance
    """
    print(f"\nVoici une liste de {DataType}")
    for Name in args:
        print(Name)


def Func2(**kwargs):
    """
        **kwargs correspond à un dictionnaire
        dont on ne connait pas les éléments à l'avance
    """
    
    LastName = kwargs.get("LastName", None)
    FirstName = kwargs.get("FirstName", None)
    Age = kwargs.get("Age", None)
    
    if (LastName and FirstName):
        print(f"Mon nom est {LastName}, {FirstName} {LastName}")
    elif (LastName):
        print(f"Mon nom est {LastName}")
    elif (FirstName):
        print(f"Mon prénom est {FirstName}")
    else:
        print("Je ne sais pas qui je suis...")
    
    if Age:
        print(f"... et j'ai {Age} ans")


def Func3(Message1, Message2, *args, **kwargs):
    """
    """
    
    LastName = kwargs.get("LastName", None)
    FirstName = kwargs.get("FirstName", None)
    Age = kwargs.get("Age", None)
    
    print()
    print(Message1)
    print(Message2)
    
    Sum = 0 
    for Element in args:
        Sum += Element
    print(f"Total = {Sum}")
    
    if (LastName and FirstName):
        print(f"Mon nom est {LastName}, {FirstName} {LastName}")
    elif (LastName):
        print(f"Mon nom est {LastName}")
    elif (FirstName):
        print(f"Mon prénom est {FirstName}")
    else:
        print("Je ne sais pas qui je suis...")
    
    if Age:
        print(f"... et j'ai {Age} ans")
    



if __name__ == "__main__":
    
    # Func11(["Pedro", "Marcel", "Georges", "Micheline"])
    Func1("prénoms", "Pedro", "Marcel", "Georges", "Micheline")
    
    print()
    Func2(LastName="Bond", FirstName="James")
    Func2(LastName="Bond", Age=35)
    Func2(FirstName="James")
    Func2()
    
    Func3("Bonjour", "Au revoir", 10, 20, 30, 40, 50, LastName="Bond", FirstName="James")
    
    