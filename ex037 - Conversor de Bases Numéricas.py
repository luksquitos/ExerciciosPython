# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

print('Digite um número para a conversão: ')
num = int(input('- '))
print('''Você gostaria de converter para qual dos a seguir ?
[A]- Binário
[B]- Hexadecimal
[C]- Octal''')
opcao = input('Digite uma opcão: ').upper()[0]

while not opcao in 'ABC:':
    opcao = input('Opcão inválida, tente novamente: ').upper()
if opcao == 'A':
    print(f'O número {num} em BINÁRIO é: {bin(num)}')
elif opcao == 'B':
    print(f'O número {num} em HEXADECIMAL é: {hex(num)}')
elif opcao == 'C':
    print(f'O número {num} em OCTAL é : {oct(num)}')
