# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vit = maquina = num = soma = 0
escolha = ''

while True:
    maquina = randint(0, 11)
    num = int(input('Que número você escolhe ? '))
    escolha = input('Você escolhe par ou ímpar ? [P/I]').upper()
    soma = num + maquina
    if soma % 2 == 0:
        if escolha == 'P':
            print(f'Você escolheu: {num} e {escolha}\nMáquina: {maquina}\nSoma {soma}\n\033[1;36m{"Você venceu":=^50}'
                  f'\033[m')
            vit += 1
        else:
            print(f'Você escolheu: {num} e {escolha}\nMáquina: {maquina}\nSoma {soma}\n\033[1;31m{"Você perdeu":=^50}'
                  f'\033[m')
            break
    else:
        if escolha == 'I':
            print(f'Você escolheu: {num} e {escolha}\nMáquina: {maquina}\nSoma {soma}\n\033[1;36m{"Você venceu":=^50}'
                  f'\033[m')
            vit += 1
        else:
            print(f'Você escolheu: {num} e {escolha}\nMáquina: {maquina}\nSoma {soma}\n\033[1;31m{"Você perdeu":=^50}'
                  f'\033[m')
            break
print(f'\033[1;33mVocê venceu a máquina com {vit}vitórias consecutivas')
