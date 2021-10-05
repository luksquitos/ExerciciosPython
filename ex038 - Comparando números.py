#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#-O Python valor é maior
#-O segundo valor é maior
#-Não existe valor maior. Os dois são iguais

print('Digite dois valores')
n1 = int(input('- '))
n2 = int(input('- '))

if n1 > n2:
    print(f'O valor maior é {n1}')
elif n2 > n1:
    print(f'O valor maior é {n2}')
elif n1 == n2:
    print('Os dois valores são iguais')
