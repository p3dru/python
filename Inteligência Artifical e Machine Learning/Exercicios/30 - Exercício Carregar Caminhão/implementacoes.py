import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

"""
O problema consiste em carregar um caminhão para se obter o maior lucro possível levando em consideração alguns quesitos:
1 - O espaço disponível do caminhão que é de 3m³
2 - O valor total de vendas (O que deve ser o maior possível)
3 - O espaço que cada objeto ocupa
"""

#para imprimir a solução padrão
def imprimir_solucao(solucao):
    for i in range(len(solucao)):
        if solucao[i] == 1:
            print("{} - {}".format(produtos[i][0], produtos[i][2]))

#função fitness (serve para verificar o quão perto uma solução encontrada está próxima de alcançar os objetivos definidos)
def fitness_function(solucao):
    custo = 0                                               #custo total (lucro)
    soma_espaco = 0                                         #soma do espaço ocupado
    for i in range(len(solucao)):
        if solucao[i] == 1:                                 #o 1 significa que o produto será carregado, 0 não. Uma solução binária
                                                            #gerada pelos algoritmos que testaremos
            custo += produtos[i][2]                         #soma produtos
            soma_espaco += produtos[i][1]                   #soma espaço
    if soma_espaco > espaco_disponivel:                     #se a soma dos produtos ultrapassarem os espaços disponíveis, ele não é carregado
        custo = 1                                           #descarta pois o custo é o pior possível
    return custo                                            #retonrna o custo total


#Produtos a serem levados em consideração:
produtos = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]
espaco_disponivel = 3


#criamos um objeto mlrose:
fitness = mlrose.CustomFitness(fitness_function)
problema = mlrose.DiscreteOpt(length=14, fitness_fn=fitness, maximize=True, max_val=2)
"""
Lenght 14 pois o tamanho da solução a ser impressa é uma lista de 14 elementos com 0 e 1, indicando o carregamento ou não
do produto, sendo o 0 para não carregado e 1 para carregado.
fitness_fn=fitness, pois é essa função que fará a análise
maximize=True, pois queremos os maiores valores possíveis
max_val=2, pois assim ele determina os valores na lista em 0 e 1 (que são as respostas que queremos) 
"""

'''
#hill climb
print("10 soluções Hill Climb")
for x in range(10):
    print("Inicio solução {}".format(x))
    melhor_solucao, melhor_custo = mlrose.hill_climb(problema)
    print(melhor_solucao, melhor_custo)
    imprimir_solucao(melhor_solucao)
    print("Fim solução {}".format(x))
    print("_____________________________________________")
'''

'''
#Simulated Annealing
print("10 tentativas Simulated Annealing")
for x in range(10):
    print("Inicio solução {}".format(x))
    melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema)
    print(melhor_solucao, melhor_custo)
    imprimir_solucao(melhor_solucao)
    print("Fim solução {}".format(x))
    print("_____________________________________________")
'''

#Genetic_algorithm
print("10 tentativa Algoritmo Genético")
for x in range(10):
    print("Inicio solução {}".format(x))
    melhor_solucao, melhor_custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2)
    print(melhor_solucao, melhor_custo)
    imprimir_solucao(melhor_solucao)
    print("Fim solução {}".format(x))
    print("_____________________________________________")



#PARA DEFINIR QUAL É A MELHOR SOLUÇÃO, É NECESSÁRIO SEMPRE FAZER OS TESTES COM OS TRÊS MÉTODOS