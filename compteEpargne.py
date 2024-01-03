from compte import Compte
class compteEpargne(Compte):
    def __init__(self , pro , sold , dateoverture , mda ):
        super().__init__( pro , sold , dateoverture)
        self.__mda = mda


    def getmda(self):
        return self.__mda
    
    
    def __str__(self):
        return  super().__str__() + f"\nma: {self.__mda}"
bb=compteEpargne("ghs",55,55,66)
print(bb)
print(Compte._numéro)
