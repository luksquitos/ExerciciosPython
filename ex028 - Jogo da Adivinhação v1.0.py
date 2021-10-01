#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero = random.randint(0, 5)
escolha = int(input('Qual número, de 0 à 5, você acha que o computador escolheu ? '))

if escolha >6:
    print('É ENTRE 0 À 5, JUBILEU')
if numero == escolha:
    print('Você acertou ')
else:
    print('Você errou ')
