from app.models.ia_model import IAPlayerModel
from random import choice
class IAService:
    """
    Service pour gérer l'IA dans le jeu Pierre Papier Ciseau.
    """

    def __init__(self, ia_player: IAPlayerModel) -> None:
        self.ia_player = ia_player

    def get_move(self, valid_moves: list[str]) -> str:
        """
        L'IA choisit un coup.
        
        Returns:
            str: Le coup choisi par l'IA
        """
        self.ia_player.current_move = choice(valid_moves)
        return self.ia_player.current_move

    def get_scores(self) -> dict[str, int]:
        """
        Récupère les scores de l'IA.

        Returns:
            dict: Un dictionnaire contenant le nom de l'IA et son score.
        """
        return {self.ia_player.name: self.ia_player.score}
