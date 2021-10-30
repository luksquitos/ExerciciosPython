# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print('Digite aqui quatro valores: ')

numeros = (int(input('- ')), int(input('- ')),
           int(input('- ')), int(input('- ')))
num_pares = []

print(f'A quantidade de vezes que apareceu o número 9 foi {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro número 3 se encontra na posição {numeros.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares são: ', end='')

for analisador in numeros:
    if analisador % 2 == 0:
        print(analisador, end=' ')
