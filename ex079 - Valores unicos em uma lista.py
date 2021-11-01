# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente

from math import trunc

lista = []

pergunta = 'S'
num = ''

while pergunta == 'S':
    num = input('Digite aqui um número inteiro: ')
    while not num.isnumeric():
        num = input('Você tem que digitar um número inteiro: ')
    else:
        num = int(num)

        if num not in lista:
            lista.append(num)
            print(f'\033[1;32mO valor {num} foi adicionado\033[m')
        else:
            print(f'\033[1;33mO valor {num} já está na lista\033[m')
        pergunta = input('Você gostaria de continuar? [S/N] ').upper()
        while not pergunta in 'SN':
            pergunta = input('SIM OU NÃO? [S/N] ').upper()
print()
print(f'Os números adicionados em ordem foram\n{sorted(lista)}')
print(f'{"PROGRAMA FINALIZADO":=^60}')
