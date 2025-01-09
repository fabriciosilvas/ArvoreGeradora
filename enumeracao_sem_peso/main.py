import matplotlib.pyplot as plt
import networkx as nx
from particao import Particao
from aresta_ponderada import ArestaPonderada
from arvore_ponderada import ArvorePonderada
import keyboard

def particionamento(particao: Particao, particoes: list):
    particao1: Particao = particao.copia()
    particao2: Particao = particao.copia()
    arestas = particao.getArestasAG()

    for a in range(len(arestas)):
        if arestas[a].getTipo() == 0:
            particao1.atualizaTipoAresta(arestas[a], 1)
            particao2.atualizaTipoAresta(arestas[a], -1)


            if particao1.calcularArvoreGeradora():
                particoes.append(particao1)

        particao1 = particao2.copia()

def plotarGrafo(grafo, arestas, contador, pos):
    for aresta in arestas:
        grafo.add_edge((aresta.getVerticeInicial()), (aresta.getVerticeFinal()))

    nx.draw_networkx_nodes(grafo, pos, node_size=700)
    nx.draw_networkx_edges(grafo, pos, width=6)

    nx.draw_networkx_labels(grafo, pos, font_size=20, font_family="sans-serif")

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.title(f"ÁRVORE {contador}")
    plt.show(block=True)
    grafo.clear_edges()

def main():

    with open("enumeracao_sem_peso/grafo.txt", "r") as grafo:
        qtdVertices = int(grafo.readline())
        particoes = []
        particao = Particao(qtdVertices)

        for linha in grafo:
            valores = tuple(map(int, linha.strip('\n').split(' ')))
            aresta = ArestaPonderada(*valores)
            particao.inserirAresta(aresta)

    with open("enumeracao_sem_peso/arvores.txt", "w") as arvores:
        particoes.append(particao)
        if not particao.calcularArvoreGeradora():
            print("Não é possível gerar uma árvore para esse grafo")
            return

        menorArvore: ArvorePonderada = particao.getArvoreGeradora()

        G = nx.Graph()
        G.add_nodes_from(list(range(1, qtdVertices + 1)))
        pos = nx.circular_layout(G)
        contador = 1
        sentinela = True
        print("Tecle p para gerar a próxima árvore ou s para encerrar")
        while menorArvore is not None and len(particoes) and sentinela:

            particao: Particao = particoes.pop()

            menorArvore: ArvorePonderada = particao.getArvoreGeradora()
            elem = menorArvore.getArestas()

            plotarGrafo(G, elem, contador, pos)
            arvores.write(str(menorArvore))
            particionamento(particao, particoes)

            contador += 1
            
            
            while True:
                if keyboard.is_pressed('s'):
                    sentinela = False
                    break
                if keyboard.is_pressed('p'):
                    break
            
            
            
main()

