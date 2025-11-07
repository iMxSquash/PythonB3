from app.models.player_model import PlayerModel as Player

class GameModel:
    """
    Représente le modèle de données du jeu Pierre Papier Ciseau.
    """
    
    # Dictionnaire des coups possibles avec leurs icônes
    MOVES: dict[str, str] = {
        'pierre': '🪨',
        'papier': '📄',
        'ciseau': '✂️'
    }
    
    # Liste des tuples de règles de victoire (gagnant, perdant)
    WINNING_RULES: list[tuple[str, str]] = [
        ('pierre', 'ciseau'),
        ('papier', 'pierre'),
        ('ciseau', 'papier')
    ]

    def __init__(self, player: Player, ia_player: Player) -> None:
        self.id: int = id(self)
        self.rounds_played: int = 0
        self.winner: str = None
        self.player: Player = player
        self.ia_player: Player = ia_player
        self.history = []

    def add_round_to_history(self, round_info: dict) -> None:
        """Ajoute un round à l'historique."""
        self.history.append(round_info)

    def __str__(self) -> str:
        return f"Rounds played: {self.rounds_played}, Winner: {self.winner}, Players: {self.player} vs IA Player: {self.ia_player}"