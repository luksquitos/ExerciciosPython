# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de {largura}m e {comprimento} é {a}m²')


area(int(input('Largura: ')), int(input('Comprimento: ')))
