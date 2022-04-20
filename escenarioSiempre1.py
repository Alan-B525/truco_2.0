'''
En este escenario se evalua la cantidad de victorias y derrotas 
cuando el Agente1 siempre canta envido contra un Agente 2 
que tiene un estlilo de juego CAUTELOSO

Para este y todos los casos se considera que el Agente 1 es mano por lo tanto
los empates se contabilizan como victorias para dicho agente
'''

from mazo import Mazo
from agente import Agente

partidaConFlor = False
N=5000
victoriaAgente1 = victoriaAgente2 = cantEmpate= cantNoQuiero = 0

for i in range(N):

    #se crea el mazo y se reparten las cartas
    mazo = Mazo()
    cartasRepartir = mazo.repartir(2)

    #se instancian los agentes y se le asigna un estilo de juego
    agente1 = Agente(True, "Agresivo", cartasRepartir[0:3], partidaConFlor)
    agente2 = Agente(None, "Cauteloso", cartasRepartir[3:6], partidaConFlor)

    #caso en el que el agente 1 siempre canta envido:
    if agente2.respuesta():

        #comparar valores de los envidos y sumar victorias correspondientes

        if(agente1.envido<agente2.envido):
            victoriaAgente2 += 1

        if(agente1.envido>agente2.envido):
            victoriaAgente1 += 1

        if(agente1.envido==agente2.envido):
            cantEmpate +=1
    else:
        cantNoQuiero += 1    

puntosAgente1 = (victoriaAgente1+cantEmpate)*2+cantNoQuiero
puntosAgente2 = 2*victoriaAgente2

print(f"\n-----------------------------------------------------") 
print(f"\nCantidad de partidas Jugadas --> {N}")
print(f"\nEstilo del Agente 2 --> CAUTELOSO")
print(f"\nCantidad de victorias del Agente 1 --> {victoriaAgente1 + cantEmpate}")
print(f"\nCantidad de victorias del Agente 2 --> {victoriaAgente2}")
print(f"\nCantidad de empates --> {cantEmpate}")
print(f"\nCantidad de No QUIERO --> {cantNoQuiero}")

print(f"\nProbabilidad de victorias del Agente 1 : {round((victoriaAgente1+cantEmpate)*100/(N-cantNoQuiero),2)}%")

print(f"\n-----------------------------------------------------") 
print(f"\nCantidad de puntos obtenidos por el Agente 1 --> {puntosAgente1}")
print(f"\nCantidad de puntos obtenidos por el Agente 2 --> {puntosAgente2}")

print(f"\nProcentaje de puntos obtenidos por el Agente 1 --> {round(100*puntosAgente1/(puntosAgente1+puntosAgente2),2)}%")
print(f"\nProcentaje de puntos obtenidos por el Agente 2 --> {round(100*puntosAgente2/(puntosAgente1+puntosAgente2),2)}%")