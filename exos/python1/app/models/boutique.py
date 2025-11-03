"""
Modèle représentant une boutique et ses données.
"""
from app.utils import formater_prix


class Boutique:
    """
    Classe représentant une boutique avec ses informations de base.
    
    Attributes:
        nom_boutique (str): Nom de la boutique
        produit (str): Type de produit vendu
        prix_unitaire (float): Prix unitaire du produit
        quantite_stock (int): Quantité en stock
        tva (float): Taux de TVA (exemple: 0.20 pour 20%)
        compte_client (float): Solde du compte client
        compte_boutique (float): Solde du compte de la boutique
    """
    
    def __init__(
        self,
        nom_boutique: str,
        produit: str,
        prix_unitaire: float,
        quantite_stock: int,
        tva: float,
        compte_client: float,
        compte_boutique: float
    ) -> None:
        """
        Initialise une nouvelle instance de Boutique.
        
        Args:
            nom_boutique: Nom de la boutique
            produit: Type de produit vendu
            prix_unitaire: Prix unitaire du produit
            quantite_stock: Quantité en stock
            tva: Taux de TVA
            compte_client: Solde du compte client
            compte_boutique: Solde du compte de la boutique
        """
        self.nom_boutique: str = nom_boutique
        self.produit: str = produit
        self.prix_unitaire: float = prix_unitaire
        self.quantite_stock: int = quantite_stock
        self.tva: float = tva
        self.compte_client: float = compte_client
        self.compte_boutique: float = compte_boutique
    
    def __str__(self) -> str:
        """
        Retourne une phrase complète utilisant toutes les variables de la boutique.
        
        Returns:
            str: Phrase descriptive de la boutique
        """
        return (
            f"La boutique {self.nom_boutique} vend des {self.produit} au prix "
            f"unitaire de {formater_prix(self.prix_unitaire)} avec une TVA de {self.tva * 100}%. "
            f"Il y a actuellement {self.quantite_stock} unités en stock. "
            f"Le compte client dispose de {formater_prix(self.compte_client)} et le compte de "
            f"la boutique contient {formater_prix(self.compte_boutique)}."
        )
    
    def __repr__(self) -> str:
        """
        Retourne une représentation textuelle de l'objet Boutique.
        
        Returns:
            str: Représentation de l'objet
        """
        return (
            f"Boutique(nom_boutique='{self.nom_boutique}', "
            f"produit='{self.produit}', "
            f"prix_unitaire={self.prix_unitaire}, "
            f"quantite_stock={self.quantite_stock}, "
            f"tva={self.tva}, "
            f"compte_client={self.compte_client}, "
            f"compte_boutique={self.compte_boutique})"
        )
    
    def afficher_infos(self) -> None:
        """
        Affiche les informations de la boutique de manière formatée.
        """
        print(f"\n{'='*50}")
        print(f"Boutique: {self.nom_boutique}")
        print(f"{'='*50}")
        print(f"Produit: {self.produit}")
        print(f"Prix unitaire: {formater_prix(self.prix_unitaire)}")
        print(f"Quantité en stock: {self.quantite_stock}")
        print(f"TVA: {self.tva * 100}%")
        print(f"Compte client: {formater_prix(self.compte_client)}")
        print(f"Compte boutique: {formater_prix(self.compte_boutique)}")
        print(f"{'='*50}\n")
