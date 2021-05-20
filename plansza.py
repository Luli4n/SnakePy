import Pole

class Plansza:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.Pola = [[0 for m in range(y)] for n in range(x)]
        for m in range(0,y):
            for n in range(0,x):
                self.Pola[n][m]=Pole.Pole(n,m,self)

    def GetSzerokosc(self):
        return self.x

    def GetWysokosc(self):
        return self.y

    def SetSzerokosc(self,x):
        self.x=x

    def SetWysokosc(self,y):
        self.y=y
