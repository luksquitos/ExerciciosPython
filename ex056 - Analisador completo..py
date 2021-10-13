#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
mais_velho = 0
nome_mais_velho = str
tot_mulheres = 0

for c in range(1, 5):

    print(f'===={c}ªPESSOA====')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (F ou M): ')).upper()
    if idade > mais_velho:
        nome_mais_velho = nome
        mais_velho = idade
    media = idade + media
    if sexo == 'F' and idade < 20:
        tot_mulheres = tot_mulheres + 1

print(f'O mais velho é o {nome_mais_velho}, com {mais_velho} anos de idade.')
print(f'A média das idades é {media / 4}')
print(f'O número de mulheres com menos de 20 anos é {tot_mulheres}')

