from random import choice

from blessed import Terminal
from colorama import init, Fore

init()


class Jeu:
    def __init__(self):
        self.lemmings: list[Lemming] = []
        self.grotte = []
        self.__entree = (0, 0)
        self.__sortie = (0, 0)
        self.__terminal = Terminal()
        self.colors = {'#': Fore.BLUE,
                       'O': Fore.RED,
                       'E': Fore.RED,
                       ' ': Fore.WHITE,
                       '>': Fore.GREEN,
                       '<': Fore.GREEN}

        with open('grotte.txt') as f:
            grilles = f.read().split('.')

        grilles = [grille.split('\n') for grille in grilles]
        grille = choice(grilles)
        self.gridsize = [len(max(grille, key=len)) - 1, len(grille) - 1]

        for line_num, line in enumerate(grille):
            line_list = []
            while len(line) < self.gridsize[0]:
                line += ' '
            for num_colonne, case in enumerate(line):
                if case == 'E':
                    self.__entree = (num_colonne, line_num)
                elif case == 'O':
                    self.__sortie = (num_colonne, line_num)
                line_list.append(Case(case))
            self.grotte.append(line_list)

    def get_entree(self):
        return self.__entree

    def get_sortie(self):
        return self.__sortie

    def afficher(self):
        for line in self.grotte:
            print(''.join(f'{self.colors[str(case)]}{str(case)}' for case in line))

    def tour(self):
        for lemming in self.lemmings:
            lemming.action()

    def demarre(self):
        with self.__terminal.cbreak():
            self.afficher()
            val = ''
            while val.lower() != 'q':
                print('[1] Pour ajouter un lemming\n'
                      '[Entrer] Pour faire passer un tour\n'
                      '[q] Pour quitter\n')
                val = self.__terminal.inkey()
                if str(val) == '1':
                    self.tour()
                    self.lemmings.append(Lemming(self))
                    self.grotte[self.get_entree()[1]][self.get_entree()[0]].arrivee(Lemming(self))
                    self.afficher()

                elif val.name == 'KEY_ENTER':
                    self.tour()
                    self.afficher()

            exit(f'{Fore.RED}Ciao!')


class Lemming:
    def __init__(self, jeu: Jeu):
        self.d = choice((1, -1))
        self.j = jeu
        self.c, self.l = jeu.get_entree()

    def __str__(self):
        return '>' if self.d == 1 else '<'

    def sort(self):
        self.j.lemmings.remove(self)

    def action(self):
        grotte = self.j.grotte
        grotte[self.l][self.c].depart(entree=(self.c, self.l) == self.j.get_entree())
        if grotte[self.l + 1][self.c].terrain in [' ', 'O'] and grotte[self.l + 1][self.c].est_libre():
            self.l += 1

        elif grotte[self.l][self.c + self.d].terrain in [' ', 'O'] and grotte[self.l][self.c + self.d].est_libre():
            self.c += self.d

        elif grotte[self.l][self.c + self.d].terrain == '#' or not grotte[self.l][self.c + self.d].est_libre():
            self.d *= -1

        grotte[self.l][self.c].arrivee(self)


class Case:
    def __init__(self, terrain=' ', lemming=None):
        self.terrain = terrain
        self.lemming = lemming

    def est_libre(self):
        return self.lemming is None

    def depart(self, entree=False):
        if entree:
            self.terrain = 'E'
        else:
            self.terrain = ' '
        self.lemming = None

    def arrivee(self, lemming: Lemming):
        if self.terrain == 'O':
            lemming.sort()
        else:
            self.lemming = lemming

    def __str__(self):
        return self.terrain if self.est_libre() else str(self.lemming)


if __name__ == '__main__':
    j = Jeu()
    j.demarre()
