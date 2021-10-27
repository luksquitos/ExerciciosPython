# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

pergunta = sexo = ''
idade = 0
cont_maior = cont_mulher_menor = cont_homem = 0


while True:
    idade = int(input('Digite aqui sua idade: '))
    sexo = input('Digite aqui seu sexo: [M/F]').upper()
    if not sexo == 'M' and not sexo == 'F':
        print('\033[1;31mSEXO INVÁLIDO, TENTE NOVAMENTE!\033[m')
        print()
        continue
    if idade > 18:
        cont_maior += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher_menor += 1
    pergunta = input('Você gostaria de continuar ? [S/N]').upper()
    if pergunta == 'N':
        break
    print()  # Linha vazia
print('\033[1;33m=\033[m'*60)
print(f'Pessoas com mais de 18 anos: {cont_maior}\nHomens cadastrados: {cont_homem}\nMulheres com menos de 20 anos:'
      f' {cont_mulher_menor}')


