from typing import Optional
from math import inf
from aresta_ponderada import ArestaPonderada
from arvore_ponderada import ArvorePonderada
from heap_minima_aresta import HeapMinimaAresta


class Particao:
    def __init__(self, quantidadeVertices: int, custo: float = 0) -> None:
        self.arvoreGeradoraMinima: Optional[ArvorePonderada] = None
        self.arestasObrigatorias: list[ArestaPonderada] = list()
        self.quantidadeVertices = quantidadeVertices
        self.custo = custo

    def __str__(self) -> str:
        string = f"{self.custo}: ["

        k: int = len(self.arestasObrigatorias)
        for elem in range(k-1):
            string += f"{str(self.arestasObrigatorias[elem])}, "

        if k:
            string += f"{str(self.arestasObrigatorias[k-1])}]"
        else:
            string += "]"

        return string

    def getArestasObrigatoria(self) -> list[ArestaPonderada]:
        return self.arestasObrigatorias

    def atualiza(self, indice, pesoFic):
        for i in range(len(self.arestasObrigatorias)):
            if self.arestasObrigatorias[i].equals(indice):
                self.arestasObrigatorias[i].setPesoFic(pesoFic)


    def copia(self) -> "Particao":
        novaParticao: Particao = Particao(self.quantidadeVertices)
        l = list()

        for ares in self.arestasObrigatorias:
            a = ares.copia()
            l.append(a)

        novaParticao.setArestasObrigatorias(l)

        return novaParticao



    def setArestasObrigatorias(self, arestas: list[ArestaPonderada]) -> None:
        self.arestasObrigatorias = arestas

    def inserirArestaObrigatoria(self, aresta: ArestaPonderada) -> None:
        self.arestasObrigatorias.append(aresta)

    '''def removerArestaAbertaMinima(self) -> ArestaPonderada:
        return self.arestasAbertas.removerElementoMinimo()'''

    def __gt__(self, outraParticao: "Particao") -> bool:
        return self.custo > outraParticao.custo

    def __eq__(self, outraParticao: "Particao") -> bool:
        return self.custo == outraParticao.custo

    def __ge__(self, outraParticao: "Particao") -> bool:
        return self.custo >= outraParticao.custo

    def getArvoreGeradoraMinima(self) -> Optional[ArvorePonderada]:
        return self.arvoreGeradoraMinima

    def getArestasAGM(self) -> list[ArestaPonderada]:
        return self.arvoreGeradoraMinima.getArestas()

    def calcularArvoreGeradoraMinima(self) -> bool:
        self.arvoreGeradoraMinima = ArvorePonderada(self.quantidadeVertices)
        temp = sorted(self.arestasObrigatorias, key=lambda a: (a.getPesoFic(), a.getPeso()))

        i = 0

        while i < len(temp) and temp[i].getPesoFic() == -inf:
            self.arvoreGeradoraMinima.inserirAresta(temp[i])
            i += 1

        while self.arvoreGeradoraMinima.size() < self.quantidadeVertices - 1 and temp[i].getPesoFic() != inf :
            self.arvoreGeradoraMinima.inserirAresta(temp[i])
            i += 1

        if self.arvoreGeradoraMinima.size() == self.quantidadeVertices - 1:
            self.custo = self.arvoreGeradoraMinima.getCusto()
            return True


        return False



