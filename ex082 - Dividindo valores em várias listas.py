# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.Ao final, mostre o conteúdo das três listas geradas.

lista = []
resposta = 'S'

while resposta == 'S':
    lista.append(input('Digite aqui um valor inteiro: '))
    while not lista[-1].isnumeric():
        lista.pop(-1)
        lista.append(input('Você deve digitar um número inteiro: '))
    lista[-1] = int(lista[-1])
    resposta = input('Você gostaria de continuar ? [S/N]: ').upper()
    while resposta not in 'SN':
        resposta = input('SIM OU NÃO ? [S/N]: ').upper()

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Os números pares digitados foram: {pares}'if len(pares) >= 1 else 'Nessa lista não há valores pares')
print(f'Os números ímpares digitados foram: {impares}' if len(impares) >= 1 else 'Nessa lista não há valores ímpares')
