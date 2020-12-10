class Case:
    def __init__(self,terrain,lemming=None):
        self.ter=terrain #    
        self.lem=lemming #on set le truc 
     
    def __libre(self):
        if self.ter==None:
            return False
        else:
            return True
    
    def depart(self):
        pass
    
    def arrivee(self,lem):
        pass
    
    def __str__(self):
        pass
    
