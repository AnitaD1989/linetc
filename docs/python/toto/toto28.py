#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

try:
    ileliczb = int(raw_input("Podaj ilość typowanych liczb: "))
    maksliczba = int(raw_input("Podaj maksymalną losowaną liczbę: "))
    if ileliczb > maksliczba:
        print "Błędne dane!"
        exit()
except:
    print "Błędne dane!"
    exit()

liczby = []
i = 0
while i < int(ileliczb):
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

for i in range(3):
    print "Wytypuj",ileliczb,"z",maksliczba," liczb: "
    typy = set()
    i = 0
    while i < ileliczb:
        typ = int(raw_input("Podaj liczbę "+str(i+1)+": "))
        if typ not in typy:
            typy.add(typ)
            i = i + 1

    trafione = set(liczby) & typy
    if trafione:
        print "\nIlość trafień: ",len(trafione)
        print "Trafione liczby: ",trafione
    else:
        print "Brak trafień. Spróbuj jeszcze raz!"

    print "\n"+"x"*40+"\n" # wydrukuj 40 znaków x

print "Wylosowane liczby:",liczby
