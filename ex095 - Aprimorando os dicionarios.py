# Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.


pergunta = 'S'
registro = []

while pergunta == 'S':
    gaveta = {'Nome': input('Nome do Jogador: '), 'Jogos': int(input('Quantidade de Jogos: '))}
    numJogos = gaveta['Jogos']
    somaGols = 0
    for golsporjogos in range(1, numJogos + 1):
        gaveta[f'Gols no {golsporjogos}º Jogo'] = int(input(f'Gols no {golsporjogos}º jogo: '))
        somaGols += gaveta[f'Gols no {golsporjogos}º Jogo']
    gaveta['Soma de gols'] = somaGols
    registro.append(gaveta.copy())
    gaveta.clear()
    pergunta = input('Gostaria de continuar ? [S/N]').upper()

for jogador in registro:
    for k, v in jogador.items():
        print(f'{k}: {v}')
    print('-' * 10)


