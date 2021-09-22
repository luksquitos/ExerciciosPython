#Converta um programa que converta uma temperatura digitada em °C e converta para °F.

C = float(input("Digite o valor em Celcius "))
F = (9*C + 160) / 5

print("O valor {}°C, em Fahrenheit, é {}°F".format(C, F))
