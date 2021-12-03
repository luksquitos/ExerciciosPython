# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

jogador = {'Nome': input('Nome do Jogador: '), 'quantJogos': int(input('Quantidade de partidas: '))}
gols = []
cont = 1
somaGols = 0

while cont != jogador['quantJogos'] + 1:
    # jogador[f'GolsnoJogo{cont}'] = int(input(f'Quantidade de Gols no {cont}ºJogo: '))
    gols.append(int(input(f'Gols no {cont}ºJogo: ')))
    cont += 1
jogador['Gols'] = gols

for jogo, gol in enumerate(jogador['Gols']):
    print(f'Na partida {jogo + 1} teve {gol} gols')
    somaGols += gol

print(f'\nFoi um total de {somaGols} gols.')
