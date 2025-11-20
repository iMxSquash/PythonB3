from typing import Protocol

class PaymentMethod(Protocol):
    def pay(self, amount: float) -> None:
        """pay effectue un paiement d'un montant spécifié.

        Args:
            amount (float): Le montant à payer.
        """
        ...

    def refund(self, amount: float) -> None:
        """refund effectue un remboursement d'un montant spécifié.

        Args:
            amount (float): Le montant à rembourser.
        """
        ...