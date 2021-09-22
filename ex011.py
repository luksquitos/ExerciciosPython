#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².

nome = str(input("Digite seu nome\n"))
alt = float(input("Digite o valor da altura\n"))
larg = float(input("Digite o valor da largura\n"))
area = alt*larg
tinta = area / 2

print("{}, serão necessários {} litros de tinta para pintar {} m² de área.".format(nome, tinta, area))

