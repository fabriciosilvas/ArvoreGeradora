class ArestaPonderada:
    def __init__(self, verticeInicial: int, verticeFinal: int, peso: int|float, pesofic: int|float = 0) -> None:
        self.peso = peso
        self.pesoFic = pesofic
        self.verticeInicial = verticeInicial
        self.verticeFinal = verticeFinal

    def copia(self):
        a = ArestaPonderada(self.verticeInicial, self.verticeFinal, self.peso, self.pesoFic)
        return a

    def setPesoFic(self, peso):
        self.pesoFic = peso

    def getPesoFic(self):
        return self.pesoFic


    def getVerticeInicial(self) -> int:
        return  self.verticeInicial

    def getVerticeFinal(self) -> int:
        return self.verticeFinal

    def getPeso(self) -> float:
        return self.peso

    def setPeso(self, peso: float) -> None:
        self.peso = peso

    def __str__(self) -> str:
        #return f"({self.verticeInicial}, {self.verticeFinal}, {self.pesoFic})"
        return f"({self.verticeInicial}, {self.verticeFinal}, {self.peso})"

    def __eq__(self, outraAresta: "ArestaPonderada") -> bool:
        return outraAresta.getPeso() == self.getPeso()

    def __gt__(self, outraAresta: "ArestaPonderada") -> bool:
        return self.getPeso() > outraAresta.getPeso()

    def __ge__(self, outraAresta: "ArestaPonderada") -> bool:
        return self.getPeso() >= outraAresta.getPeso()

    def equals(self, other):
        return self.getVerticeInicial() == other.getVerticeInicial() and self.getVerticeFinal() == other.getVerticeFinal()




