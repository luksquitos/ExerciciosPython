# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

nome = nome_barato = continuar = ''
total_compra = produtos_maior = mais_barato = valor = 0
cont = 1  # Dirá quantos produtos foram comprados.

while True:
    nome = input(f'Digite aqui o nome do {cont}º produto: ')
    valor = float(input(f'Digite aqui o valor do {cont}º R$'))
    if cont == 1:
        mais_barato = valor
        nome_barato = nome
    if valor < mais_barato:
        mais_barato = valor
        nome_barato = nome
    if valor > 1000:
        produtos_maior += 1
    total_compra += valor

    continuar = input('Você gostaria de continuar ? [S/N]').upper()
    if continuar == 'N':
        break
    cont += 1

print('='*50)
print(f'O total gasto na compra foi de R${total_compra:.2f} e foram {cont} produtos adquiridos')
print(f'A quantidade de produtos com mais de R$1000 reais são {produtos_maior}')
print(f'O nome do produto mais barato é {nome_barato} custando R${mais_barato}')

