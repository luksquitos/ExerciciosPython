# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['media'] > 6:
    aluno['situação'] = '\033[1;32mAprovado'
elif aluno['media'] == 6:
    aluno['situação'] = '\033[1;33mPassou de raspão'
elif aluno['media'] < 6:
    aluno['situação'] = '\033[1;31mReprovado'
print('--X--' * 4)
for k, v in aluno.items():
    print(f'{k}:{v}')


