import Pole
import random
import OgonWeza
import Smakolyk

class Waz(Pole.Pole):

    def __init__(self,x,y,plansza,gra):
        self.x=random.randrange(0,x)
        self.y=random.randrange(0,y)
        self.ogonweza=[]
        self.koniecX=self.x
        self.koniecY=self.y
        self.dlugosc=0
        self.kierunek=random.randrange(0,4)
        self.plansza=plansza
        self.wydluzWezaWNastTurze=False
        self.wydluz=False
        self.gra=gra

    def RysujPole(self):
        print("* ",end="")

    def ZmienKierunek(self,kierunek):
        if kierunek=='up' and self.kierunek!=1:
            self.kierunek=0
        elif kierunek=='down' and self.kierunek!=0:
            self.kierunek=1
        elif kierunek=='left' and self.kierunek!=3:
            self.kierunek=2
        elif kierunek=='right' and self.kierunek!=2:
            self.kierunek=3

    def Kolizja(self,nextX,nextY):

        if len(self.ogonweza)!=0:
            self.plansza.Pola[self.ogonweza[-1].x][self.ogonweza[-1].y]=Pole.Pole(self.ogonweza[-1].x,self.ogonweza[-1].y,self.plansza)


        if self.wydluz==True:
            self.wydluzWezaWNastTurze=True
            self.wydluz=False
            self.ogonweza.append(OgonWeza.OgonWeza(self.koniecX, self.koniecY, self.plansza))

        for l in range(len(self.ogonweza)-1, -1, -1):
            if l-1>=0:
                self.ogonweza[l].x=self.ogonweza[l-1].x
                self.ogonweza[l].y = self.ogonweza[l-1].y
            else:
                self.ogonweza[l].x=self.x
                self.ogonweza[l].y=self.y
            self.plansza.Pola[self.ogonweza[l].x][self.ogonweza[l].y]=self.ogonweza[l]




        if type(self.plansza.Pola[nextX][nextY])==Pole.Pole:

            if self.dlugosc==0:
                self.koniecX=nextX
                self.koniecY=nextY
            elif self.dlugosc==1:
                self.koniecX=self.x
                self.koniecY=self.y
            else:
                self.koniecX=self.ogonweza[-1].x
                self.koniecY = self.ogonweza[-1].y

            self.x = nextX
            self.y = nextY
            self.plansza.Pola[nextX][nextY] = self

        elif type(self.plansza.Pola[nextX][nextY])==Smakolyk.Smakolyk:

            if self.dlugosc==0:
                self.koniecX=nextX
                self.koniecY=nextY
            elif self.dlugosc==1:
                self.koniecX=self.x
                self.koniecY=self.y
            else:
                self.koniecX=self.ogonweza[-2].x
                self.koniecY = self.ogonweza[-2].y

            self.wydluz=True
            if self.gra.predkosc!= 0.98:
                self.gra.predkosc+=0.002
            self.dlugosc+=1
            self.gra.score+=10
            self.x = nextX
            self.y = nextY
            self.plansza.Pola[nextX][nextY] = self
            self.gra.smakolyk=Smakolyk.Smakolyk(self.plansza.x,self.plansza.y,self.plansza)
        elif type(self.plansza.Pola[nextX][nextY])==OgonWeza.OgonWeza:
            self.gra.GrajDalej=False





    def WykonajRuch(self):
        self.plansza.Pola[self.x][self.y]=Pole.Pole(self.x,self.y,self.plansza)
        nextX=self.x
        nextY=self.y

        if self.kierunek==0:
            nextY=self.y-1
            if nextY < 0:
                nextY = self.plansza.y - 1

        elif self.kierunek==1:
            nextY=self.y+1
            if nextY > self.plansza.y - 1:
                nextY = 0

        elif self.kierunek==2:
            nextX=self.x-1
            if nextX < 0:
                nextX = self.plansza.x - 1

        elif self.kierunek==3:
            nextX=self.x+1
            if nextX > self.plansza.x - 1:
                nextX = 0
        self.Kolizja(nextX,nextY)

