from random import choice

class Lemming:
    def __init__(self, jeu):
        self.d = choice((1, -1))  # Lemming au hasard soit à gauche soit à droite
        self.j = jeu
        self.l, self.c = jeu.get_entree()

    def __str__(self):
        return '>' if self.d == 1 else '<'

    def action(self):
        pass
