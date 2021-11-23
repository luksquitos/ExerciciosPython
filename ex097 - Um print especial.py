# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com o tamanho adaptável.

def mensagem(x):
    print(f'{"~" * len(x) * 2}')
    print(f'{x:^{len(x) * 2}}')
    print(f'{"~" * len(x) * 2}')



mensagem(input('Digite uma frase aqui: '))

