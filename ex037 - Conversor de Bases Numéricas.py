#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

print('Digite um número para a conversão: ')
num = int(input('- '))
x = num / 2
y = num % 2

print(x, '\n', y)
print(x / 2 != 0)

