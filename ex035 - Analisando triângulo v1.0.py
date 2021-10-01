#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Digite os valores dos lados do triângulo. ')
l1 = float(input('- '))
l2 = float(input('- '))
l3 = float(input('- '))

if |l2 - l3| < l1 < l2 + l3: