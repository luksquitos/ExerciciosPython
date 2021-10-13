#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print('\033[1;35mO que você escolhe, meu brow?')
print('\033[1;33m(1) - Pedra\n(2) - Papel\n(3) - Tesoura\033[m')
opcao = int(input('\033[1;35mMAKE YOUR CHOICE! - \033[m'))
lista = ['Pedra', 'Papel', 'Tesoura']
maquina = choice(lista)

print('\033[1;36mTAM')
sleep(1)
print('TAMM')
sleep(1)
print('TAMMMMMMMM')
sleep(1)


if opcao > 3 or opcao == 0:
    print('\033[1;31mNão irás me enganar,CABRON!!')
else:
    if lista[opcao - 1] == maquina:
        print('\033[1;33mVocês empataram!\033[m')
    elif lista[opcao - 1] == 'Pedra' and maquina == 'Tesoura':
        print('\033[1;36mVOCÊ APEDREJOU A MÁQUINA!\033[m')
    elif lista[opcao - 1] == 'Tesoura' and maquina == 'Pedra':
        print('\033[1;31mA MÁQUINA APEDREJOU VOCÊ!\033[m')
    elif lista[opcao - 1] == 'Tesoura' and maquina == 'Papel':
        print('\033[1;36mVOCÊ FATIOU A MAQUINA EM PEDAÇINHOS!\033[m')
    elif lista[opcao - 1] == 'Papel' and maquina == 'Tesoura':
        print('\033[1;31mA MÁQUINA FATIOU VOCÊ EM PEDAÇINHOS!\033[m')
    elif lista[opcao - 1] == 'Papel' and maquina == 'Pedra':
        print('\033[1;36mVOCÊ EMBRULHOU A MAQUINA PRA PRESENTE!\033[m')
    elif lista[opcao - 1] == 'Pedra' and maquina == 'Papel':
        print('\033[1;31mA MAQUINA EMBRULHOU VOCÊ PRA PRESENTE!\033[m')

    print(f'Você escolheu {lista[opcao - 1]}\nA máquina escolheu {maquina}')

#FIQUEI ORGULHOSO DESSE CÓDIGO
# -SUGOI SUGOI


