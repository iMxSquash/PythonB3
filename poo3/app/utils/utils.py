from pprint import pprint

def show(variable: any, name: str = '') -> None:
    """Petite fonction d'affichage qui permet de regarder à l'intérieur des objets ou des variables dans la console.

    Args:
        variable (any): La variable à afficher.
        name (str, optional): Le nom de la variable. Par défaut, une chaîne vide.
    """
    if hasattr(variable, '__dict__'):
        if name:
            print(f"Objet observé : {name} (type: {type(variable)})")
            class_name = type(variable).__name__
            print(f"Objet de classe: {class_name}")
            
            #propriétés de l'objet
            class_attributes = {
                key: value
                for key, value in type(variable).__dict__.items()
                if not key.startswith('__') and not callable(value)
            }
            
            for elem in class_attributes:
                if isinstance(class_attributes[elem], classmethod):
                    class_attributes[elem] = "<Méthode de classe>"
                if isinstance(class_attributes[elem], property):
                    class_attributes[elem] = "<Propriété>"
                if isinstance(class_attributes[elem], staticmethod):
                    class_attributes[elem] = "<Méthode statique>"
                
                if len(class_attributes) > 0:
                    print("\nPropriétés de la classe:")
                    pprint(class_attributes)
            
            # Propriétés de l'instance
            print("\nPropriétés de l'instance:")
            properties = vars(variable)
            pprint(properties)
            
            # Méthodes de l'objet
            print("\nMéthodes de l'objet:")
            methods = [method for method in dir(variable) if callable(getattr(variable, method)) and not method.startswith("__")]
            pprint(methods)
            
        else: # ce n'est pas un objet
            print("Variable observée:")
            pprint(variable)
            