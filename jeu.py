class Case:
    def __init__(self, terrain='vide', lemming=None):
        self.terrain = terrain
        self.lemming = lemming

    def libre(self):
        return self.lemming is not None
    
    def depart(self):
        lemming = self.lemming
        print(lemming)
        self.lemmings = None
        print(lemming)
        return lemming

class Jeu:
    def __init__(self):
        self.lemmings = []
        self.grotte = [[Case(), Case(), Case()], 
                       [Case(), Case(), Case()]]
