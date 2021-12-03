# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(msg):
    validação = False
    while True:
        num = input(msg)
        if not num.isnumeric():
            print('\033[1;31mErro!\033[m')
            continue
        else:
            num = int(num)
            validação = True
        if validação:
            break
    return num


n = leiaInt('Escreva alguma coisa: ')
print(f'O numero é {n}')
