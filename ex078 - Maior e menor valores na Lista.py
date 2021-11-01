# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

from math import trunc

lista = []

print('\033[1;33mDigite aqui 5 valores')
print('\033[1;31m!!SOMENTE SERÃO ACEITOS VALORES INTEIROS!!\033[m')

for posicao, cont in enumerate(range(1, 6)):
    lista.append(input(f'Digite o {cont}º valor: '))
    while lista[posicao].isalnum() and not lista[posicao].isnumeric():  # Toda essa parte é pra evitar que o programa
        lista.pop(posicao)                                              # fosse interrompido por erro.
        print('Você deve escrever apenas números')
        lista.append(input(f'Digite o {cont}º valor'))
    else:
        lista[posicao] = trunc(float(lista[posicao]))  # Somente serão aceitos números inteiros.
print('-' * 50)
print(f'A lista criada foi: {lista}\n')
print(f'O maior valor na lista foi {max(lista)} e ele se encontra na {lista.index(max(lista)) + 1}ª posição')
print(f'O menor valor na lista foi {min(lista)} e ele se encontra na {lista.index(min(lista)) + 1}ª posição')
