#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o Python e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()

print('Seu Python e ultimo nome é: {} {}'.format(div[0], div[len(div) - 1]))

#o 'len(div)' está contando quantas posições tem em div.


