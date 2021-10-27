#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('Digite aqui vários valores:')
print('Digite "999" para parar.')
valor = quant = soma = 0

while True:
    valor = int(input('- '))
    if valor == 999:
        break
    soma += valor
    quant += 1

print(f'O total de números digitados foram {quant} e a soma entre eles foi de {soma}.')
print(f'\033[1;31m{"FIM":=^70}')