from app.models.game_model import GameModel
from app.models.player_model import PlayerModel as Player
from app.models.ia_model import IAPlayerModel
from app.utils import print_real_time, Colors, display_separator
import time

class GameService:
    """
    Service pour gérer les parties de Pierre Papier Ciseau.
    """

    def __init__(self, ia_service=None):
        self.games: list[GameModel] = []
        self.ia_service = ia_service

    def create_game(self, player: Player, ia_player: IAPlayerModel) -> GameModel:
        """Crée une nouvelle partie."""
        game: GameModel = GameModel(player, ia_player)
        self.games.append(game)
        return game

    def get_game(self, game_id: int) -> GameModel | None:
        """Récupère une partie par son ID."""
        return next((game for game in self.games if game.id == game_id), None)

    def play_round(self, game: GameModel, player_move: str) -> dict[str, str | int]:
        """
        Joue un round de la partie.
        
        Args:
            game: La partie en cours
            player_move: Le coup du joueur
            
        Returns:
            dict: Informations sur le round joué
        """
        # Le joueur a déjà joué
        game.player.current_move = player_move
        
        # L'IA joue via le service
        valid_moves = list(GameModel.MOVES.keys())
        ia_move = self.ia_service.get_move(valid_moves)
        
        # Détermine le gagnant
        winner: Player | IAPlayerModel | None = self.determine_winner(game.player, game.ia_player)

        # Met à jour le score
        if winner == game.player:
            game.player.update_score(1)
            result = "victoire"
        elif winner == game.ia_player:
            game.ia_player.update_score(1)
            result = "défaite"
        else:
            result = "égalité"
        
        game.rounds_played += 1
        
        # Crée un dictionnaire pour l'historique du round
        round_info: dict[str, str | int] = {
            'round': game.rounds_played,
            'player_move': player_move,
            'ia_move': ia_move,
            'result': result,
            'player_score': game.player.score,
            'ia_score': game.ia_player.score
        }
        
        game.add_round_to_history(round_info)
        
        return round_info

    def determine_winner(self, player: Player, ia_player: IAPlayerModel) -> Player | IAPlayerModel | None:
        """
        Détermine le gagnant d'un round en utilisant les règles définies dans GameModel.
        
        Returns:
            Player | IAPlayerModel | None: Le gagnant ou None en cas d'égalité
        """
        if player.current_move == ia_player.current_move:
            return None  # Égalité
        
        # Vérifie les règles de victoire à partir des tuples
        for winning_move, losing_move in GameModel.WINNING_RULES:
            if player.current_move == winning_move and ia_player.current_move == losing_move:
                return player
            elif ia_player.current_move == winning_move and player.current_move == losing_move:
                return ia_player
        
        return None

    def display_round_result(self, round_info: dict, game: GameModel) -> None:
        """
        Affiche le résultat d'un round avec des icônes et des couleurs.
        """
        display_separator()
        print()
        
        # Affichage des coups
        player_icon: str = GameModel.MOVES[round_info['player_move']]
        ia_icon: str = GameModel.MOVES[round_info['ia_move']]

        print_real_time(f"👤 {game.player.name}: {player_icon}  {round_info['player_move'].upper()}",
                       delay=0.03, color=Colors.CYAN)
        print_real_time(f"🤖 {game.ia_player.name}: {ia_icon}  {round_info['ia_move'].upper()}", 
                       delay=0.03, color=Colors.MAGENTA)
        print()
        
        # Affichage du résultat
        if round_info['result'] == 'victoire':
            print_real_time("✨ 🎉 VOUS AVEZ GAGNÉ ! 🎉 ✨", delay=0.05, color=Colors.GREEN)
        elif round_info['result'] == 'défaite':
            print_real_time("❌ L'IA a gagné... 😢", delay=0.05, color=Colors.RED)
        else:
            print_real_time("🤝 ÉGALITÉ ! 🤝", delay=0.05, color=Colors.YELLOW)
        
        print()
        self.display_scores(game)
        display_separator()

    def display_scores(self, game: GameModel) -> None:
        """
        Affiche les scores actuels avec un formatage amélioré.
        """
        print()
        print_real_time("📊 SCORES ACTUELS 📊", delay=0.03, color=Colors.BOLD + Colors.YELLOW)
        print_real_time(f"   👤 {game.player.name}: {game.player.score} point(s)", 
                       delay=0.02, color=Colors.CYAN)
        print_real_time(f"   🤖 {game.ia_player.name}: {game.ia_player.score} point(s)", 
                       delay=0.02, color=Colors.MAGENTA)
        print()