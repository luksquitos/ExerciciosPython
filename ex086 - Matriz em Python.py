# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for coluna in range(0, 3):
    for linha in range(0, 3):
        matriz[coluna][linha] = int(input(f'Digite um valor para {coluna}:{linha}: '))
print(f'{"A matriz é":.^20}')
for coluna in range(0, 3):
    for linha in range(0, 3):
        print(matriz[coluna][linha], end='/ ')
    print()
