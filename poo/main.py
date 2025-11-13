from app.utils import utils
from app.classes.Voiture import Voiture
from app.classes.Ma_Classe import Ma_Classe

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