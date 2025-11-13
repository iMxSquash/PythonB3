class Ma_Classe:
    def __new__(cls, *args, **kwargs):
        print("appel de __new__ pour Ma_Classe")
        instance = super(Ma_Classe, cls).__new__(cls)
        return instance
    
    def __init__(self, valeur: int, *args, **kwargs):
        print("appel de __init__ pour Ma_Classe")
        self.props = args[0]
        
    def __del__(self):
        print("appel de __del__ pour Ma_Classe")