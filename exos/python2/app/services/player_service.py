from app.utils import request_user_input_while_condition, print_real_time, Colors
from app.models.player_model import PlayerModel

class PlayerService:
    """
    Service pour gérer les joueurs dans le jeu Pierre Papier Ciseau.
    """

    def __init__(self, player: PlayerModel) -> None:
        self.player = player

    def get_move(self, valid_moves: list) -> str:
        """
        Demande au joueur de choisir un coup.
        
        Args:
            valid_moves: Liste des coups valides
            
        Returns:
            str: Le coup choisi par le joueur
        """
        moves_str: str = " / ".join(valid_moves)
        prompt: str = f"\n👤 {self.player.name}, choisissez votre coup ({moves_str}): "

        error_msg: str = f"⚠️  Choix invalide ! Veuillez choisir parmi: {moves_str}"

        move: str = request_user_input_while_condition(
            prompt, 
            lambda x: x in valid_moves,
            error_message=error_msg
        )
        
        return move

    def get_scores(self) -> dict[str, int]:
        """
        Récupère les scores du joueur.

        Returns:
            dict: Un dictionnaire contenant le nom du joueur et son score.
        """
        return {self.player.name: self.player.score}
