#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Digite os valores dos lados do triângulo. ')
l1 = float(input('- '))
l2 = float(input('- '))
l3 = float(input('- '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2): # Não seriam necessários esse parenteses.
    print('Essas medidas formam um triângulo')
else:
    print('Essas medidas NÃO formam um triângulo')
