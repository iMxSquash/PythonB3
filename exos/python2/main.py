"""
Créer un jeu console "Pierre Papier Ciseau" en python.
Votre programme devra être correctement modularisé et non mono bloc. 
L'humain joue contre l'ordinateur. 
L'humain peut à chaque tour décider d'arrêter le jeu.
Le jeu ne se termine que si l'humain le demande.
Votre programme doit obligatoirement comporter l'utilisation de boucles, de listes de tuples et de dictionnaires.
Si une fausse entrée est realisée par l'humain un warning doit être affiché avant de redonner le choix de la frappe a l'humain.
A chaque tour le score doit être affiché pour l'humain et le computer BONUS
"""

from app.utils import print_real_time, Colors, request_user_input_while_condition, display_separator, clear_screen
from app.models.player_model import PlayerModel
from app.models.ia_model import IAPlayerModel
from app.services.game_service import GameService
from app.services.player_service import PlayerService
from app.services.ia_service import IAService
import time

def display_welcome() -> None:
    """Affiche l'écran d'accueil du jeu."""
    clear_screen()
    display_separator("═", 70, Colors.CYAN)
    print()
    print_real_time("    🎮  BIENVENUE DANS LE JEU PIERRE PAPIER CISEAU  🎮", delay=0.05, color=Colors.BOLD + Colors.YELLOW)
    print()
    display_separator("═", 70, Colors.CYAN)
    print()
    time.sleep(0.5)

def display_rules() -> None:
    """Affiche les règles du jeu."""
    print_real_time("📜 RÈGLES DU JEU:", delay=0.03, color=Colors.GREEN)
    print()
    rules = [
        "   🪨  Pierre bat Ciseau ✂️",
        "   📄  Papier bat Pierre 🪨",
        "   ✂️  Ciseau bat Papier 📄"
    ]
    for rule in rules:
        print_real_time(rule, delay=0.02, color=Colors.WHITE)
    print()
    display_separator("─", 70, Colors.CYAN)
    print()

def get_player_name() -> str:
    """Demande et retourne le nom du joueur."""
    print_real_time("👤 Quel est votre nom ? ", delay=0.03, color=Colors.CYAN)
    name = input("   ➜ ")
    while not name.strip():
        print_real_time("⚠️  Le nom ne peut pas être vide !", delay=0.02, color=Colors.RED)
        name = input("   ➜ ")
    return name.strip()

def ask_continue() -> bool:
    """
    Demande au joueur s'il veut continuer à jouer.
    
    Returns:
        bool: True si le joueur veut continuer, False sinon
    """
    print()
    response = request_user_input_while_condition(
        "🔄 Voulez-vous faire une autre manche ? (oui/non): ",
        lambda x: x in ['oui', 'non', 'o', 'n'],
        error_message="⚠️  Répondez par 'oui' ou 'non' !"
    )
    return response in ['oui', 'o']

def display_final_stats(game) -> None:
    """
    Affiche les statistiques finales de la partie.
    
    Args:
        game: La partie terminée
    """
    clear_screen()
    display_separator("═", 70, Colors.YELLOW)
    print()
    print_real_time("    📊 STATISTIQUES FINALES 📊", delay=0.05, color=Colors.BOLD + Colors.YELLOW)
    print()
    display_separator("═", 70, Colors.YELLOW)
    print()
    
    # Affichage des scores finaux
    print_real_time(f"Nombre total de manches jouées: {game.rounds_played}", delay=0.02, color=Colors.WHITE)
    print()
    print_real_time(f"👤 {game.player.name}: {game.player.score} victoire(s)", delay=0.02, color=Colors.CYAN)
    print_real_time(f"🤖 {game.ia_player.name}: {game.ia_player.score} victoire(s)", delay=0.02, color=Colors.MAGENTA)
    
    # Calcul des égalités
    draws = game.rounds_played - game.player.score - game.ia_player.score
    print_real_time(f"🤝 Égalités: {draws}", delay=0.02, color=Colors.YELLOW)
    print()
    
    # Annonce du vainqueur final
    if game.player.score > game.ia_player.score:
        print_real_time("🏆 ✨ FÉLICITATIONS ! VOUS ÊTES LE GRAND GAGNANT ! ✨ 🏆", 
                       delay=0.05, color=Colors.GREEN)
    elif game.ia_player.score > game.player.score:
        print_real_time("🤖 L'IA a remporté la partie... Réessayez ! 💪", 
                       delay=0.05, color=Colors.RED)
    else:
        print_real_time("🤝 MATCH NUL ! Vous êtes à égalité ! 🤝", 
                       delay=0.05, color=Colors.YELLOW)
    
    print()
    display_separator("═", 70, Colors.YELLOW)
    print()
    print_real_time("Merci d'avoir joué ! À bientôt ! 👋", delay=0.03, color=Colors.CYAN)
    print()

def main() -> None:
    """
    Fonction principale du programme.
    Gère la boucle principale du jeu.
    """
    # Affichage de l'accueil
    display_welcome()
    
    # Affichage des règles
    display_rules()
    
    # Récupération du nom du joueur
    player_name = get_player_name()
    print()
    print_real_time(f"Bienvenue {player_name} ! Préparez-vous à affronter l'IA ! 🤖", 
                   delay=0.03, color=Colors.GREEN)
    time.sleep(1)
    
    # Initialisation des modèles
    player = PlayerModel(player_name)
    ia_player = IAPlayerModel("Ordinateur")
    
    # Initialisation des services
    ia_service = IAService(ia_player)
    game_service = GameService(ia_service)
    player_service = PlayerService(player)
    
    # Création de la partie
    game = game_service.create_game(player, ia_player)
    
    # Liste des coups valides (depuis le dictionnaire)
    from app.models.game_model import GameModel
    valid_moves = list(GameModel.MOVES.keys())
    
    print()
    print_real_time("🎮 QUE LE JEU COMMENCE ! 🎮", delay=0.05, color=Colors.BOLD + Colors.GREEN)
    time.sleep(1)
    
    # Boucle principale du jeu - continue tant que le joueur veut jouer
    game_running = True
    while game_running:
        print()
        display_separator("═", 70, Colors.CYAN)
        print_real_time(f"    🎯 MANCHE {game.rounds_played + 1} 🎯", 
                       delay=0.03, color=Colors.BOLD + Colors.YELLOW)
        display_separator("═", 70, Colors.CYAN)
        
        # Le joueur choisit son coup
        player_move = player_service.get_move(valid_moves)
        
        # Jouer le round
        round_info = game_service.play_round(game, player_move)
        
        # Afficher le résultat
        time.sleep(0.5)
        game_service.display_round_result(round_info, game)
        
        # Demander si le joueur veut continuer
        game_running = ask_continue()
    
    # Affichage des statistiques finales
    time.sleep(0.5)
    display_final_stats(game)

if __name__ == "__main__":
    main()
