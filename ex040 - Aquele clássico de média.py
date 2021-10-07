#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

print('Digite aqui suas notas:')
n1 = float(input('- '))
n2 = float(input('- '))

if (n1 + n2) / 2 < 5.0:
    print('\033[1;31mREPROVADO!')
elif 5.0 <= (n1 + n2) / 2 <= 6.9:
    print(f'\033[1;33mRECUPERAÇÃO!')
elif (n1 + n2) / 2 >= 7.0:
    print(f'\033[1;32mAPROVADO!')

print(f'Sua média foi {(n1 + n2) / 2}')
