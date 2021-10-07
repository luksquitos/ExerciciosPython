# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('Digite os valores dos lados:')
l1 = float(input('- '))
l2 = float(input('- '))
l3 = float(input('- '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    #print('Esses lados formam um triângulo')
    if l1 != l2 != l3:
        print('Escaleno')
    elif l1 == l2 !=l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('Isóceles')
    elif l1 == l2 == l3:
        print('Equilátero')
else:
    print('Esses lados não formam triângulo')

