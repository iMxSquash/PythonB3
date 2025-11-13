class Rectangle:
    """
    Classe Rectangle avec deux propriétés privées:
    - __largeur
    - __hauteur
    """
    
    def __init__(self, largeur: float, hauteur: float) -> None:
        """
        Initialise un rectangle
        
        Args:
            largeur: La largeur du rectangle
            hauteur: La hauteur du rectangle
        """
        self.__largeur: float = largeur
        self.__hauteur: float = hauteur
    
    # Getter et Setter pour __largeur
    @property
    def largeur(self) -> float:
        """Retourne la largeur du rectangle"""
        return self.__largeur
    
    @largeur.setter
    def largeur(self, valeur: float) -> None:
        """
        Définit la largeur du rectangle
        
        Args:
            valeur: La nouvelle largeur
            
        Raises:
            ValueError: Si la largeur est négative ou nulle
        """
        if valeur <= 0:
            raise ValueError("La largeur doit être positive et non nulle")
        self.__largeur = valeur
    
    # Getter et Setter pour __hauteur
    @property
    def hauteur(self) -> float:
        """Retourne la hauteur du rectangle"""
        return self.__hauteur
    
    @hauteur.setter
    def hauteur(self, valeur: float) -> None:
        """
        Définit la hauteur du rectangle
        
        Args:
            valeur: La nouvelle hauteur
            
        Raises:
            ValueError: Si la hauteur est négative ou nulle
        """
        if valeur <= 0:
            raise ValueError("La hauteur doit être positive et non nulle")
        self.__hauteur = valeur
    
    # Getter pour l'aire (calculée)
    @property
    def aire(self) -> float:
        """
        Retourne l'aire du rectangle
        
        Returns:
            L'aire calculée (largeur × hauteur)
        """
        return self.__largeur * self.__hauteur
