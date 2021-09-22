# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

nome = str(input("Escreva seu nome "))
dia = int(input("{}, quantos dias o carro foi alugado ? ".format(nome)))
km: float = float(input("{}, quantos Km foram rodados ? ".format(nome)))
total = 60*dia + 0.15*km

print("{}, você terá que pagar R$ {} reais".format(nome, total))
