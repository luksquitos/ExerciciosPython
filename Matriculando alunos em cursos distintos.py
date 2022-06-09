# Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas Lógica e Linguagem de
# Programação. Coloque os números das matriculas dos alunos que cursam Lógica em um vetor, no máximo quinze alunos.
# Coloque os números das matriculas dos alunos que cursam Linguagem de Programação em outro vetor, no máximo dez
# alunos. Mostre o número das matriculas que aparecem nos dois vetores.
from random import randint
logica = []
linguagem = []
matriculados_logica = matriculados_linguagem = 0
while True:
    if matriculados_linguagem != 10 and matriculados_logica != 15:
        #num_matricula = input('Numero de matricula: ')
        num_matricula = randint(1, 1000)
        print('Você cursa qual dos cursos abaixo ?')
        print('''        A) Lógica de programação
        B)Linguagem de programação
        C)Ambos''')
        #gaveta = dict()
        opcao = input('- ').upper()
        if opcao == 'A':
            logica.append(num_matricula)
            matriculados_logica += 1
        elif opcao == 'B':
            linguagem.append(num_matricula)
            matriculados_linguagem += 1
        elif opcao == 'C':
            logica.append(num_matricula)
            linguagem.append(num_matricula)
            matriculados_logica += 1
            matriculados_linguagem += 1

    elif matriculados_linguagem == 10 and matriculados_logica != 15:
        num_matricula = input('Número de matricula: ')
        logica.append(num_matricula)
        print('O Curso de linguagem já está cheio, você só pode entrar no de Lógica')
        matriculados_logica += 1

    elif matriculados_linguagem != 10 and matriculados_logica == 15:
        num_matricula = input('Número de matricula: ')
        linguagem.append(num_matricula)
        print('O Curso de lógica já está cheio, você só pode entrar no de Linguagem')
        matriculados_linguagem += 1

    elif matriculados_linguagem == 10 and matriculados_logica == 15:
        break

print(logica)
print(linguagem)






