import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
#Antecedent é um array que informa o universo
#'qualidade' é o nome do universo
#o universo está descrito em np.arange(0, 10, 1)
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')

gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')
#Consequent pois retorna a quantidade de gorjeta a serem emitidas

"""
o automf vai mapear cada um dos universos de cada uma das funções nas categorias
passadas em "names", o "number", indica a quantidade de names passados
"""
qualidade.automf(number = 3, names = ['ruim', 'boa', 'saborosa'])
servico.automf(number = 3, names = ['ruim', 'aceitavel', 'otimo'])


#qualidade.view()   #cria um gráfico para verificar melhor a situação

#qualidade['saborosa'].view()           #destaca uma classe

#servico.view()
"""
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 10])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [0, 10, 20])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [10, 20, 20])
#o trimf gera um gráfico triangular
#o arrauy significa [começo, pico, limite]
"""
gorjeta['baixa'] = fuzz.sigmf(gorjeta.universe, 5, -1)          #começa do maior valor e decai
gorjeta['media'] = fuzz.gaussmf(gorjeta.universe, 10, 3)
gorjeta['alta'] = fuzz.pimf(gorjeta.universe, 10, 20, 20, 21)

#regras
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
regra3 = ctrl.Rule(servico['otimo'] | qualidade['saborosa'], gorjeta['alta'])
#o "|" significa or
#a "," significa então

#sistema de controle, para criação de previsão
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)
#para fazer a simulação  do sistema

sistema.input['qualidade'] = 9.5
sistema.input['servico'] = 9.5
sistema.compute()

#saída da gorjeta
print(sistema.output['gorjeta'])

#visualização da porcentagem em gorjeta
gorjeta.view(sim = sistema)