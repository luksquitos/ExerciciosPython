# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

print(f'{"Cadastro de alunos":.^50}')
pergunta = 'S'
gaveta = []
registro = []
cont = soma = 0
while pergunta == 'S':
    gaveta.append(input('Nome: '))
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    gaveta.append((n1 + n2) / 2)
    gaveta.append(n1)
    gaveta.append(n2)
    registro.append(gaveta[:])
    gaveta.clear()
    pergunta = input('Gostaria de continuar ? [S/N]').upper()
    while pergunta not in 'SN':
        pergunta = input('S ou N?').upper()
print()
print(f'{"Nº NOME":.<10}', end='')
print('MÉDIA')
print('-' * 15)
for num, aluno in enumerate(registro):
    for elem in range(0, 2):
        if elem == 0:
            print(f'{num} {aluno[elem]:.<10}', end='')
        elif elem == 1:
            print(aluno[elem])
print('Você gostaria de ver as notas de quem ? (999 para encerrar)')
perguntaAluno = int(0)
while perguntaAluno != 999:
    perguntaAluno = int(input('Digite um número válido: '))
    try:
        if perguntaAluno == 999:
            print(f'{"PROGRAMA ENCERRADO":-^50}')
            break
        else:
            print('.' * 10)
            print(f'Aluno: {registro[perguntaAluno][0]}')
            print(f'Nota 1: {registro[perguntaAluno][2]}')
            print(f'Nota 2: {registro[perguntaAluno][3]}')
            print(f'Média: {registro[perguntaAluno][1]}')
    except:
        print('Você digitou um número inválido')
        continue
