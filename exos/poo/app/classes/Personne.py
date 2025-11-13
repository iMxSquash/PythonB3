class Personne:
    """
    Classe Personne avec trois niveaux d'encapsulation:
    - nom: public
    - _age: protégé
    - __numero_securite: privé
    """
    
    def __init__(self, nom: str, age: int, numero_securite: str = "123-45-6789") -> None:
        """
        Initialise une personne
        
        Args:
            nom: Le nom de la personne
            age: L'âge de la personne
            numero_securite: Le numéro de sécurité sociale (valeur par défaut: "123-45-6789")
        """
        self.nom: str = nom
        self._age: int = age
        self.__numero_securite: str = numero_securite
    
    @property
    def age(self) -> int:
        """Retourne l'âge de la personne"""
        return self._age
    
    @age.setter
    def age(self, valeur: int) -> None:
        """Définit l'âge de la personne"""
        if valeur:
            if valeur < 0:
                raise ValueError("L'âge ne peut pas être négatif")
            self._age = valeur
        else:
            raise ValueError("L'âge doit être une valeur valide")
    
    @property
    def numero_securite(self) -> str:
        """Retourne le numéro de sécurité sociale"""
        return self.__numero_securite
    
    @numero_securite.setter
    def numero_securite(self, valeur: str) -> None:
        """Définit le numéro de sécurité sociale"""
        if valeur:
            self.__numero_securite = valeur
        else:
            raise ValueError("Le numéro de sécurité sociale ne peut pas être vide")
    
    def afficher_info(self) -> None:
        """Affiche les informations de la personne"""
        print("=== Informations de la personne ===")
        print(f"Nom: {self.nom}")
        print(f"Âge: {self._age} ans")
        print(f"Numéro de sécurité: {self.__numero_securite}")
        print("===================================")
