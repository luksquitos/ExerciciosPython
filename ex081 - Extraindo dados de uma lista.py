# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
resp = 'S'
num = ''

while resp == 'S':
    num = input('Digite aqui um valor inteiro: ')
    while not num.isnumeric():
        print('NÚMERO INVÁLIDO')
        num = input('Tente novamente: ')
    num = int(num)
    lista.append(num)
    resp = input('Gostaria de continuar ? [S/N]').upper()
    while resp not in 'SN':
        resp = input('SIM OU NÃO [S/N]')

print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
print('O valor 5 está na lista' if 5 in lista else 'O valor 5 não está na lista')
# Coloquei print depois do else e ele me retornou none no final. Não entendi essa parte
