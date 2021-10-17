#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('''\033[1;33mDigite aqui vários valores.
\033[1;31mPara parar o programa, digite "999"\033[m''')

valor = 0
soma = 0
total = 0

while valor != 999:
    valor = int(input('- '))
    if valor == 999:
        continue  #O continue vai impedir que o resto do while seja lido, voltando pro começo.
    soma += valor
    total += 1

print(f'\033[1;32mO total de números escritos foram {total}\n\033[1;33mA soma foi {soma}')
