#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

n = int(input('digite o primeiro valor: '))
r = int(input('digite a razão: '))
c = n
s = 0
cont = 0

while cont < 10:
    if cont == 0:
        print(f'1º termo = {c}')
        cont = 1
    s = s + c + r
    c = 0
    cont += 1
    print(f'{cont}º termo: {s}')
