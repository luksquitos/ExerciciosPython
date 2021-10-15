#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''n = int(input('digite um número: '))
s = 1
for c in range(n, 0, -1):
    s = s * c
print(s)'''

d = e = s = int
while d != 0:
    d = int(input('digite um número: '))
    s = 1
    while d != 0:
        s = s * d
        d = d - 1
print(f'O valor de {d}! é {s}') #O d está mostrando 0, ao inves do valor fornecido.
