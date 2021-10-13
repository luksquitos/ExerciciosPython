#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa , o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

cores = {'padrao': '\033[m', 'ciano': '\033[1:36m', 'vermelho': '\033[1:31m'}
casa = float(input('Digite o valor da casa: -'))
salario = float(input('Digite seu salário: -'))
anos = int(input('Digite em quantos anos você quer pagar'))
prestacao = (casa / anos) / 12

if prestacao > salario*0.3:
    print('{}O EMPRÉSTIMO FOI RECUSADO{}'.format(cores['vermelho'], cores['padrao']))
else:
    print('{}O EMPRÉSTIMO FOI ACEITO{}'.format(cores['ciano'], cores['padrao']))

print(f'Salário: R${salario}\nParcela: R${prestacao:.2f}')
