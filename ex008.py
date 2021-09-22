#Escreva um programa que leia um valor em metros e exibe convertido em centimetros e milímetros.

valor = int(input("Digite aqui um valor para ser convertido \n"))
cent = valor*100
mili = valor*1000

print("O valor de {} metros em centimetros é {}\n e em milimetros é {}".format(valor, cent, mili))
