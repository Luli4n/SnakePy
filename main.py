# coding=utf-8

import plansza
import os
import Waz
import random
import time
import Smakolyk

from pynput import keyboard

class Gra:

    def __init__(self):
        self.GrajDalej=True
        x=int(input("Podaj szerokość: "))
        y=int(input("Podaj wysokosc: "))
        self.plansza=plansza.Plansza(x,y)
        self.waz=Waz.Waz(x,y,self.plansza,self)
        self.plansza.Pola[self.waz.x][self.waz.y]=self.waz
        self.smakolyk=Smakolyk.Smakolyk(x,y,self.plansza)
        self.predkosc = 0.8
        self.score = 0
        self.RozgrywajTure()


    def on_press(self,key):
        if key == keyboard.Key.esc:
            self.GrajDalej=False
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if k in ['left', 'right','up','down']:  # keys of interest
            self.waz.ZmienKierunek(k)

            return True  # stop listener; remove this if want more keys

    def Clear(self):
        os.system('cls')

    def RysujSwiat(self):
        self.Clear()
        for y in range(0,self.plansza.GetWysokosc()):
            for x in range(0,self.plansza.GetSzerokosc()):
                self.plansza.Pola[x][y].RysujPole()
            print("|")
        print("- "*self.plansza.GetSzerokosc())


    def RozgrywajTure(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()  # start to listen on a separate thread

        while(self.GrajDalej):

            time.sleep(1-self.predkosc)
            self.waz.WykonajRuch()
            self.RysujSwiat()
            print("Twój aktualny wynik to: " + str(self.score))

        print("PRZEGRAŁEŚ!!!!!")


game=Gra()

