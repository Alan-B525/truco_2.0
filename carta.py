class Carta:
    idCarta = 0

    def __init__(self, numero, palo) -> None:
        __class__.idCarta = __class__.idCarta + 1
        self.__id = __class__.idCarta
        self.__numero = numero
        self.__palo = palo                                  #de tipo string
        self.__valorEnvido = self.calValorEnvido(numero)

    def __str__(self) -> None:
        return f'Id: {self.__id}.\t|\tNumero: {self.__numero}.\t|\tPalo: {self.__palo}.\t\
            |\tValor envido: {self.__valorEnvido}.\n'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.numero = numero

    @property
    def palo(self):
        return self.__palo

    @palo.setter
    def palo(self, palo):
        self.__palo = palo

    @property
    def valorEnvido(self):
        return self.__valorEnvido

    @valorEnvido.setter
    def id(self, valorEnvido):
        self.__valorEnvido = valorEnvido

    def calValorEnvido(self, numero):
        if numero == 10 or numero == 11 or numero == 12:
            return 0
        else:
            return numero

'''
#para testear
carta2e = Carta(2, "e")
carta10b= Carta(10, "b")

print(f"Numero de la carta 1 --> {carta2e.numero}\n")
print(f"Valor en envido de la carta 1 --> {carta2e.valorEnvido}\n")
print(f"Palo de la carta 1 --> {carta2e.palo}\n")

print(f"Numero de la carta 2 --> {carta10b.numero}\n")
print(f"Valor en envido de la carta 2 --> {carta10b.valorEnvido}\n")
print(f"Palo de la carta 2 --> {carta10b.palo}\n")
'''