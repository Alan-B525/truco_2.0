from carta import Carta
from mazo import Mazo
from agente import Agente

partidaConFlor = False

mazo = Mazo()
cartasRepartir = mazo.repartir(2)

#agente1 = Agente(True, "Agresivo", cartasRepartir[0:3], partidaConFlor)
#agente2 = Agente(None, "Agresivo", cartasRepartir[3:6], partidaConFlor)

#testeo
cartasA1 = cartasRepartir[0:3]
cartasA2 = cartasRepartir[3:6]

agente1 = Agente(True, "Agresivo", cartasA1, partidaConFlor)
agente2 = Agente(None, "Agresivo", cartasA2, partidaConFlor)

print("\nCartas del agente 1: ")
for c in cartasA1:
    print(c)

print("\nCartas del agente 2: ")
for c in cartasA2:
    print(c)

print(f"\nEl envido del agente 1 es --> {agente1.envido}")
print(f"\ntieneFlor del agente 1 arroja {agente1.tieneFlor}")
print(f"\nEl envido del agente 2 es --> {agente2.envido}")
print(f"\ntieneFlor del agente 1 arroja {agente2.tieneFlor}")

#------------------------------------------------------------
#testeo del funcionamiento del calculo de flor y partida con flor
partidaConFlor = True

cartasAgente3 = []
carta3A= Carta(1,'b')
carta3B= Carta(3,'c')
carta3C= Carta(10,'b')
cartasAgente3.append(carta3A)
cartasAgente3.append(carta3B)
cartasAgente3.append(carta3C)

cartasAgente4 = []
carta4A= Carta(5,'e')
carta4B= Carta(6,'e')
carta4C= Carta(7,'e')
cartasAgente4.append(carta4A)
cartasAgente4.append(carta4B)
cartasAgente4.append(carta4C)

agente3 = Agente(True, "Agresivo", cartasAgente3, partidaConFlor)
agente4 = Agente(None, "Agresivo", cartasAgente4, partidaConFlor)

print("\nCartas del agente 3: ")
for c in cartasAgente3:
    print(c)

print("\nCartas del agente 4: ")
for c in cartasAgente4:
    print(c)

print(f"\nEl envido del agente 3 es --> {agente3.envido}")
print(f"\ntieneFlor del agente 3 arroja {agente3.tieneFlor}")
print(f"\nEl envido del agente 4 es --> {agente4.envido}")
print(f"\ntieneFlor del agente 4 arroja {agente4.tieneFlor}")