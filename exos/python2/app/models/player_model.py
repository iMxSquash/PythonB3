class PlayerModel:
    """
    Représente un joueur dans le jeu Pierre Papier Ciseau.
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.score: int = 0
        self.current_move: str = None

    def update_score(self, points: int) -> None:
        """Ajoute des points au score du joueur."""
        self.score += points

    def reset_score(self) -> None:
        """Réinitialise le score du joueur."""
        self.score: int = 0

    def __str__(self) -> str:
        return f"Joueur: {self.name}, Score: {self.score}, Coup actuel: {self.current_move}"