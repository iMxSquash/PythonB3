from .Vehicule import Vehicule
from .Moteur import Moteur

class Voiture(Vehicule, Moteur):
    """Classe représentant une voiture, héritant des classes Vehicule et Moteur.

    Args:
        Vehicule (Vehicule): Classe de base Vehicule.
        Moteur (Moteur): Classe de base Moteur.
    """
    def __init__(self, marque: str, modele: str, annee: int, puissance: int, vitesse: float = 0.00):
        """Initialise une voiture avec une marque, un modèle, une année, une puissance moteur et une vitesse.

        Args:
            marque (str): La marque de la voiture.
            modele (str): Le modèle de la voiture.
            annee (int): L'année de fabrication de la voiture.
            puissance (int): La puissance du moteur en chevaux.
            vitesse (float, optional): La vitesse actuelle de la voiture en km/h. Defaults to 0.00.
        """
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance)
        self.vitesse = vitesse

    def accelerer(self, increment: float) -> None:
        """Augmente la vitesse de la voiture.

        Args:
            increment (float): L'incrément de vitesse en km/h.
        """
        self.vitesse += increment
        print(f"La voiture accélère de {increment} km/h. Vitesse actuelle: {self.vitesse} km/h")
    
    def freiner(self, decrement: float) -> None:
        """Réduit la vitesse de la voiture.

        Args:
            decrement (float): La décrémentation de vitesse en km/h.
        """
        self.vitesse = max(0, self.vitesse - decrement)
        print(f"La voiture freine de {decrement} km/h. Vitesse actuelle: {self.vitesse} km/h")
    
    def afficher_details(self) -> str:
        """Affiche les détails complets de la voiture.

        Returns:
            str: Description complète des détails de la voiture.
        """
        details = Vehicule.afficher_details(self)
        details += ", " + Moteur.afficher_details(self)
        return f"{details}, Vitesse: {self.vitesse} km/h"
    
    def klaxonner(self) -> str:
        """Fait klaxonner la voiture.

        Returns:
            str: Le son du klaxon.
        """
        return "Beep Beep!"
    