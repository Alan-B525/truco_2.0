'''
En este escenario se evalua la cantidad de victorias y derrotas 
cuando el Agente1 nunca canta envido,y su estilo de juego es AGRESIVO contra un Agente 2 
que tiene un estlilo de juego NORMAL

Para este y todos los casos se considera que el Agente 1 es mano por lo tanto
los empates se contabilizan como victorias para dicho agente
'''

from mazo import Mazo
from agente import Agente

partidaConFlor = False
N=5000
victoriaAgente1 = victoriaAgente2 = cantEmpate= cantNoQuiero = partidasSinEnvido = cantNoquieroAgente1 = 0
partidasConEnvido = 0
for i in range(N):

    #se crea el mazo y se reparten las cartas
    mazo = Mazo()
    cartasRepartir = mazo.repartir(2)

    #se instancian los agentes y se le asigna un estilo de juego
    agente1 = Agente(True, "Agresivo", cartasRepartir[0:3], partidaConFlor)
    agente2 = Agente(None, "Normal", cartasRepartir[3:6], partidaConFlor)

    #caso en el que el agente 2 analiza si canta envido:
    if agente2.respuesta(): #agente2 propone envido
        partidasConEnvido += 1
        if agente1.respuesta(): #agente 1 acepta
            if(agente1.envido<agente2.envido):
                victoriaAgente2 += 1

            if(agente1.envido>agente2.envido):
                victoriaAgente1 += 1

            if(agente1.envido==agente2.envido):
                cantEmpate +=1
        else:
            cantNoquieroAgente1 += 1        
    else:
        partidasSinEnvido += 1    

puntosAgente1 = (victoriaAgente1+cantEmpate)*2
puntosAgente2 = 2*victoriaAgente2+cantNoquieroAgente1

print(f"\n-----------------------------------------------------") 
print(f"\nCantidad de partidas Jugadas --> {N}")
print(f"\nEstilo del Agente 1 --> AGRESIVO")
print(f"\nCantidad de victorias del Agente 1 --> {victoriaAgente1 + cantEmpate}")
print(f"\nCantidad de victorias del Agente 2 --> {victoriaAgente2}")
print(f"\nCantidad de empates --> {cantEmpate}")
print(f"\nCantidad de NO QUIERO Agente 1 --> {cantNoquieroAgente1}")
print(f"\nCantidad de Envidos del Agente 2 --> {partidasConEnvido}")
print(f"\nProbabilidad de victorias del Agente 1 : {round((victoriaAgente1+cantEmpate)*100/(N-partidasSinEnvido-cantNoquieroAgente1),2)}%")

print(f"\n-----------------------------------------------------") 
print(f"\nCantidad de puntos obtenidos por el Agente 1 --> {puntosAgente1}")
print(f"\nCantidad de puntos obtenidos por el Agente 2 --> {puntosAgente2}")

print(f"\nProcentaje de puntos obtenidos por el Agente 1 --> {round(100*puntosAgente1/(puntosAgente1+puntosAgente2),2)}%")
print(f"\nProcentaje de puntos obtenidos por el Agente 2 --> {round(100*puntosAgente2/(puntosAgente1+puntosAgente2),2)}%")