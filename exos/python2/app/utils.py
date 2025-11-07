"""
Fonctions utilitaires pour l'application.
"""

import time

# Codes de couleur ANSI
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_real_time(message: str, delay: float = 0.05, color: str = "") -> None:
    """
    Affiche un message en temps réel dans la console, lettre par lettre.
    
    Args:
        message (str): Le message à afficher.
        delay (float): Délai entre chaque lettre.
        color (str): Couleur du texte (optionnel).
    """
    if color:
        print(color, end="", flush=True)
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    if color:
        print(Colors.RESET, end="", flush=True)
    print()  # Retour à la ligne

def request_user_input_while_condition(prompt: str, condition: callable, error_message: str = "⚠️  Entrée invalide. Veuillez réessayer.") -> str:
    """
    Demande une entrée utilisateur tant qu'une condition spécifique n'est pas remplie.
    
    Args:
        prompt (str): Le message à afficher pour demander l'entrée.
        condition (callable): La condition à vérifier.
        error_message (str): Message d'erreur personnalisé.

    Returns:
        str: L'entrée de l'utilisateur.
    """
    while True:
        input_value = input(prompt)
        try:
            user_input = str(input_value).lower().strip()
            if condition(user_input):
                return user_input
            else:
                print_real_time(error_message, delay=0.02, color=Colors.RED)
        except ValueError:
            print_real_time(error_message, delay=0.02, color=Colors.RED)

def clear_screen() -> None:
    """Efface l'écran de la console."""
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def display_separator(char: str = "═", length: int = 60, color: str = Colors.CYAN) -> None:
    """Affiche une ligne de séparation."""
    print(f"{color}{char * length}{Colors.RESET}")