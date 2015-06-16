#! /usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul32 import ustawienia, losujliczby, pobierztypy

# program główny

# ustawienia gry
nick, ileliczb, maksliczba, ilerazy = ustawienia()

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
for i in range(ilerazy):
    typy = pobierztypy(ileliczb, maksliczba)
    trafione = wyniki(set(liczby), typy)

print "Wylosowane liczby:",liczby
