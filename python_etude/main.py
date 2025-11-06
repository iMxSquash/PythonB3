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
    
    #Les listes
    # mutables
    fruits = ["pomme", "banane", "cerise"]
    listeVide = []

    # acceder aux elements
    print(f"Premier fruit: {fruits[0]}")

    # modifier un element
    fruits[1] = "orange"

    #supprimer un element
    del fruits[2]
    print(f"Fruits apres suppression: {fruits}")

    #boucler a travers les elements
    for fruit in fruits:
        print(f"Fruit: {fruit}")

    # verifier l'existence d'un element
    if "pomme" in fruits:
        print("La pomme est dans la liste des fruits.")

    # nombre d'elements
    print(f"La liste contient {len(fruits)} fruits.")

    # creer une liste d'entiers de 0 a 9
    nombres = list(range(10))

    # ajouter un element
    fruits.append("kiwi")

    # inserer un element a une position specifique
    fruits.insert(1, "mangue")

    # etendre la liste avec une autre liste
    panier = ["raisins", "ananas"]

    fruits.extend(panier)

    #supprimer un element par valeur
    fruits.remove("pomme")

    # supprimer et retourner le dernier element
    dernier_fruit = fruits.pop()

    # decouper une sous-liste
    sous_liste = fruits[1:3] # elements d'index 1 a 2
    print(f"Sous-liste: {sous_liste}")

    autre_sous_liste = fruits[:2] # premiers deux elements

    autre_sous_liste2 = fruits[2:] # a partir de l'index 2 jusqu'a la fin

    autre_sous_liste3 = fruits[1::2] # a partir de l'index 1, tous les deux elements

    # les listes de listes (listes imbriquees)
    matrice = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for ligne in matrice:
        for element in ligne:
            print(f"Element: {element}")
    # acceder a un element specifique
    element = matrice[1][2] # 6

    # modifier un element specifique
    matrice[0][0] = 10  # change 1 en 10

if __name__ == "__main__":
    main()