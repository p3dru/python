#esse arquivo é para criar um dicionario com duas chaves e uma lista de atributos, dados ex:{('BRU', 'FCO'): ['15:44', '18:55', 382]}

pessoas = [("Lisboa", "LIS"),
            ("Madrid", "MAD"),
            ("Paris", "CDG"),
            ("Dublin", "DUB"),
            ("Londres", "LHR"),
            ("Bruxelas", "BRU")]

destino = 'FCO'

voos = {}

"""
for linha in open("arquivo que seja separado por virgulas e que contenha os dados de voo"):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))

    print(voos)

    #print(voos[('LIS', 'FCO')])
"""
#o exemplo pego (após ter passado por esse for) foi:
voos = {('BRU', 'FCO'): [('6:12', '10:22', 230),
  ('7:53', '11:37', 433),
  ('9:08', '12:12', 364),
  ('10:30', '14:57', 290),
  ('12:19', '15:25', 342),
  ('13:54', '18:02', 294),
  ('15:44', '18:55', 382),
  ('16:52', '20:48', 448),
  ('18:26', '21:29', 464),
  ('20:07', '23:27', 473)],
 ('CDG', 'FCO'): [('6:25', '9:30', 335),
  ('7:34', '9:40', 324),
  ('9:15', '12:29', 225),
  ('11:28', '14:40', 248),
  ('12:05', '15:30', 330),
  ('14:01', '17:24', 338),
  ('15:34', '18:11', 326),
  ('17:07', '20:04', 291),
  ('18:23', '21:35', 134),
  ('19:53', '22:21', 173)],
 ('DUB', 'FCO'): [('6:17', '8:26', 89),
  ('8:04', '10:11', 95),
  ('9:45', '11:50', 172),
  ('11:16', '13:29', 83),
  ('12:34', '15:02', 109),
  ('13:40', '15:37', 138),
  ('15:27', '17:18', 151),
  ('17:11', '18:30', 108),
  ('18:34', '19:36', 136),
  ('20:17', '22:22', 102)],
 ('FCO', 'BRU'): [('6:09', '9:49', 414),
  ('7:57', '11:15', 347),
  ('9:49', '13:51', 229),
  ('10:51', '14:16', 256),
  ('12:20', '16:34', 500),
  ('14:20', '17:32', 332),
  ('15:49', '20:10', 497),
  ('17:14', '20:59', 277),
  ('18:44', '22:42', 351),
  ('19:57', '23:15', 512)],
 ('FCO', 'CDG'): [('6:33', '9:14', 172),
  ('8:23', '11:07', 143),
  ('9:25', '12:46', 295),
  ('11:08', '14:38', 262),
  ('12:37', '15:05', 170),
  ('14:08', '16:09', 232),
  ('15:23', '18:49', 150),
  ('16:50', '19:26', 304),
  ('18:07', '21:30', 355),
  ('20:27', '23:42', 169)],
 ('FCO', 'DUB'): [('6:39', '8:09', 86),
  ('8:23', '10:28', 149),
  ('9:58', '11:18', 130),
  ('10:33', '12:03', 74),
  ('12:08', '14:05', 142),
  ('13:39', '15:30', 74),
  ('15:25', '16:58', 62),
  ('17:03', '18:03', 103),
  ('18:24', '20:49', 124),
  ('19:58', '21:23', 142)],
 ('FCO', 'LHR'): [('6:58', '9:01', 238),
  ('8:19', '11:16', 122),
  ('9:58', '12:56', 249),
  ('10:32', '13:16', 139),
  ('12:01', '13:41', 267),
  ('13:37', '15:33', 142),
  ('15:50', '18:45', 243),
  ('16:33', '18:15', 253),
  ('18:17', '21:04', 259),
  ('19:46', '21:45', 214)],
 ('FCO', 'LIS'): [('6:19', '8:13', 239),
  ('8:04', '10:59', 136),
  ('9:31', '11:43', 210),
  ('11:07', '13:24', 171),
  ('12:31', '14:02', 234),
  ('14:05', '15:47', 226),
  ('15:07', '17:21', 129),
  ('16:35', '18:56', 144),
  ('18:25', '20:34', 205),
  ('20:05', '21:44', 172)],
 ('FCO', 'MAD'): [('6:03', '8:43', 219),
  ('7:50', '10:08', 164),
  ('9:11', '10:42', 172),
  ('10:33', '13:11', 132),
  ('12:08', '14:47', 231),
  ('14:19', '17:09', 190),
  ('15:04', '17:23', 189),
  ('17:06', '20:00', 95),
  ('18:33', '20:22', 143),
  ('19:32', '21:25', 160)],
 ('LHR', 'FCO'): [('6:08', '8:06', 224),
  ('8:27', '10:45', 139),
  ('9:15', '12:14', 247),
  ('10:53', '13:36', 189),
  ('12:08', '14:59', 149),
  ('13:40', '15:38', 137),
  ('15:23', '17:25', 232),
  ('17:08', '19:08', 262),
  ('18:35', '20:28', 204),
  ('20:30', '23:11', 114)],
 ('LIS', 'FCO'): [('6:11', '8:31', 249),
  ('7:39', '10:24', 219),
  ('9:15', '12:03', 99),
  ('11:08', '13:07', 175),
  ('12:18', '14:56', 172),
  ('13:37', '15:08', 250),
  ('15:03', '16:42', 135),
  ('16:51', '19:09', 147),
  ('18:12', '20:17', 242),
  ('20:05', '22:06', 261)],
 ('MAD', 'FCO'): [('6:05', '8:32', 174),
  ('8:25', '10:34', 157),
  ('9:42', '11:32', 169),
  ('11:01', '12:39', 260),
  ('12:44', '14:17', 134),
  ('14:22', '16:32', 126),
  ('15:58', '18:40', 173),
  ('16:43', '19:00', 246),
  ('18:48', '21:45', 246),
  ('19:50', '22:24', 269)]}


