from typing import Optional
from aresta_ponderada import ArestaPonderada
from arvore_ponderada import ArvorePonderada


class Particao:
    def __init__(self, quantidadeVertices: int) -> None:
        self.arvoreGeradora: Optional[ArvorePonderada] = None
        self.arestas: list[ArestaPonderada] = list()
        self.quantidadeVertices: int = quantidadeVertices

    def __str__(self) -> str:
        string: str = f"["

        k: int = len(self.arestas)
        for elem in range(k-1):
            string += f"{str(self.arestas[elem])}, "

        if k:
            string += f"{str(self.arestas[k - 1])}]"
        else:
            string += "]"

        return string

    def getArestas(self) -> list[ArestaPonderada]:
        return self.arestas

    def atualizaTipoAresta(self, aresta:  ArestaPonderada, novoTipo: int):
        for i in range(len(self.arestas)):
            if self.arestas[i].equals(aresta):
                self.arestas[i].setTipo(novoTipo)


    def copia(self) -> "Particao":
        novaParticao: Particao = Particao(self.quantidadeVertices)
        l = list()

        for ares in self.arestas:
            a = ares.copia()
            l.append(a)

        novaParticao.setArestas(l)

        return novaParticao



    def setArestas(self, arestas: list[ArestaPonderada]) -> None:
        self.arestas = arestas

    def inserirAresta(self, aresta: ArestaPonderada) -> None:
        self.arestas.append(aresta)

    def getArvoreGeradora(self) -> Optional[ArvorePonderada]:
        return self.arvoreGeradora

    def getArestasAG(self) -> list[ArestaPonderada]:
        return self.arvoreGeradora.getArestas()

    def calcularArvoreGeradora(self) -> bool:
        self.arvoreGeradora = ArvorePonderada(self.quantidadeVertices)
        temp = sorted(self.arestas, key=lambda a: a.getTipo())

        i = 0

        while i < len(temp) and temp[i].getTipo() == -1:
            self.arvoreGeradora.inserirAresta(temp[i])
            i += 1

        while self.arvoreGeradora.size() < self.quantidadeVertices - 1 and temp[i].getTipo() != 1 :
            self.arvoreGeradora.inserirAresta(temp[i])
            i += 1

        if self.arvoreGeradora.size() == self.quantidadeVertices - 1:
            return True

        return False



