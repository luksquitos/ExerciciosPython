#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str

while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo [M/F]: ').upper()
    print('\033[1;31mTente novamente!\033[m')
print('='*20)
