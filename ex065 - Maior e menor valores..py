#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = 0
total = 1
soma = 0
resposta = 'S'
maior = 0
menor = 0

while resposta == 'S':
    n = int(input('Digite um valor: '))
    if n > maior:
        maior = n
    if total == 1:
        menor = n
    if n < menor:
        menor = n
    soma += n
    total += 1
    resposta = input('Você quer continuar ? [S/N] ').upper()
    if resposta != 'S' and resposta != 'N':
        print('\033[1;31mComando inválido\033[m')
        continue
print(f'A média foi de {soma / total:.2f}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

