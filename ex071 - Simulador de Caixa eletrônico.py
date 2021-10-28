# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print(f'\033[1;33m{"BANCO DO JACOLELÊ":=^70}\033[m')
num = int(input('Digite um valor para saque:\nR$'))
cinq = vint = dez = um = resto = 0

while True:
    cinq = num // 50
    resto = num % 50
    vint = resto // 20
    resto = resto % 20
    dez = resto // 10
    resto = resto % 10
    um = resto // 1
    break

print(f'''O Valor sacado será:
~R$50: {cinq} notas
~R$20: {vint} notas
~R$10: {dez} notas
~R$1: {um} notas''')
