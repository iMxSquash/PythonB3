class Paypal:
    def pay(self, amount: float) -> None:
        print(f"[Paypal] Paiement de {amount}€ accepté")

    def refund(self, amount: float) -> None:
        print(f"[Paypal] Remboursement de {amount}€")