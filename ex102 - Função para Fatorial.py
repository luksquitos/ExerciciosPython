# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    Função para calcular um fatorial
    :param num: Valor de entrada dada pelo usuário
    :param show: True or False, também modificado pelo usuário
    :return: Retorna o valor do resultado
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            print(end=' X ' if c > 1 else f' = {f}')
        f *= c
    return f

print('Escolha um número para saber o fatorial')
print(fatorial(int(input('- ')), False))  # O valor False ou True modifica o valor de Show de dentro da função
