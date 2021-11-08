# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = maiorValorSegunda = somaTerceira = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        try:
            matriz[linha][coluna] = int(input(f'Digite um valor para {linha}:{coluna} '))
            if matriz[linha][coluna] % 2 == 0:
                somaPares += matriz[linha][coluna]
            if coluna == 2:
                somaTerceira += matriz[linha][coluna]
            if linha == 1:
                maiorValorSegunda = max(matriz[1])
        except:
            print('Você digitou um número inválido!')

print(f'\033[1;32m{"A MATRIZ FOI":.^40}')
for c in matriz:
    print(c)
#print(matriz)

print(f'\033[1;33mA soma de todos os pares digitados foi {somaPares}')
print(f'A soma dos valores da terceira coluna foram {somaTerceira}')
print(f'O maior valor da segunda linha foi o nº {maiorValorSegunda}')
