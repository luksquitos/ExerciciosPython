#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano = int(input('Digite o ano que você nasceu: '))
cores = {'padrao': '\033[m', 'vermelho': '\033[1;31m', 'amarelo': '\033[1;33m', 'verde': '\033[1;32m'}
atual = datetime.today().year

if atual - ano < 18:
    print('{}Você tem {} anos e lhe faltam {} para se alistar no exército'.format(cores['verde'], atual - ano, 18 - (atual - ano),))
elif atual - ano == 18:
    print('{}Chegou a hora de você se alistar no exército' .format(cores['amarelo']))
elif atual - ano > 18:
    print('{}Já passou {} anos do seu prazo de alistamento'.format(cores['vermelho'], (atual - ano) - 18))
