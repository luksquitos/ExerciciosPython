#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = str(input("Digite seu nome\n"))
salario = float(input("{}, digite seu salário R$".format(nome)))

print("{}, seu salário reajustado foi de R${:.2f} reais".format(nome, salario*1.15))