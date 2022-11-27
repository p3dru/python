import numpy as np

class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
    
    def adiciona_adjacentes(self, adjacente):
        self.adjacentes.append(adjacente)
    
    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)
    

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = self.custo + vertice.distancia_objetivo


class Grafo:
    #padrão: nome_cidade = Vertice("nome_cidade", distancia_em linha_reta_até_o_objetivo)
    porto_uniao = Vertice("Porto Uniao", 203)
    paulo_frontin = Vertice("Paulo Frontin", 172)
    canoinhas = Vertice("Canoinhas", 141)
    tres_barras = Vertice("Três Barras", 131)
    sao_mateus = Vertice("São Mateus do Sul", 123)
    irati = Vertice("Irati", 139)
    curitiba = Vertice("Curitiba", 0)                  #pois curitiba é o objetivo
    palmeira = Vertice("Palmeira", 59)
    mafra = Vertice("Mafra", 94)
    campo_largo = Vertice("Campo Largo", 27)
    balsa_nova = Vertice("Balsa Nova", 41)
    lapa = Vertice("Lapa", 74)
    tijucas_do_sul = Vertice("Tijucas do Sul", 56)
    araucaria = Vertice("Araucária", 23)
    sao_jose = Vertice("São José dos Pinhais", 13)
    contenda = Vertice("Contenda", 39)

    #adicionar ligações entre cidades/adjacentes
    #padrão = nome_cidade.adiciona_adjacentes(Adjacente(nome_cidade_adjacente, distancia))
    porto_uniao.adiciona_adjacentes(Adjacente(canoinhas, 78))
    porto_uniao.adiciona_adjacentes(Adjacente(sao_mateus, 87))
    porto_uniao.adiciona_adjacentes(Adjacente(paulo_frontin, 46))

    canoinhas.adiciona_adjacentes(Adjacente(tres_barras, 12))
    canoinhas.adiciona_adjacentes(Adjacente(mafra, 66))
    canoinhas.adiciona_adjacentes(Adjacente(porto_uniao, 78))

    paulo_frontin.adiciona_adjacentes(Adjacente(porto_uniao, 46))
    paulo_frontin.adiciona_adjacentes(Adjacente(irati, 75))

    sao_mateus.adiciona_adjacentes(Adjacente(porto_uniao, 87))
    sao_mateus.adiciona_adjacentes(Adjacente(tres_barras, 43))
    sao_mateus.adiciona_adjacentes(Adjacente(irati, 57))
    sao_mateus.adiciona_adjacentes(Adjacente(palmeira, 77))
    sao_mateus.adiciona_adjacentes(Adjacente(lapa, 60))

    tres_barras.adiciona_adjacentes(Adjacente(canoinhas, 12))
    tres_barras.adiciona_adjacentes(Adjacente(sao_mateus, 43))

    irati.adiciona_adjacentes(Adjacente(paulo_frontin, 75))
    irati.adiciona_adjacentes(Adjacente(sao_mateus, 57))
    irati.adiciona_adjacentes(Adjacente(palmeira, 75))

    palmeira.adiciona_adjacentes(Adjacente(irati, 75))
    palmeira.adiciona_adjacentes(Adjacente(sao_mateus, 77))
    palmeira.adiciona_adjacentes(Adjacente(campo_largo, 55))

    lapa.adiciona_adjacentes(Adjacente(sao_mateus, 60))
    lapa.adiciona_adjacentes(Adjacente(mafra, 57))
    lapa.adiciona_adjacentes(Adjacente(contenda, 26))

    mafra.adiciona_adjacentes(Adjacente(canoinhas, 66))
    mafra.adiciona_adjacentes(Adjacente(lapa, 57))
    mafra.adiciona_adjacentes(Adjacente(tijucas_do_sul, 99))

    contenda.adiciona_adjacentes(Adjacente(lapa, 26))
    contenda.adiciona_adjacentes(Adjacente(araucaria, 18))
    contenda.adiciona_adjacentes(Adjacente(balsa_nova, 19))

    tijucas_do_sul.adiciona_adjacentes(Adjacente(mafra, 99))
    tijucas_do_sul.adiciona_adjacentes(Adjacente(sao_jose, 49))

    araucaria.adiciona_adjacentes(Adjacente(contenda, 18))
    araucaria.adiciona_adjacentes(Adjacente(curitiba, 37))

    balsa_nova.adiciona_adjacentes(Adjacente(contenda, 19))
    balsa_nova.adiciona_adjacentes(Adjacente(campo_largo, 22))
    balsa_nova.adiciona_adjacentes(Adjacente(curitiba, 51))

    campo_largo.adiciona_adjacentes(Adjacente(palmeira, 55))
    campo_largo.adiciona_adjacentes(Adjacente(balsa_nova, 22))
    campo_largo.adiciona_adjacentes(Adjacente(curitiba, 29))

    sao_jose.adiciona_adjacentes(Adjacente(tijucas_do_sul, 49))
    sao_jose.adiciona_adjacentes(Adjacente(curitiba, 15))

    curitiba.adiciona_adjacentes(Adjacente(sao_jose, 15))
    curitiba.adiciona_adjacentes(Adjacente(araucaria, 37))
    curitiba.adiciona_adjacentes(Adjacente(balsa_nova, 51))
    curitiba.adiciona_adjacentes(Adjacente(campo_largo, 29))


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)
    
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor Cheio")
            return
        posicao = 0

        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1
    
    
    def imprime(self):
        if self.ultima_posicao == -1:
            print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, "-", self.valores[i].vertice.rotulo, '-',
                self.valores[i].custo, '-',
                self.valores[i].vertice.distancia_objetivo, '-',
                self.valores[i].distancia_aestrela)


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
    
    def buscar(self, atual):
        print("------------")
        print("Atual: {}".format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado == True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)
        
grafo = Grafo()

busca_aestrela = AEstrela(grafo.curitiba)
busca_aestrela.buscar(grafo.porto_uniao)