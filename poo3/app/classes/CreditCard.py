class CreditCard:
    def pay(self, amount: float) -> None:
        print(f"[Carte bancaire] Paiement de {amount}€ accepté")

    def refund(self, amount: float) -> None:
        print(f"[Carte bancaire] Remboursement de {amount}€")
