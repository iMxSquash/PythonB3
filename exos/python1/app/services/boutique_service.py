"""
Service contenant la logique métier pour la gestion de la boutique.
"""

from typing import Optional, Tuple
from app.models import Boutique
from app.utils import formater_prix


class BoutiqueService:
    """
    Service gérant les opérations liées à une boutique.
    """
    
    def __init__(self, boutique: Boutique) -> None:
        """
        Initialise le service avec une instance de boutique.
        
        Args:
            boutique: Instance de la boutique à gérer
        """
        self.boutique: Boutique = boutique
    
    def calculer_prix_ttc(self) -> float:
        """
        Calcule le prix TTC d'un produit.
        
        Returns:
            float: Prix TTC du produit
        """
        return self.boutique.prix_unitaire * (1 + self.boutique.tva)
    
    def calculer_valeur_stock(self) -> float:
        """
        Calcule la valeur totale du stock HT.
        
        Returns:
            float: Valeur totale du stock
        """
        return self.boutique.prix_unitaire * self.boutique.quantite_stock
    
    def calculer_valeur_stock_ttc(self) -> float:
        """
        Calcule la valeur totale du stock TTC.
        
        Returns:
            float: Valeur totale du stock TTC
        """
        return self.calculer_prix_ttc() * self.boutique.quantite_stock
    
    def afficher_resume(self) -> None:
        """
        Affiche un résumé des calculs pour la boutique.
        """
        prix_ttc = self.calculer_prix_ttc()
        valeur_stock_ht = self.calculer_valeur_stock()
        valeur_stock_ttc = self.calculer_valeur_stock_ttc()
        
        print(f"\n{'='*50}")
        print(f"RÉSUMÉ - {self.boutique.nom_boutique}")
        print(f"{'='*50}")
        print(f"Prix unitaire HT: {formater_prix(self.boutique.prix_unitaire)}")
        print(f"Prix unitaire TTC: {formater_prix(prix_ttc)}")
        print(f"Valeur du stock HT: {formater_prix(valeur_stock_ht)}")
        print(f"Valeur du stock TTC: {formater_prix(valeur_stock_ttc)}")
        print(f"{'='*50}\n")
    
    def valider_quantite_achat(self, quantite_str: str) -> Tuple[bool, Optional[int], Optional[str]]:
        """
        Valide la quantité saisie par l'utilisateur.
        
        Args:
            quantite_str: Chaîne de caractères saisie par l'utilisateur
        
        Returns:
            Tuple[bool, Optional[int], Optional[str]]: 
                - bool: True si valide, False sinon
                - Optional[int]: La quantité convertie si valide, None sinon
                - Optional[str]: Message d'erreur si invalide, None sinon
        """
        # Vérifier si la chaîne est vide
        if not quantite_str or quantite_str.isspace():
            return False, None, "La saisie ne peut pas être vide."
        
        # Tentative de conversion en entier
        try:
            quantite: int = int(quantite_str)
        except ValueError:
            return False, None, f"'{quantite_str}' n'est pas un nombre entier valide."
        
        # Vérifier que la valeur est strictement positive
        if quantite <= 0:
            return False, None, f"La quantité doit être strictement positive (valeur saisie: {quantite})."
        
        # Vérifier que la quantité ne dépasse pas le stock disponible
        if quantite > self.boutique.quantite_stock:
            return (
                False, 
                None, 
                f"Stock insuffisant! Quantité demandée: {quantite}, "
                f"Stock disponible: {self.boutique.quantite_stock}."
            )
        
        # Vérifier que le client a assez d'argent
        montant_ttc_estime: float = self.calculer_prix_ttc() * quantite
        if montant_ttc_estime > self.boutique.compte_client:
            return (
                False,
                None,
                f"Solde insuffisant! Montant à payer: {formater_prix(montant_ttc_estime)}, "
                f"Solde disponible: {formater_prix(self.boutique.compte_client)}."
            )
        
        # Tout est valide
        return True, quantite, None
    
    def effectuer_achat(self, quantite: int) -> dict:
        """
        Effectue un achat complet : calculs, mise à jour des stocks et des comptes.
        
        Args:
            quantite: Quantité à acheter
        
        Returns:
            dict: Dictionnaire contenant tous les détails de la transaction
        """
        prix_unitaire_ht: float = self.boutique.prix_unitaire
        prix_unitaire_ttc: float = self.calculer_prix_ttc()
        montant_ht: float = prix_unitaire_ht * quantite
        montant_ttc: float = prix_unitaire_ttc * quantite
        tva_montant: float = montant_ttc - montant_ht
        
        # Sauvegarder les valeurs avant modification
        stock_avant: int = self.boutique.quantite_stock
        compte_client_avant: float = self.boutique.compte_client
        compte_boutique_avant: float = self.boutique.compte_boutique
        
        # Mettre à jour le stock
        self.boutique.quantite_stock -= quantite
        
        # Débiter le compte client
        self.boutique.compte_client -= montant_ttc
        
        # Encaisser dans le compte boutique
        self.boutique.compte_boutique += montant_ttc
        
        # Retourner un dictionnaire avec toutes les informations
        return {
            "quantite": quantite,
            "prix_unitaire_ht": prix_unitaire_ht,
            "prix_unitaire_ttc": prix_unitaire_ttc,
            "montant_ht": montant_ht,
            "montant_ttc": montant_ttc,
            "tva_montant": tva_montant,
            "stock_avant": stock_avant,
            "stock_apres": self.boutique.quantite_stock,
            "compte_client_avant": compte_client_avant,
            "compte_client_apres": self.boutique.compte_client,
            "compte_boutique_avant": compte_boutique_avant,
            "compte_boutique_apres": self.boutique.compte_boutique
        }
    
    def afficher_recapitulatif_achat(self, transaction: dict) -> None:
        """
        Affiche un récapitulatif clair de la transaction.
        
        Args:
            transaction: Dictionnaire contenant les détails de la transaction
        """
        print(f"\n{'='*60}")
        print(f"{'RÉCAPITULATIF DE LA TRANSACTION'.center(60)}")
        print(f"{'='*60}\n")
        
        print(f"📦 DÉTAILS DE L'ACHAT")
        print(f"   Produit: {self.boutique.produit}")
        print(f"   Quantité achetée: {transaction['quantite']}")
        print(f"   Prix unitaire HT: {formater_prix(transaction['prix_unitaire_ht'])}")
        print(f"   Prix unitaire TTC: {formater_prix(transaction['prix_unitaire_ttc'])}")
        
        print(f"\n💰 MONTANTS")
        print(f"   Montant HT: {formater_prix(transaction['montant_ht'])}")
        print(f"   TVA ({self.boutique.tva * 100}%): {formater_prix(transaction['tva_montant'])}")
        print(f"   Montant TTC: {formater_prix(transaction['montant_ttc'])}")
        
        print(f"\n📊 STOCK")
        print(f"   Stock avant: {transaction['stock_avant']} unités")
        print(f"   Stock après: {transaction['stock_apres']} unités")
        print(f"   Variation: -{transaction['quantite']} unités")
        
        print(f"\n💳 COMPTE CLIENT")
        print(f"   Solde avant: {formater_prix(transaction['compte_client_avant'])}")
        print(f"   Débit: -{formater_prix(transaction['montant_ttc'])}")
        print(f"   Solde après: {formater_prix(transaction['compte_client_apres'])}")
        
        print(f"\n🏪 COMPTE BOUTIQUE")
        print(f"   Solde avant: {formater_prix(transaction['compte_boutique_avant'])}")
        print(f"   Crédit: +{formater_prix(transaction['montant_ttc'])}")
        print(f"   Solde après: {formater_prix(transaction['compte_boutique_apres'])}")
        
        print(f"\n{'='*60}")
        print(f"{'✓ TRANSACTION RÉUSSIE'.center(60)}")
        print(f"{'='*60}\n")
    
    def verifier_stock_faible(self, seuil: int = 10) -> None:
        """
        Vérifie le niveau du stock et affiche des avertissements selon les conditions.
        
        Args:
            seuil: Seuil en dessous duquel le stock est considéré comme faible (par défaut: 10)
        """
        stock_actuel: int = self.boutique.quantite_stock
        prix_unitaire: float = self.boutique.prix_unitaire
        
        # Condition VIII : stock entre 10 et 15 (exclus) ET prix > 5
        if 10 < stock_actuel < 15 and prix_unitaire > 5:
            print(f"⚠️  {'!! ATTENTION PRODUIT PRESQUE EN RUPTURE !!'.center(60)} ⚠️")
            print(f"   Stock restant: {stock_actuel} unités")
            print(f"   Prix unitaire: {formater_prix(prix_unitaire)}")
            print()
        # Condition VII : stock < 10
        elif stock_actuel < seuil:
            print(f"⚠️  {'!! STOCK BIENTÔT ÉPUISÉ !!'.center(60)} ⚠️")
            print(f"   Stock restant: {stock_actuel} unités (seuil: {seuil})")
            print()
    
    def afficher_facture(self, quantite: int) -> None:
        """
        Affiche une facture formatée pour un achat.
        
        Args:
            quantite: La quantité achetée
        """
        # Calculs
        prix_unitaire_ht: float = self.boutique.prix_unitaire
        prix_unitaire_ttc: float = self.calculer_prix_ttc()
        montant_ht: float = prix_unitaire_ht * quantite
        montant_tva: float = montant_ht * self.boutique.tva
        montant_ttc: float = montant_ht + montant_tva
        
        # Largeur de la facture
        largeur: int = 84
        separateur: str = "-" * largeur
        
        # En-tête
        print(f"\n{separateur}")
        print(f"{self.boutique.nom_boutique}")
        print(f"{separateur}")
        
        # Ligne d'en-tête des colonnes
        print(f"{'Produit':<50} {'qté':>10} {'ht':>20}")
        
        # Ligne du produit avec points de suspension
        produit_cap: str = self.boutique.produit.capitalize()
        points: str = "." * (50 - len(produit_cap) - 1)
        print(f"{produit_cap} {points} {quantite:>10} {montant_ht:>20.2f}")
        
        # Ligne vide
        print()
        
        # Totaux alignés à droite
        print(f"{'Total HT :':>64} {montant_ht:>16.2f}")
        print(f"{'TVA :':>64} {montant_tva:>16.2f}")
        print(f"{'Total TTC :':>64} {montant_ttc:>16.2f}")
        
        # Pied de page
        print(f"{separateur}\n")

