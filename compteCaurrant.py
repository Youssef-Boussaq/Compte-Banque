from compte import Compte
class compteCourant(Compte):
    def __init__(self , pro , sold , dateoverture , intret ):
        super().__init__( pro , sold , dateoverture)
        self.__intret = intret


    @property
    def getintret(self):
        return self.__intret
    



    
    def __str__(self):
        return  super().__str__() + f"\nintret: {self.__intret}"