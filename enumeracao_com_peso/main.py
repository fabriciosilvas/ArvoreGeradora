from math import inf
import matplotlib.pyplot as plt
import networkx as nx
from particao import Particao
from aresta_ponderada import ArestaPonderada
from arvore_ponderada import ArvorePonderada
from heap_minima_particao import HeapMinimaParticao
import keyboard

def particionamento(particao: Particao, particoes: HeapMinimaParticao):
    particao1: Particao = particao.copia()
    particao2: Particao = particao.copia()
    arestas = particao.getArestasAGM()

    for a in range(len(arestas)):
        if arestas[a].getPesoFic() == 0:
            particao1.atualiza(arestas[a], inf)
            particao2.atualiza(arestas[a], -inf)

            if particao1.calcularArvoreGeradoraMinima():
                particoes.inserirElemento(particao1)

        particao1 = particao2.copia()
        
def plotarGrafo(grafo, arestas, contador, pos, custo):
    for aresta in arestas:
        grafo.add_edge((aresta.getVerticeInicial()), (aresta.getVerticeFinal()), weight=aresta.getPeso())

    nx.draw_networkx_nodes(grafo, pos, node_size=700)
    elarge = [(u, v) for (u, v, d) in grafo.edges(data=True)]
    nx.draw_networkx_edges(grafo, pos, edgelist=elarge, width=6)
    
    
    nx.draw_networkx_labels(grafo, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(grafo, "weight")

    nx.draw_networkx_edge_labels(grafo, pos, edge_labels, label_pos=0.3)
    
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.title(f"ÁRVORE {contador} - CUSTO = {custo}")
    plt.show(block=True)
    grafo.clear_edges()
        

def main():

    with open("enumeracao_com_peso/grafo.txt", "r") as grafo:
        qtdVertices = int(grafo.readline())
        particoes: HeapMinimaParticao = HeapMinimaParticao(qtdVertices)
        particao = Particao(qtdVertices)

        for linha in grafo:
            valores = tuple(map(int, linha.strip('\n').split(' ')))
            aresta = ArestaPonderada(*valores)
            particao.inserirArestaObrigatoria(aresta)

    with open("enumeracao_com_peso/arvores.txt", "w") as arvores:
        particoes.inserirElemento(particao)
        if not particao.calcularArvoreGeradoraMinima():
            print("Não é possível gerar uma árvore para esse grafo")
            return

        menorArvore: ArvorePonderada = particao.getArvoreGeradoraMinima()

        G = nx.Graph()
        G.add_nodes_from(list(range(1, qtdVertices + 1)))
        pos = nx.circular_layout(G)
        contador = 1
        print("Tecle p para gerar a próxima árvore ou s para encerrar")
        sent = True
        while menorArvore is not None and particoes.tamanhoHeap and sent:
            particao: Particao = particoes.removerElementoMinimo()
            menorArvore: ArvorePonderada = particao.getArvoreGeradoraMinima()
            elem = menorArvore.getArestas()
            
            plotarGrafo(G, elem, contador, pos, menorArvore.getCusto())
           

            arvores.write(str(menorArvore))

            
            particionamento(particao, particoes)

            contador += 1
            while True:
                if keyboard.is_pressed('s'):
                    sent = False
                    break
                if keyboard.is_pressed('p'):
                    break




        

    
            
main()