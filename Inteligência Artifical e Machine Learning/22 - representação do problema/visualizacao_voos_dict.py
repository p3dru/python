#esse arquivo é para criar um dicionario com duas chaves e uma lista de atributos, dados ex:{('BRU', 'FCO'): ['15:44', '18:55', 382]}

pessoas = [("Lisboa", "LIS"),
            ("Madrid", "MAD"),
            ("Paris", "CDG"),
            ("Dublin", "DUB"),
            ("Londres", "LHR"),
            ("Bruxelas", "BRU")]

destino = 'FCO'

voos = {}

for linha in open("arquivo que seja separado por virgulas e que contenha os dados de voo"):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))

    print(voos)

    #print(voos[('LIS', 'FCO')])