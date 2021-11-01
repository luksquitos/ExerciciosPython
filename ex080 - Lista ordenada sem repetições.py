# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
num = ''
cont = 0

for vezes in range(1, 11):
    num = input('Digite um número inteiro: ')
    while not num.isnumeric():
        num = input('Você deve digitar um número inteiro: ')
    num = int(num)
    cont += 1
    if cont == 1:
        #print('O valor foi adicionado na posição 0')
        lista.append(num)
        continue
    if cont == 2:
        if num <= lista[0]:
            lista.insert(0, num)
            #print('O valor assumiu a posição 0')
            continue
        else:
            lista.append(num)
            #print('O valor foi adicionado ao final')
            continue
    for posicao, numero in enumerate(lista):
        if num <= numero:
            lista.insert(posicao, num)
            break
        elif num > lista[-1]:
            lista.append(num)
            break

print(lista)
