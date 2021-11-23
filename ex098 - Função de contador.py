from time import sleep


def contador(x, y, z):
    w = 0
    if z >= 0:
        w = 1
    else:
        w = -1
    if z == 0:
        z = 1
    print('.' * 30)
    print(f'CONTANDO DE {x} ATÉ {y} DE {z} EM {z}')
    for cont in range(x, y + w, z):
        print(cont, end=' ')
        sleep(0.5)
    print()
    print('.' * 30)


contador(1, 10, 1)
contador(10, 0, -1)
print('SUA VEZ DE ESCOLHER OS NÚMEROS!')
contador(int(input('Começo: ')), int(input('Fim: ')), int(input('Frequência: ')))
