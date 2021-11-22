# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem savendo que o vencedor tirou o maior número no dado.

from random import randint
# from operator import itemgetter

jogadas = {}
ordem = list()
cont = 1

while cont < 5:
    jogadas[f'Jogador {cont}'] = randint(1, 6)
    ordem.append(jogadas.copy()[f'Jogador {cont}'])
    cont += 1
for k, v in jogadas.items():
    print(f'{k} com {v}')
ordem.sort(reverse=True)
print(f'{"O RANKING É":.^50}')
n = 1
repetido = ''
for indice_Lista in ordem:
    for k, v in jogadas.items():
        if indice_Lista == v and repetido != k:
            print(f'{n}º Lugar: {k} com o número {v}')
            repetido = k
            n += 1
            break

# Esse exericio eu tive inspiração de um comentário no vídeo da resolução, achei mais simples que o Itemgatter que o
# professor explicou.
