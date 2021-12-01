# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador se chama {nome} e fez {gols} na temporada')


n = input('Nome: ').strip()
g = input('Gols: ')

while not g.isnumeric():
    g = input('Digite um valor numérico: ')
g = int(g)

if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
