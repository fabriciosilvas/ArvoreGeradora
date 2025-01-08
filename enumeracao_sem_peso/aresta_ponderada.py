class ArestaPonderada:
    def __init__(self, verticeInicial: int, verticeFinal: int, tipo: int = 0) -> None:
        self.verticeInicial = verticeInicial
        self.verticeFinal = verticeFinal
        self.tipo = tipo

    def copia(self) -> 'ArestaPonderada':
        copiaAresta = ArestaPonderada(self.verticeInicial, self.verticeFinal, self.tipo)
        return copiaAresta

    def getTipo(self) -> int:
        return self.tipo

    def setTipo(self, tipo: int) -> None:
        self.tipo = tipo


    def getVerticeInicial(self) -> int:
        return self.verticeInicial

    def getVerticeFinal(self) -> int:
        return self.verticeFinal

    def equals(self, outraAresta: 'ArestaPonderada') -> bool:
        return self.verticeInicial == outraAresta.getVerticeInicial() and \
            self.verticeFinal == outraAresta.getVerticeFinal()

    def __str__(self) -> str:
        return f"({self.verticeInicial}, {self.verticeFinal})"


