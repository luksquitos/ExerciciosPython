# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from datetime import datetime

print(f'\033[1;32m{f"MEGA SENA {datetime.today().year}":.^50}')
cont = int(input('Quantos jogos você tentará esse ano ?\n- '))
gaveta = list()
jogosGerados = []
numeros = 6

while cont > 0:
    gaveta.append(randint(1, 60))
    numeros -= 1
    if numeros == 0:
        jogosGerados.append(gaveta[:])
        gaveta.clear()
        cont -= 1
        numeros = 6
print('\033[1;34m')
print('Os palpites gerados foram')
for jogos in jogosGerados:
    print(jogos)
print('BOA SORTE!!!')
