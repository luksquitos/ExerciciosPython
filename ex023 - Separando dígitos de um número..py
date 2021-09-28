#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input("Digite um número de 0 à 9999 "))

print('unidade: {}' .format(num[len(num) - 1]))
print("dezena: {}".format(num[len(num) - 2]))
print("centena : {}".format(num[len(num) - 3]))
print("milhar : {}" .format(num[len(num) - 4]))
