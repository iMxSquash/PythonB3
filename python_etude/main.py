from app.utils import *
import sys
from app.models.player import Player
from bataille import Battle

valeurGlobale = 1

def ma_fonction():
    valeurLocale = 2
    print(valeurLocale)

def main():
    print("Début d'execution du programme...")
    saluer("kevin")
    if len(sys.argv) > 1:
        print(f"Argument de la ligne de commande: {sys.argv[1:]}")
    else:
        print("Aucun argument de la ligne de commande fourni.")
        
    print(valeurGlobale)
    ma_fonction()
    
    age = 25
    
    #formatage avancé
    print("Alice a {} ans et Bob a {} ans".format(age, age + 5))
    
    start_result = (7802 + 4752)/12700
    print(f"la stat final est : {start_result:.2f}")
    print(f"la stat final est : {start_result:.4f}")
    print(f"la stat final est : {start_result:.0f}")
    
    print(f"{7864:*>16d}")
    
    entier = 2
    print(f"le type de {entier} est {type(entier)}")
    
    fruits = ["pomme", "poire", "cerise"]
    print(f"le type de {fruits} est {type(fruits)}")
    print(" ".join(fruit for fruit in fruits))
    
    coordonees = (10.0, 20.0)
    print(f"le type de {coordonees} est {type(coordonees)}")
    x, y = coordonees
    print(f"x = {x}, y = {y}")
    
    nombres = range(5)
    print(f"le type de {nombres} est {type(nombres)}")
    for i in nombres:
        print(i)
    
    etudiant = {"nom": "Alice", "age": 23}
    print(f"le type de {etudiant} est {type(etudiant)}")
    for cle, valeur in etudiant.items():
        print(f"{cle}: {valeur}")
        
    print(f"{int('42')} est de type {type(int('42'))}")
    
    # opérateurs
    a = 10
    b = 3
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ** {b} = {a ** b}")
    
    #match case
    jour = "lundi"
    match jour:
        case "lundi":
            print("C'est le premier jour de la semaine.")
        case "mercredi":
            print("C'est le milieu de la semaine.")
        case "vendredi":
            print("C'est presque le week-end.")
        case _:
            print("C'est un autre jour de la semaine.")
    
    def chateau(h: int) -> int:
        print("*" * h)
        if h > 0:
            chateau(h - 1)

    chateau(10)
    
    def chateau_2(h: int) -> int:
        for i in range(h, 0, -1):
            print("*" * i)
            
    chateau_2(10)
            
    def chateau_3(h: int) -> int:
        while h > 0:
            print("*" * h)
            h -= 1
    
    # chateau_3(int(input("Entrez la hauteur du chateau: ")))

    joueur1 = Player("Alice")
    joueur2 = Player("Bob")
    bataille = Battle(joueur1, joueur2)
    bataille.start_battle()

if __name__ == "__main__":
    main()