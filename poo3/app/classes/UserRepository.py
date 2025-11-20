from typing import Protocol, List

class UserRepository(Protocol):
    def find_all(self) -> List[dict]:
        """find_all récupère tous les utilisateurs.

        Returns:
            List[dict]: Une liste de dictionnaires représentant les utilisateurs.
        """
        ...
        
    def save(self, user: dict[str | str] | str) -> None:
        """save enregistre un utilisateur.

        Args:
            user (dict): Un dictionnaire représentant l'utilisateur à enregistrer.
        """
        ...