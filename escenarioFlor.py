'''
En este escenario se evalua la cantidad de victorias y derrotas 
cuando se juega con Flor. Se reunen los datos de las probabilidad de victorias de el Agente 1 
y se cuentan los puntos obtenidos por cada agente.

Para este y todos los casos se considera que el Agente 1 es mano por lo tanto
los empates se contabilizan como victorias para dicho agente
'''

from mazo import Mazo
from agente import Agente

partidaConFlor = True
N=5000
victoriaAgente1 = victoriaAgente2 = cantEmpate =  partidasSinFlor = noQuieroA1 = noQuieroA2 = conFlor = 0
for i in range(N):

    #se crea el mazo y se reparten las cartas
    mazo = Mazo()
    cartasRepartir = mazo.repartir(2)

    #se instancian los agentes y se le asigna un estilo de juego
    agente1 = Agente(True, "Agresivo", cartasRepartir[0:3], partidaConFlor)
    agente2 = Agente(None, "Normal", cartasRepartir[3:6], partidaConFlor)

    if agente1.tieneFlor:
        conFlor += 1
        if agente2.tieneFlor:
            if agente1.envido>agente2.envido:
                victoriaAgente1 += 1
            elif agente1.envido == agente2.envido:
                cantEmpate +=1
            else:
                victoriaAgente2 += 1
        else:
            noQuieroA2 += 1
    else:
        if agente2.tieneFlor:
            conFlor += 1
            noQuieroA1 += 1
        else:
            partidasSinFlor += 1


puntosAgente1 = (victoriaAgente1+cantEmpate)*4+noQuieroA2*3
puntosAgente2 = victoriaAgente2*4+noQuieroA1*3



print(f"\n-----------------------------------------------------") 
print(f"\nCantidad de partidas Jugadas --> {N}")
print(f"\nCantidad de victorias del Agente 1 --> {victoriaAgente1 + cantEmpate}")
print(f"\nCantidad de victorias del Agente 2 --> {victoriaAgente2}")
print(f"\nCantidad de empates --> {cantEmpate}")
print(f"\nCantidad de NO QUIERO Agente 1 --> {noQuieroA1}")
print(f"\nCantidad de NO QUIERO Agente 2 --> {noQuieroA2}")
print(f"\nProbabilidad de victorias del Agente 1 : {round((victoriaAgente1+cantEmpate)*100/(N-partidasSinFlor),2)}%")
print(f"\nCantidad de partidas SinFlor : {partidasSinFlor}")

print(f"\n-----------------------------------------------------") 
print(f"\nCantidad de puntos obtenidos por el Agente 1 --> {puntosAgente1}")
print(f"\nCantidad de puntos obtenidos por el Agente 2 --> {puntosAgente2}")

print(f"\nProcentaje de puntos obtenidos por el Agente 1 --> {round(100*puntosAgente1/(puntosAgente1+puntosAgente2),2)}%")
print(f"\nProcentaje de puntos obtenidos por el Agente 2 --> {round(100*puntosAgente2/(puntosAgente1+puntosAgente2),2)}%")