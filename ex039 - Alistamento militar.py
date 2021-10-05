#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

#-Se ele ainda vai se alistar ao serviço militar
#-Se é a hora de se alistar.
#-Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Digite sua idade: '))

if idade < 18:
    print(f'\033[1;32mAinda faltam {18 - idade} anos para você se alistar\033[m')
elif idade == 18:
    print('\033[1;33mChegou a hora de você se alistar.\033[m')
else:
    print(f'\033[1;31mVocê deveria ter se alistado {idade - 18} anos atrás\033[m')
