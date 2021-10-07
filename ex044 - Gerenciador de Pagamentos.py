#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: R$'))
print('De que forma você gostaria de pagar ?')
print('1 - À Vista no Dinheiro/Cheque: 10% de desconto\n2 - À vista no cartão: 5% de desconto\n3 - Até 2x no cartão: '
      'preço formal\n4 - 3x ou mais no cartão: 20% de juros')
opcao = int(input('- '))

if opcao > 4:
    print('\033[1;31mOPÇÃO INVÁLIDA')
else:
    print('\033[1;36m')
    if opcao == 1:
        print(f'Você irá pagar R$ {valor * 0.9}')
    elif opcao == 2:
        print(f'Você irá pagar R$ {valor * 0.95}')
    elif opcao == 3:
        print(f'Você irá pagar R$ {valor}')
    elif opcao == 4:
        print(f'Você irá pagar R$ {valor * 1.2}')
