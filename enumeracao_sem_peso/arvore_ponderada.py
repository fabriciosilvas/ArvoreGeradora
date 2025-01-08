from aresta_ponderada import ArestaPonderada

class ArvorePonderada:
    def __init__(self, quantidadeVertices: int, arestas: list[ArestaPonderada] = None) -> None:
        self.quantidadeVertices: int = quantidadeVertices
        self.parent: list[int] = list(range(1, quantidadeVertices + 1))
        self.rank: list[int] = [0] * quantidadeVertices
        self.quantidadeArestas = 0
        self.arestas: list[ArestaPonderada] = list()

        if arestas is not None:
            for aresta in arestas:
                self.inserirAresta(aresta)

    def getArestas(self) -> list[ArestaPonderada]:
        return self.arestas

    def size(self) -> int:
        return self.quantidadeArestas

    def __str__(self) -> str:
        string: str = "["

        indice: int = len(self.arestas)

        for aresta in range(indice - 1):
            string += f"{str(self.arestas[aresta])}, "

        if indice:
            string += f"{str(self.arestas[indice - 1])}]"
        else:
            string += "]"


        string += "\n"

        return string


    def inserirAresta(self, aresta: ArestaPonderada) -> bool:
        if self.quantidadeArestas == self.quantidadeVertices - 1:
            return False

        if self.unionSet(aresta):
            self.arestas.append(aresta)
            self.quantidadeArestas += 1

            return True

        return False


    def getQtdVertices(self) -> int:
        return self.quantidadeVertices

    def getQtdArestas(self) -> int:
        return self.quantidadeArestas


    def findSet(self, vertice: int) -> int:
        if vertice == self.parent[vertice - 1]:
            return vertice

        auxiliar: int = self.findSet(self.parent[vertice - 1])
        self.parent[vertice - 1] = auxiliar

        return auxiliar


    def unionSet(self, aresta: ArestaPonderada) -> bool:
        verticeInicial: int = aresta.getVerticeInicial()
        verticeFinal: int = aresta.getVerticeFinal()

        parentVerticeInicial = self.findSet(verticeInicial)
        parentVerticeFinal = self.findSet(verticeFinal)

        if parentVerticeInicial != parentVerticeFinal:
            if self.rank[parentVerticeInicial - 1] < self.rank[parentVerticeFinal - 1]:
                parentVerticeInicial, parentVerticeFinal = parentVerticeFinal, parentVerticeInicial

            self.parent[parentVerticeFinal - 1] = parentVerticeInicial
            if self.rank[parentVerticeInicial - 1] == self.rank[parentVerticeFinal - 1]:
                self.rank[parentVerticeInicial - 1] += 1

            return True

        return False