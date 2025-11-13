from typing import List
from .Personne import Personne


class CompteBancaire:
    """
    Classe CompteBancaire avec trois niveaux d'encapsulation:
    - titulaire: public
    - _solde: protégé
    - __transactions: privé
    """
    
    def __init__(self, titulaire: Personne, solde_initial: float = 0) -> None:
        """
        Initialise un compte bancaire
        
        Args:
            titulaire: La personne titulaire du compte
            solde_initial: Le solde initial du compte (par défaut: 0)
        """
        self.titulaire: Personne = titulaire
        self._solde: float = solde_initial
        self.__transactions: List[str] = []
        if solde_initial > 0:
            self.__enregistrer_transaction(f"Ouverture du compte avec {solde_initial}€")
    
    # Getter et Setter pour _solde
    @property
    def solde(self) -> float:
        """Retourne le solde du compte"""
        return self._solde
    
    @solde.setter
    def solde(self, valeur: float) -> None:
        """Définit le solde du compte"""
        self._solde = valeur
    
    # Getter pour __transactions (pas de setter pour préserver l'intégrité)
    @property
    def transactions(self) -> List[str]:
        """Retourne la liste des transactions"""
        return self.__transactions.copy()
    
    def deposer(self, montant: float) -> None:
        """
        Dépose un montant sur le compte
        
        Args:
            montant: Le montant à déposer
        """
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        
        self._solde += montant
        self.__enregistrer_transaction(f"Dépôt de {montant}€")
        print(f"✓ Dépôt de {montant}€ effectué. Nouveau solde: {self._solde}€")
    
    def afficher_solde(self) -> None:
        """Affiche le solde du compte (méthode publique)"""
        print(f"Solde actuel: {self._solde}€")
    
    def _afficher_solde(self) -> None:
        """Affiche le solde du compte (méthode protégée)"""
        print(f"[Méthode protégée] Solde: {self._solde}€")
    
    def __enregistrer_transaction(self, description: str) -> None:
        """
        Enregistre une transaction (méthode privée)
        
        Args:
            description: La description de la transaction
        """
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = f"[{timestamp}] {description}"
        self.__transactions.append(transaction)
        print(f"[Méthode privée] Transaction enregistrée: {description}")