agenda = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]

def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0                                         #preço total do custo da viagem

    for i in range(len(agenda) // 2):                       #repete o "conjunto representado pela agenda", uma vez que ela está organizada em pares
        nome = pessoas[i][0]                                #acessa o nome das cidades
        origem = pessoas[i][1]                              #encontra os voos pela sigla de onde ele está saindo, lista pessoas da linha 3
        id_voo += 1                                         #incrementa o id do voo informando que é o de ida
        ida = voos[(origem, destino)][agenda[id_voo]]       #busca os voos com a chave (origem, destino), pelo indice passado pela agenda no indice id_voo que é incrementado
        total_preco += ida[2]                               #aumenta o preço total baseando-se no preço, determinado pelo array de ida
        id_voo += 1                                         #incremente novamente o id do voo informando que é o de volta (nome arbitrário)    
        volta = voos[(destino, origem)][agenda[id_voo]]     #busca os voos com a chave (destino, origem), pelo indice passado pela agenda no indice id_voo que é incrementado
        total_preco += volta[2]                             #incrementa o preço baseado no preço da volta, acessável por ida[2] que seria um array

        #imprime o nome da cidade     sigla do aeroporto, horario de inicio da viagem de ida, horario de termino da viagem de ida, preço da viagem de ida
        #horario do inicio da viagem de volta, horario do termino da viagem de volta, preço da viagem de volta
        print("%10s%10s %5s-%5s %3s %5s-%5s %3s" % (nome, origem, ida[0], ida[1], ida[2], volta[0], volta[1], volta[2]))
    
    #print o preço total da viagem
    print(f"Preço total: {total_preco}")

imprimir_voos(agenda)

#O objetivo dos outros algoritmos é determinar os menores custos das viagens de ida e volta "automaticamente"