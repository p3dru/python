#levando em consideração o eixo x como idade (máximo de 50) e o eixo y como renda (máximo de 24.0) no ponto (x,y)


import random


def distancia_cluster(cluster:list, dado:list):
    distancia = ((dado[0] - cluster[0]) ** 2 + (dado[1] - cluster[1]) ** 2) ** 1/2
    return distancia


def calcular_ponto_medio(lista:list):
    soma_dos_x = 0
    soma_dos_y = 0
    for elementos in range(len(lista)):
        soma_dos_x += float(lista[elementos[0][0]])
        soma_dos_y += float(lista[elementos[0][1]])
    
    
    media_dos_x = soma_dos_x / len(lista)
    media_dos_y = soma_dos_y / len(lista)

    cluster = (media_dos_x, media_dos_y)
    return cluster

#indica qual é o conjunto dos dados
dados = [[9.6, 28], [8.4, 31], [2.4, 42], [18.2, 38], [3.9, 25], [6.4, 41]]

#cluster 1 aleatório
renda = random.randint(0, 240) / 10
idade = random.randint(0, 50)
cluster_1 = (renda, idade)

#cluster 2 aleatório
renda = random.randint(0, 240) / 10
idade = random.randint(0, 50)
cluster_2 = (renda, idade)

#listas para pontos mais próximos de cada cluster
lista_cluster_1 = []
lista_cluster_2 = []

#fazer 5 iterações
for x in range(5):
    #calcular quais os pontos mais próximos
    for elementos in range(len(dados)):
        #calcular as distâncias
        distancia_1 = distancia_cluster(cluster_1, dados[elementos])
        print(distancia_1, " 1")
        distancia_2 = distancia_cluster(cluster_2, dados[elementos])
        print(distancia_2, " 2")

        #comparar qual distância é a menor e atribuir à um cluster
        if distancia_1 < distancia_2:
            lista_cluster_1.append(dados[elementos])
        else:
            lista_cluster_2.append(dados[elementos])
    
    if len(lista_cluster_1) > 0:
        cluster_1 = calcular_ponto_medio(lista_cluster_1)

    if len(lista_cluster_2) > 0:
        cluster_2 = calcular_ponto_medio(lista_cluster_2)


#calcular a médio entre os pontos de cada cluster
if len(lista_cluster_1) == 0:
    print("Não foi possível encontrar o ponto médio")
elif len(lista_cluster_1) == 1:
    print(f"Ponto médio: {lista_cluster_1[0]}")
else:
    ponto_medio = calcular_ponto_medio(lista_cluster_1)
    print(f"O centróide 1 está localizado no ponto {ponto_medio}")

if len(lista_cluster_2) == 0:
    print("Não foi possível encontrar o ponto médio")
elif len(lista_cluster_2) == 1:
    print(f"Ponto médio: {lista_cluster_2[0]}")
else:
    ponto_medio = calcular_ponto_medio(lista_cluster_2)
    print(f"O centróide 2 está localizado no ponto {ponto_medio}")


    
print(lista_cluster_1)
print(lista_cluster_2)

    



'''
'''