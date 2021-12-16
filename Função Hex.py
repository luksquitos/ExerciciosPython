# Essa função foi criada para substituir 6 "if's".
def sub(a, b, c):
    """
    Essa função converte os números maiores ou igual a 10 em suas respectivas letras.
    Ela será chamada dentro da função posterior em que...
    :param a: Será o número da posição na lista "rest"
    :param b:Será a variável "num" em que trará o número para a conversão
    :param c:Será a lista "rest" inteira
    """
    letras = 'ABCDEF'
    letra_escolhida = b - 10
    del (c[a])  # Apaga o "num"
    c.insert(a, letras[letra_escolhida])  # Adiciona a letra correspondente ao "num"


# Função principal.
def hex(x):
    """
    Função que fará as divisões sucessivas
    :param x: receberá o número decimal informado pelo usuário.
    """
    rest = []
    div = x
    while True:
        ultimo_valor = div // 16
        rest.append(div % 16)
        div = ultimo_valor
        if div < 16:
            break

    print(end=f'\033[1;32mO número {x} em Hex é: \033[1;36m')
    rest.append(div)  # Coloquei esse valor dentro da lista para caso o ultimo divisor inteiro ser maior que 10
    for cont in range(len(rest) - 1, -1, -1):
        num = rest[cont]
        if num >= 10:
            sub(cont, num, rest)
            num = rest[cont]
        print(end=f'{num}')


print(f'\033[1;33m{"Conversor de Decimal para Hexadecimal":.^50}')
numero = input('Digite um número: ')
while not numero.isnumeric():
    print('\033[1;31mVocê digitou um número inválido')
    numero = input('Tente novamente: \033[m')
numero = int(numero)
hex(numero)
