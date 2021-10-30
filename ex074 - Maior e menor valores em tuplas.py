# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
numeros = (n1, n2, n3, n4, n5)  # Pode colocar os randint dentro da tupla direto.


print(f'A sequência escolhida foi {numeros}')
print(f'O maior valor gerado foi {sorted(numeros)[-1]}')  # Pode usar a função max()
print(f'O menor valor gerado foi {sorted(numeros)[0]}')   # Pode usar a função min()


