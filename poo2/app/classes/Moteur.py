class Moteur:
    """Classe représentant un moteur.
    """
    def __init__(self, puissance: int):
        """Initialise un moteur avec une puissance donnée.

        Args:
            puissance (int): La puissance du moteur en chevaux.
        """
        self.puissance = puissance

    def demarrer(self) -> str:
        """Démarre le moteur.

        Returns:
            str: Message indiquant que le moteur a démarré.
        """
        return "Moteur démarré"
    
    def afficher_details(self) -> str:
        """Affiche les détails du moteur.

        Returns:
            str: Description des détails du moteur.
        """
        return f"Puissance du moteur: {self.puissance} CV"