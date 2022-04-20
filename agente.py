import random
from mazo import Mazo

class Agente:
    idAgente = 0

    #matriz de probabilidades de los estilos de juego, solo lectura 
    matrizProbabilidad = [
                         [0.00, 0.00, 0.00, ], #0 --> fila 0
                         [0.00, 0.00, 0.00, ], #1 --> fila 1
                         [0.00, 0.00, 0.01, ], #2 --> fila 2 
                         [0.00, 0.00, 0.02, ], #3 --> fila 3
                         [0.00, 0.00, 0.05, ], #4 --> fila 4
                         [0.00, 0.01, 0.10, ], #5 --> fila 5
                         [0.00, 0.02, 0.15, ], #6 --> fila 6
                         [0.00, 0.04, 0.20, ], #7 --> fila 7
                         [0.01, 0.10, 0.50, ], #20 --> fila 8
                         [0.03, 0.10, 0.53, ], #21 --> fila 9
                         [0.05, 0.15, 0.59, ], #22 --> fila 10
                         [0.07, 0.20, 0.67, ], #23 --> fila 11
                         [0.10, 0.25, 0.81, ], #24 --> fila 12
                         [0.15, 0.33, 0.88, ], #25 --> fila 13
                         [0.20, 0.43, 0.92, ], #26 --> fila 14
                         [0.30, 0.58, 0.98, ], #27 --> fila 15
                         [0.35, 0.69, 0.99, ], #28 --> fila 16
                         [0.50, 0.86, 1.00, ], #29 --> fila 17
                         [0.75, 0.97, 1.00, ], #30 --> fila 18
                         [0.85, 1.00, 1.00, ], #31 --> fila 19
                         [0.95, 1.00, 1.00, ], #32 --> fila 20
                         [1.00, 1.00, 1.00, ],] #33 --> fila 21
                         

    def __init__(self, iniciativa, estiloJugador, cartas, partidaConFlor): #los parametros son (bool, string, lista, bool) 
        __class__.idAgente = __class__.idAgente + 1
        self.__id = __class__.idAgente
        self.__iniciativa = iniciativa
        self.__estiloJugador = estiloJugador
        self.__cartas = cartas
        self.__partidaConFlor = partidaConFlor
        self.__tieneFlor= self.__tenerFlor(cartas) #es bool
        self.__envido = self.__calcularEnvido(cartas) #es int

    # __iniciativa es solo para el Agente1 (True para pedir siempre, False para no pedir y esperar) 
    # __estiloJugador es para los demas Agentes y cuando la iniciativa del Agente1 esta en False 
    # __cartas es la lista de las 3 cartas repartidas
    # __partidaConFlor es para informar si la partida contempla el caso de Flor
    # __tieneFlor es para determinar si el agente tiene flor

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def iniciativa(self):
        return self.__iniciativa

    @iniciativa.setter
    def iniciativa(self, iniciativa):
        self.iniciativa = iniciativa

    @property
    def estiloRespuesta(self):
        return self.__estiloJugador

    @estiloRespuesta.setter
    def estiloRespuesta(self, estiloRespuesta):
        self.__estiloJugador = estiloRespuesta

    @property
    def cartas(self):
        return self.__cartas

    @cartas.setter
    def cartas(self, cartas):
        self.__cartas = cartas

    @property
    def envido(self):
        return self.__envido

    @envido.setter
    def envido(self, envido):
        self.__envido = envido

    @property
    def flor(self):
        return self.__flor

    @flor.setter
    def flor(self, envido):
        self.__flor = envido

    @property
    def partidaConFlor(self):
        return self.__partidaConFlor

    @partidaConFlor.setter
    def partidaConFlor(self, partidaConFlor):
        self.__partidaConFlor = partidaConFlor

    @property
    def tieneFlor(self):
        return self.__tieneFlor

    @tieneFlor.setter
    def tieneFlor(self, tieneFlor):
        self.__tieneFlor = tieneFlor

    #-----------------------------------------------------------------------------------------------------------------

    def __tenerFlor(self, cartas) -> bool:
        if cartas[0].palo == cartas[1].palo and cartas[0].palo == cartas[2].palo:
            return True
        else:
            return False

    def __calcularEnvido(self, cartas) -> int:
        tanto = cantEspada = cantBasto = cantOro = cantCopa = 0

        if self.tieneFlor:
            if self.partidaConFlor:
                tanto = 20 + cartas[0].valorEnvido + cartas[1].valorEnvido + cartas[2].valorEnvido 
            else:
                tanto = 20 + cartas[0].valorEnvido + cartas[1].valorEnvido
                
                if tanto < (20 + cartas[0].valorEnvido + cartas[2].valorEnvido):
                    tanto = 20 + cartas[0].valorEnvido + cartas[2].valorEnvido

                if tanto < (20 + cartas[1].valorEnvido + cartas[2].valorEnvido):
                    tanto = 20 + cartas[1].valorEnvido + cartas[2].valorEnvido

            return tanto

        #a partir de aca se calcula los casos: 2 cartas del mismo palo o niguna carta del mismo palo
        for c in cartas:
            if c.palo == 'e':
                cantEspada = cantEspada + 1 
            elif c.palo == 'b':
                cantBasto = cantBasto + 1
            elif c.palo == 'o':
                cantOro = cantOro + 1
            elif c.palo == 'c':
                cantCopa = cantCopa + 1

        #se calcula el envido si tiene 2 cartas del mismo palo:
        if cantEspada==2:
            tanto=20
            for c in cartas:
                if c.palo=='e':
                    tanto = tanto + c.valorEnvido
            return tanto

        elif cantBasto==2:
            tanto=20
            for c in cartas:
                if c.palo=='b':
                    tanto = tanto + c.valorEnvido
            return tanto

        elif cantOro==2:
            tanto=20
            for c in cartas:
                if c.palo=='o':
                    tanto = tanto + c.valorEnvido
            return tanto

        elif cantCopa==2:
            tanto=20
            for c in cartas:
                if c.palo=='c':
                    tanto = tanto + c.valorEnvido
            return tanto
        
        else: #no hay ningun palo con 2 cartas, hay que determinar el mayor valor
            mayor=0
            if cartas[0].valorEnvido>=mayor:
                mayor = cartas[0].valorEnvido
            
            if cartas[1].valorEnvido>=mayor:
                mayor = cartas[1].valorEnvido
            
            if cartas[2].valorEnvido>=mayor:
                mayor=cartas[2].valorEnvido
            
            return mayor

    def respuesta(self) -> bool:
        k=0
        
        #se asigna la fila de la matriz de probabilidad
        '''if self.__partidaConFlor and self.__tieneFlor: 
                return None  #? es para cantar FLOR, analizar!
        '''
        if self.__envido<20:
            f = self.__envido
        else:
            f = self.__envido - 12

        #se asigna la columna de probabilidad
        if self.__estiloJugador == "Cauteloso":
            c=0
        elif self.__estiloJugador == "Normal":
            c=1
        elif self.__estiloJugador == "Agresivo":
            c=2

        k = __class__.matrizProbabilidad[f][c]
        
        if k==0.00:
            return False
        elif k==1.00:
            return True
        else:
            x = random.random()
            if x<k:
                return True
            else:
                return False
