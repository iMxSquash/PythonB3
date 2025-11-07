import random
from app.models.player_model import PlayerModel

class IAPlayerModel(PlayerModel):
    """
    Représente un joueur contrôlé par l'IA dans le jeu Pierre Papier Ciseau.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __str__(self) -> str:
        return f"IA: {self.name}, Score: {self.score}"