#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor da casa. '))
salario = float(input('Digite seu salário. '))
anos = int(input('Digite em quantos anos você deseja pagar. '))
parcela = (valor / anos) / 12


if parcela > salario*1.30:
    print('O empréstimo foi negado')
    print(f'Seu salário é:\033[1;31mR${salario}\033[m\nA prestação é:\033[1;36mR${parcela:.2f}')
else:
    print('O empréstimo foi aceito')
    print(f'Seu salário é:\033[1;31mR${salario}\033[m\nA prestação é:\033[1;36mR${parcela:.2f}')
