# Escrevendo todos os números primos de 1 à 500

num = 0
num_primos = []

while num < 501:
    cont = 0
    num += 1
    for div in range(1, num + 1):
        if num % div == 0:
            cont += 1
            if num == div:
                if cont <= 2:
                    num_primos.append(num)
print(num_primos)