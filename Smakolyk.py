import Pole
import random


class Smakolyk(Pole.Pole):

    def __init__(self, x, y, plansza):
        self.plansza = plansza
        self.GenerujSmakolyk(x, y)

    def RysujPole(self):
        print("S ", end="")

    def GenerujSmakolyk(self, x, y):
        self.x = random.randrange(0, x)
        self.y = random.randrange(0, y)
        while type(self.plansza.Pola[self.x][self.y]) != Pole.Pole:
            self.x = random.randrange(0, x)
            self.y = random.randrange(0, y)

        self.plansza.Pola[self.x][self.y] = self

