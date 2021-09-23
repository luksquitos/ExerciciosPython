# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input("Digite aqui o valor do ângulo: "))

print("O valor do Seno é {:.2f}".format(math.sin(math.radians(ang))))
print("O valor do Cosseno é {:.2f}".format(math.cos(math.radians(ang))))
print("O valor da Tangente é {:.2f}".format(math.tan(math.radians(ang))))
