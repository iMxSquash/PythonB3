from app.utils import utils
from app.classes.Voiture import Voiture
from app.classes.Ma_Classe import Ma_Classe
from app.classes.Maths import Maths

if __name__ == "__main__":
    voiture = Voiture("Toyota", "Corolla", 2020)
    utils.show(voiture, "ma_voiture")
    
    print("\nAcces a une prop de classe:")
    print("Voiture.roues =", Voiture.roues)
    
    voiture.afficher_details()
    
    ma_classe = Ma_Classe(10, {"clé": "valeur"})
    
    print(voiture)
    print(repr(voiture))
    
    print("\n-- Acces à un membre privé --")
    print("vitesse actuelle :", voiture._Voiture__vitesse)
    
    # utilisation des méthodes statiques de la classe Maths
    a = 5
    b = 3
    print(f"\nUtilisation des méthodes statiques de la classe Maths:")
    print(f"Addition de {a} et {b} =", Maths.addition(a, b))
    print(f"Soustraction de {a} et {b} =", Maths.subtract(a, b))
    print(f"Multiplication de {a} et {b} =", Maths.multiply(a, b))
    print(f"Division de {a} et {b} =", Maths.divide(a, b))