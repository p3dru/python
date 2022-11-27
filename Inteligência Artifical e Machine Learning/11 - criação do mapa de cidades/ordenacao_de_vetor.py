import numpy as np
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