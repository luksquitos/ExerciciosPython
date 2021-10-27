#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
print(f'{"TABUADA":=^40}')
print('\033[1;31m!Para parar o programa, digite um valor negativo!\033[m')
num = 0
cont = 1

while num >= 0:
    num = int(input('Qual tabuada você gostaria de saber ?\n- '))
    if num < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
print(f'Você digitou um número negativo\n\033[1;31m{"FIM DA EXECUÇÃO DO PROGRAMA":=^40}')
