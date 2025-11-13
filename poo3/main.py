from app.classes.Voiture import Voiture

if __name__ == "__main__":
    voiture1 = Voiture("Toyota", "Corolla")
    voiture2 = Voiture("Honda", "Civic")

    print(f"Voiture 1: {voiture1.marque} {voiture1.modele}")
    print(f"Voiture 2: {voiture2.marque} {voiture2.modele}")
    
    voiture1.marque = "Ford"
    voiture1.modele = "Mustang"
    voiture2.marque = "Chevrolet"
    voiture2.modele = "Camaro"

    print(f"Voiture 1 modifiée: {voiture1.marque} {voiture1.modele}")
    print(f"Voiture 2 modifiée: {voiture2.marque} {voiture2.modele}")