# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Abacate', 30.00, 'Banana', 2, 'Cookies', 4.50, 'Picanha', 75.00, 'Gasolina', 8)

print(f'{"SACOLÉ DO JUBILEU":=^40}')
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<35}', end='')
    else:
        print(f'{lista[c]:.2f}')
