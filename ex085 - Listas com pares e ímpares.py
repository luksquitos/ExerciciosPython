# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

pares = []
impares = []
valores = []
num = 0

for vez in range(1, 8):
    num = int(input(f'Digite aqui o {vez}º número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
valores.append(pares[:])
valores.append(impares[:])
valores[0].sort()
valores[1].sort()


print(f'''Os valores pares são {valores[0]}
e os valores ímpares são {valores[1]}''')
