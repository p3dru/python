"""
Uma clínica recebe vários chamados por dia, os chamados são apenas de
duas naturezas ou são marcações de consultas ou são cancelamento de consultas,
sendo o custo da primeira sendo 75 reais e a segunda 20. 
A taxa de cancelamento de consultas é em torno de 22%.
O script abaixo retorna a quantidade de pessoas que remarcaram as consultas no dia,
a quantidade de pessoas que compareceram às consultas no dia, a lucro diário da clínica
e o lucro médio no período.
"""
import random
import numpy as np
from numpy.core.fromnumeric import size


def lucro_diario(cancelados, efetuados):
    y = (cancelados + efetuados) * 75 + cancelados * 20
    return y


#variáveis para o lucro mínimo e máximo da empresa
lucro_minimo = 0
lucro_maximo = 0
lucro_total = 0

#define o período de simulações (dias)
dias = int(input("Digite a quantidade de dias para teste: "))

for x in range(dias):
    #recebe a quantidade de chamados em um dia
    chamados = int(input("Digite a quantidade de chamados no dia: "))

    #variáveis para quem compareceu e não
    remarcaram = realizados = 0

    #para cada chamado, avalia a possibilidade da pessoa cancelar ou não
    for y in range(chamados):
        probabilidade_de_comparecimento = random.randint(1, 100)
        probabilidade_de_comparecimento = probabilidade_de_comparecimento / 10
        if probabilidade_de_comparecimento > 2.2:
            realizados += 1
        else:
            remarcaram += 1
        
    lucro = lucro_diario(remarcaram, realizados)
    lucro_total += lucro

    print("=-" * 30)
    print(f"Pessoas que compareceram para as consultas: {realizados}")
    print(f"Pessoas que remarcaram as consultas: {remarcaram}")
    print(f"Lucro diário: {lucro}")
    print("=-" * 30)
    print()
    
    #descobrir lucro máximo e mínimo
    if x == 0:
        lucro_maximo = lucro
        lucro_minimo = lucro
    else:
        if lucro < lucro_minimo:
            lucro_minimo = lucro
        else:
            lucro_minimo = lucro_minimo
        
        if lucro > lucro_maximo:
            lucro_maximo = lucro
        else:
            lucro_maximo = lucro_maximo


#definir pontos aleatórios entre dias testados
    #lucro_minimo é o valor inferior
    #lucro_maximo é o valor superior
    #as iterações são os números de dias
valores_aleatorios = lucro_minimo+(lucro_maximo - lucro_minimo) * np.random.uniform(size=dias)

#encontrar valor máximo da função no intervalo: max_y=max([f(x[i]) for i in range(N)])
#porém, já possuo o valor máximo no período que é o valor_máximo

#pontos aleatórios entre 0 e max_y = lucro_máximo
pontos_aleatorios = lucro_maximo * np.random.uniform(size=dias)


#contagem entre a função descrita e o y=0 (função zerada)
contador = 0

for i in range(dias):
    if valores_aleatorios[i] < lucro_maximo:
        contador += 1

#area de integração em relacao a area do retangulo na proporcao contador/dias
relacao = lucro_maximo*(lucro_maximo - lucro_minimo) * (contador/dias)
print(relacao)

print(f"A média de lucro é de {lucro_total / dias}")



