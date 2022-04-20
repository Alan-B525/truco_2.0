from carta import Carta
from random import sample

class Mazo:
    palos = ["e", "b", "c", "o"]
    cartas = []

    for p in palos:
        for n in range(1,13):
            if n!=8 and n!=9:
                carta = Carta(n,p)
                cartas.append(carta)

    def repartir(self, cantJugadores) -> list: #retorna una lista con las cartas necesarias para todos los jugadores
        cartasRepartir = []

        cartasRepartir = sample(__class__.cartas, 3*cantJugadores) #se utilizo este metodo porque randint() fallaba

        return cartasRepartir

'''
mazo = Mazo()
cartasRepartir = mazo.repartir(2)
cartasA1 = cartasRepartir[0:3] #hay que tener cuidado donde cortar las listas
cartasA2 = cartasRepartir[3:6]

print("Las 3 cartas del Agente 1:\n")
for c1 in cartasA1:
    print(c1)

print("Las 3 cartas del Agente 2:\n")
for c2 in cartasA2:
    print(c2)
'''