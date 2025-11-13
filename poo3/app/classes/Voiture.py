class Voiture:
    """Classe représentant une voiture.
    """
    def __init__(self, marque: str, modele: str):
        """Initialise une voiture avec une marque et un modèle.

        Args:
            marque (str): La marque de la voiture.
            modele (str): Le modèle de la voiture.
        """
        self.__marque: str = marque
        self.__modele: str = modele
    
    @property
    def marque(self) -> str:
        """str: La marque de la voiture."""
        return self.__marque
    
    @marque.setter
    def marque(self, marque: str) -> None:
        if marque:
            self.__marque = marque
        else:
            raise ValueError("La marque ne peut pas être vide.")
        
    @property
    def modele(self) -> str:
        """str: Le modèle de la voiture."""
        return self.__modele
    
    @modele.setter
    def modele(self, modele: str) -> None:
        if modele:
            self.__modele = modele
        else:
            raise ValueError("Le modèle ne peut pas être vide.")