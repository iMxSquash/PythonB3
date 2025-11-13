class Voiture:
    # Props de CLASSE
    # Déclaration + Initialisation
    roues = 4  # Toutes les voitures ont 4 roues

    # Initialisation des props d'INSTANCE
    # on ne peut y acceder qu'à partir de l'instance
    # et non de la classe
    def __init__(self, marque: str, modele: str, annee: int):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.__vitesse = 0  # Vitesse initiale (privée)

    def __str__(self):
        return f"VROOOOOOMMMMMMMMM -> {self.marque} {self.modele} ({self.annee}) - Vitesse: {self.__vitesse} km/h"
    
    def __repr__(self):
        return f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Vitesse: {self.__vitesse} km/h"
    
    # Méthodes d'INSTANCE
    def accelerer(self, increment: int):
        """Augmente la vitesse de la voiture."""
        self.__vitesse += increment
        print(f"La voiture accélère de {increment} km/h. Vitesse actuelle: {self.__vitesse} km/h")
    
    def freiner(self, decrement: int):
        """Diminue la vitesse de la voiture."""
        self.__vitesse = max(0, self.__vitesse - decrement)
        print(f"La voiture freine de {decrement} km/h. Vitesse actuelle: {self.__vitesse} km/h")  

    def afficher_details(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Vitesse: {self.__vitesse} km/h")
        
    @classmethod
    def nombre_de_rues(cls):
        """Méthode de classe pour obtenir le nombre de roues."""
        return cls.roues
    
    @classmethod
    def set_roues(cls, nombre: int):
        """Méthode de classe pour définir le nombre de roues."""
        cls.roues = nombre