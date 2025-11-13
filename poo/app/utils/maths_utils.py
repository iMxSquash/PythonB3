def add(a, b):
    """Additionne deux nombres.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """Soustrait deux nombres.

    Args:
        a (int or float): Le premier nombre.
        b (int or float): Le deuxième nombre à soustraire du premier.

    Returns:
        int or float: La différence entre a et b.
    """
    return a - b

def multiply(a, b):
    """Multiplie deux nombres.

    Args:
        a (int or float): Le premier nombre.
        b (int or float): Le deuxième nombre.

    Returns:
        int or float: Le produit de a et b.
    """
    return a * b

def divide(a, b):
    """Divise deux nombres.

    Args:
        a (int or float): Le numérateur.
        b (int or float): Le dénominateur.

    Returns:
        int or float: Le quotient de a divisé par b.

    Raises:
        ValueError: Si b est égal à zéro.
    """
    if b == 0:
        raise ValueError("Le dénominateur ne peut pas être zéro.")
    return a / b