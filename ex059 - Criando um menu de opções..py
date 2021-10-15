#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0

while opcao < 5:
    opcao = 0
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    while opcao < 4:
        print('''O que você gostaria de fazer com esses valores ?
        [1] Somar.
        [2] Multiplicar.
        [3] Saber quem é o maior.
        [4] Inserir novos números.
        [5] Encerrar programa.''')
        opcao = int(input('- '))
        if opcao == 1:
            print(f'A soma dos dois algarismos é {n1 + n2}')
        elif opcao == 2:
            print(f'A multiplicação dos dois algarismos é {n1 * n2}')
        elif opcao == 3:
            if n1 > n2:
                print(f'{n1} é maior que {n2}')
            else:
                print(f'{n2} é maior que {n1}')

print('\033[1;31mO programa foi encerrado!!')
