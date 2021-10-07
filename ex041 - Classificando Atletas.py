#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import datetime

ano = int(input('Digite aqui o ano que você nasceu: '))
atual = datetime.today().year
idade = atual - ano
cores = {'padrao': '\033[m', 'ciano': '\033[1;36m', 'amarelo': '\033[1;33m', 'verde': '\033[1;32m',
         'vermelho': '\033[1;31m', 'azul': '\033[1;34m'}


if idade <= 9:
    print('{}Você pertence a categoria MIRIM'.format(cores['ciano']))
elif 9 < idade <= 14:
    print('{} Você pertence a categoria INFANTIL'.format(cores['amarelo']))
elif 14 < idade <= 19:
    print('{}Você pertence a categoria JUNIOR'.format(cores['verde']))
elif 19 < idade <= 25:
    print('{}Você pertence a categoria SENIOR'.format(cores['vermelho']))
elif idade > 25:
    print('{}Você pertence a categoria MASTER'.format(cores['azul']))

print(f'Sua idade é {idade} anos')


