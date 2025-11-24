"""Module définissant la classe Frappe pour les attaques des personnages."""


class Frappe:
    """Représente une frappe avec sa force et son gain d'expérience."""

    def __init__(self, nom: str, force: int, experience_gain: int) -> None:
        """Initialise une frappe.

        Args:
            nom: Le nom de la frappe
            force: La force de la frappe (dégâts infligés)
            experience_gain: L'expérience gagnée lors de l'utilisation
        """
        self._nom = nom
        self._force = force
        self._experience_gain = experience_gain

    @property
    def nom(self) -> str:
        """Retourne le nom de la frappe."""
        return self._nom

    @property
    def force(self) -> int:
        """Retourne la force de la frappe."""
        return self._force

    @property
    def experience_gain(self) -> int:
        """Retourne le gain d'expérience de la frappe."""
        return self._experience_gain
