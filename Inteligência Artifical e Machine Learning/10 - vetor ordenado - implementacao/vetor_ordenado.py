import numpy as np


class VetorOrdenado:

    def __init__(self, capacidade):                             #(__init__) é utilizado para inicializar objetos
        self.capacidade = capacidade                            #recebe a capacidade total do vetor
        self.ultima_posicao = -1                                #quando estiver vazio, retorna -1
        self.valores = np.empty(self.capacidade, dtype=int)     #cria um array do tipo int com a capacidade passada 
    
    def imprime(self):                                          #imprime o array com a posição
        if self.ultima_posicao == -1:                           #se estiver vazio, imprime apenas que estão vazio
            print("Vetor Vazio")
        else:
            for i in range(self.ultima_posicao + 1):            #se estiver povoado, mostra todos os valores com as respectivas posições
                print(i, " - ", self.valores[i])
    
    def insere(self, valor):                                    #insere em self, o valor passado por valor
        if self.ultima_posicao == self.capacidade - 1:          #verifica se ainda tem espaço no vetor, se não tiver, retorna que está cheio
            print("Capacidade máxima atingida")
            return
        
        posicao = 0                                             #define a posição inicial

        for i in range(self.ultima_posicao + 1):                #para cada posição do vetor              
            posicao = i                                         #posição se atualiza com a posição atual do vetor
            if self.valores[i] > valor:                         #essa linha serve para encontrar a posição a ser inserida, quando encontra, passa pra próxima instrução
                break
            if i == self.ultima_posicao:                        #se ele já percorreu todo o vetor e está na última posição
                posicao = i + 1                                 #ele atualiza o valor de i para i + 1, adicionando o maior valor ao final da lista
        
        x = self.ultima_posicao                                 #começa um contador da última posição

        while x >= posicao:                                     #enquanto a posição indicada por x for maior que a posicao atual [i]
            self.valores[x + 1] = self.valores[x]               #é realizada a troca de valores, sendo que cada valor acima da posição atual, é movido pra frente em 1 elemento (pula um)
            x -= 1                                              #atualiza o valor de x para x - 1
        
        self.valores[posicao] = valor                           #insere o novo valor na posição encontrada por [i]
        self.ultima_posicao += 1                                #atualiza a última posição em +1 pois foi inserido um novo elemento no vetor


vetor = VetorOrdenado(10)
vetor.imprime()

vetor.insere(12)
vetor.insere(14)
vetor.insere(1)
vetor.insere(7)
vetor.insere(6)
vetor.insere(82)
vetor.insere(17)
vetor.insere(92)
vetor.insere(98)
vetor.insere(100)

vetor.imprime()
