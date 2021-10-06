#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

print('Digite dois números: ')
n1 = int(input('- '))
n2 = int(input('- '))

if n1 > n2:
    print(f'{n1} é Maior')
elif n2 > n1:
    print(f'{n2} é Maior')
elif n1 == n2:
    print('\033[1;33mOs dois valores são iguais')
