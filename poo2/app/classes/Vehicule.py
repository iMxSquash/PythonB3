class Vehicule:
    """Classe représentant un véhicule.
    """
    def __init__(self, marque: str, modele: str, annee: int):
        """Initialise un véhicule avec une marque, un modèle et une année.

        Args:
            marque (str): La marque du véhicule.
            modele (str): Le modèle du véhicule.
            annee (int): L'année de fabrication du véhicule.
        """
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_details(self) -> str:
        """Affiche les détails du véhicule.

        Returns:
            str: Description des détails du véhicule.
        """
        return f"Marque: {self.marque}, Modèle: {self.modele}"