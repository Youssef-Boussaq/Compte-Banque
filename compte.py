class Compte :
    _numéro=0
    def __init__(self, pro , sold , dateoverture ):
        self.__pro= pro
        self.__sold = sold
        self.__dateoverture = dateoverture 
        Compte._numéro+=1
        
        
    @property
    def getpro(self):
        return self.__pro
    
    
    @property
    def getsold(self):
        return self.__sold
    
    
    @property
    def getdate(self):
        return self.__dateoverture
    
    def __str__(self) :
        return "the compte: {} ; \nthe solde is: {} ; \nthe compte opening in: {}".format( self.__pro ,  self.__sold , self.__dateoverture )
