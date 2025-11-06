# app/utils.py

def saluer(nom: str) -> None:
    """
    function to greet 
    """
    print(f"Bonjour, {nom} !")
    
    def addition_multiple(*args: int) -> int:
        """
        function to add multiple integers
        """
        return sum(args)