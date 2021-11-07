# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
cadastradas = 0
pergunta = 'S'

while pergunta == 'S':
    dados.append(input('Nome: '))
    dados.append(input('Peso: '))
    try:
        dados[1] = float(dados[1])
    except:
        print('\033[1;31mVocê digitou um peso inválido. Tente novamente.\033[m')
        dados.clear()
        continue
    pessoas.append(dados[:])
    dados.clear()
    cadastradas += 1
    pergunta = input('Gostaria de continuar ? [S/N]').upper()
    while pergunta not in 'SN':
        pergunta = input('S/N?! ').upper()
pesados = list()
leves = list()

for a in pessoas:
    if a[1] >= 100:
        pesados.append(a[0])
    elif a[1] <= 70:
        leves.append(a[0])
print('\033[1;33m')
print(f'Foram cadastrados {cadastradas} pessoas: ')
print(f'Os mais pesados cadastrados foram : {pesados}')
print(f'Os mais leves cadastrados foram : {leves}')
