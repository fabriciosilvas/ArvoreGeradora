# Enumeração de árvores geradoras 
A enumeração de árvores geradoras é um tópico de grande relevância na Teoria dos Grafos, especialmente em problemas que envolvem análise estrutural e otimização de grafos conectados. <br>  <br>
Árvores geradoras são subgrafos acíclicos que conectam todos os vértices de um grafo, e sua enumeração consiste em identificar e listar todas as possíveis árvores geradoras de um grafo dado. <br><br>O algoritmo aqui desenvolvido se baseia nas técnicas apresentadas por Sörensen e Janssens (2005) e no algoritmo de cálculo de árvore geradora mínima de Kruskal.

## Instalação de bibliotecas
Para que o código funcione corretamente, é necessário instalar as seguintes bibliotecas: <br>
```$ pip install networkx``` <br>
```$ pip install matplotlib``` <br>
```$ pip install keyboard```

## Execução
Para executar o algoritmo, é preciso seguir os seguintes passos: <br>


### Grafos não direcionados sem peso
1. Instale as bibliotecas
2. No arquivo ```grafo.txt``` adicione
    - o número de vértices na primeira linha
    - as arestas em seguida, uma por linha, no formato ```verticeInicial verticeFinal```, separados por espaço
    - os vértices devem ser identificados como inteiros na sequência [1, n], onde n representa o número de vertices 
3. Execute o arquivo ```main.py``` em [enumeracao_sem_peso](/enumeracao_sem_peso)
4. A primeira árvore será gerada e exibida na tela. Para fechar a imagem, tecle ```q```
5. Para encerrar o programa, tecle ```s```
6. Para gerar a próxima árvore, tecle ```p```

### Grafos não direcionados com peso
1. Instale as bibliotecas
2. No arquivo ```grafo.txt``` adicione
    - o número de vértices na primeira linha
    - as arestas em seguida, uma por linha, no formato ```verticeInicial verticeFinal peso```, separados por espaço
    - os vértices devem ser identificados como inteiros na sequência [1, n], onde n representa o número de vertices 
    - o peso pode ser um número decimal ou inteiro
3. Execute o arquivo ```main.py``` em [enumeracao_com_peso](/enumeracao_com_peso)
4. A primeira árvore será gerada e exibida na tela. Para fechar a imagem, tecle ```q```
5. Para encerrar o programa, tecle ```s```
6. Para gerar a próxima árvore, tecle ```p```

Além das imagens, um arquivo ```arvores.txt``` será fornecido, contendo as arestas de cada uma das árvores geradas.