# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('Qual tabuada você gostaria de saber ?\033[1;35m')
n = int(input('- '))

for c in range(1, 11):
    print(n, 'X', c, '=', n*c)
