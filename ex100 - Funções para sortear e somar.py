# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
# valores pares sorteados pela função anterior.

from random import randint

numeros = list()


def sorteia():
    print('Os números sorteados foram: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(n, end=' ')
    print()


def somaPar(x):
    somaPar = 0
    print(f'A soma dos pares é: ', end='')
    for numero in x:
        if numero % 2 == 0:
            somaPar += numero
    print(somaPar)


sorteia()
somaPar(numeros)
