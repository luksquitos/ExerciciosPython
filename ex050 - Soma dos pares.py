#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0

for c in range(1, 7):
    n = int(input('\033[1;32mDigite um número '))
    if n % 2 == 0:
         s = s + n

print('\033[1;33mA soma dos pares é {}'.format(s))
