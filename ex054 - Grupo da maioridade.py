#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

print('Digite aqui 7 anos de nascimento:')
atual = datetime.today().year
maioridade = 0
menoridade = 0

for c in range(1, 8):
    ano = int(input('- '))
    if atual - ano >= 18:
        maioridade = maioridade + 1
        #print(f'A idade {atual - ano} já atingiu a maioridade')
    else:
        menoridade += 1
        #print(f'A idade {atual - ano} faltam {18 - (atual - ano)} anos para atingir a maioridade')

print(f'{maioridade} pessoas atingiram a maioridade.')
print(f'{menoridade} não atingiram a maioridade.')
