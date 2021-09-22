#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

nome = str(input("Digite seu nome\n"))
valor = float(input("Digite o valor do produto\n"))

print("{}, o valor reajustado é {:.2f} reais".format(nome, valor*0.95))
