#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hiponenusa.

import math

cat1 = float(input("Digite o valor do Cateto Oposto: "))
cat2 = float(input("Digite o valor do Cateto Adjacente: "))
print("O valor da Hipotenusa é {:.2f}".format(math.sqrt(math.pow(cat1, 2) + math.pow(cat2, 2))))


#Tem outros dois modos de fazer. Vou deixar o método mais simples aqui

#hip = (cat1**2 + cat2**2) ** 1/2

#ou então, utilizando;

#hip = math.hypot (cat1, cat2)

