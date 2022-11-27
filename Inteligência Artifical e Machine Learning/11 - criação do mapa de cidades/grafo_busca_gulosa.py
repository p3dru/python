import numpy as np


class Vertice:
    def __init__(self, rotulo, distancia_objetivo):            #self é o padrão, rotulo é o nome da cidade, distancia objetivo é a distancia ao 
                                                            #próximo vertice
        self.rotulo = rotulo                                   
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
    
    def adiciona_adjacente(self, adjacente):                   #adiciona uma cidade adjacente à lista de cidades adjancetes (self.adjacentes)
        self.adjacentes.append(adjacente)
    
    def mostra_adjacentes(self):                               #exibe os adjacentes de determinada cidade
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)                   #sendo i o indice, vertice é a cidade selecionada,
                                                                #rotulo é o nome das cidades proximas e
                                                                # i.custo é o custo de ir até aquela cidade
        

class Adjacente:                                               #é a classe que define o que é o adjacente, informando o vertice que é a cidade
                                                                #proxima e o custo que é a distancia de se ir até lá
    def __init__(self, vertice, custo):
        self.vertice = vertice                                 
        self.custo = custo
    

class Grafo:                                                   #cria o grafo por completo
    #cria os vertices das cidades, passando o nome da cidade e a distânica até o objetivo (Bucharest) em linha reta
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    #aqui, adiciona todos os ajacentes de cada cidade, passando a
    #cidade_de_referencia.adiciona_adjacente(Adjacente(proxima_cidade, distancia da cidade_de_referencia à proxima_cidade))
    #Nas linhas 48 e 52 (e em algumas outras) estão "repetidos", pois é necessário repetir, uma vez que a via é de mão dupla
    #(você pode ir de arad a zerind e de zerind à arad) e a distância é a mesma, só não poderiamos repetir, caso a viagem
    #permitisse apenasum sentido  
    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))


grafo = Grafo()                                                         #cria um novo grafo

#grafo.bucharest.mostra_adjacentes()                                     #mostra as cidades adjacentes da cidade escolhida



class VetorOrdenado:                                                    #ordena a lista de cidades
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)              #cria um array de objetos

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, vertice):
    if self.ultima_posicao == self.capacidade - 1:                      #verifica se a posição atual é a última
      print('Capacidade máxima atingida')
      return
    posicao = 0                                                         #recebe a posição como a primeira (inicio)
    for i in range(self.ultima_posicao + 1):                            #varre o array para procurar a posição ideal a inserir o vertice
      posicao = i                                                       #recebe a posição i
      if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:   #se a distância do vertice presente no array for maior do que a do
                                                                            #vertice a ser adicionado
        break                                                           #para a busca por posições de onde inserir        
      if i == self.ultima_posicao:                                      #se a posição encontrada foi a ultima 
        posicao = i + 1                                                 #adiciona o valor à próxima
    x = self.ultima_posicao                                             #recebe a ultima posição do array
    while x >= posicao:                                                 #faz uma busca reversa
      self.valores[x + 1] = self.valores[x]                             #para deslocar os valores que estão acima da posição encontrada para inserir o novo vertice
      x -= 1                                                            #decrementa para atualizar
    self.valores[posicao] = vertice                                     #aqui, ele atualiza a posição dos valores para uma casa à frente
    self.ultima_posicao += 1                                            #e atualiza o total de posições

  def imprime(self):
    if self.ultima_posicao == -1:                                       #se estiver vazio...
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):                          #se estiver povoado, printa a posição, o nome da cidade na posição i do array
                                                                        #e o valor da distância do objetivo
        print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)  

class Gulosa:
  def __init__(self, objetivo):                                         #define como objetivo, o que queremos alcançar (a cidade de bucharest)
    self.objetivo = objetivo
    self.encontrado = False                                             #para saber se foi encontrado

  def buscar(self, atual):                                              #atual é o elemento a ser processado no momento
    print('-------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True                                               #altera para true pois ele já foi visitado

    if atual == self.objetivo:                                          
      self.encontrado = True                                            #se encontrado os objetivos para as demandas necessárias
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))             #gera um vetor com as cidades adjacentes (economiza memória)
      for adjacente in atual.adjacentes:                                #para as cidades adjacentes nas adjacentes encontradas
        if adjacente.vertice.visitado == False:                         #se o vertice adjacente não foi visitado
          adjacente.vertice.visitado == True                            #altera para true
          vetor_ordenado.insere(adjacente.vertice)                      #adiciona o vertice ao vetor ordenado
      vetor_ordenado.imprime()                                          #imprime o vetor ordenado

      if vetor_ordenado.valores[0] != None:                             #se o vetor ordenado na posição 0 for diferente de None (vazio)
        self.buscar(vetor_ordenado.valores[0])                          #chama a função recursiva para buscar a próxima cidade trocando os elementos
                                                                        #na próxima chamada
    """
    Como ele faz essa troca: Como o vetor é ordenado, o menor valor, vai para a primeira posição (posição 0)
    logo, como essa é a menor distância para se percorrer, ela é a escolhida como ideal. Essa "escolha" acontece
    na linha 160 e 161. O código para quando a condição da linha 150 é atendida.
    """

busca_gulosa = Gulosa(grafo.bucharest)                                  #deve ser bucharest pois o os valores passados da linha 31 à 44, são a distância em
                                                                        #em linha reta até bucharest
busca_gulosa.buscar(grafo.arad)                                         #aqui basta alterar a cidade para uma das inseridas