# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações: - Quantidade de notas - A maior nota - A menor nota - A média da turma - A situação (
# opcional) Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*notas):
    """
    Função criada para ler notas de alunos
    :param notas: Recebe números float e inteiros de notas de alunos
    :return: Caso notas receba parâmetros que não sejam números ou números maiores que 10 receberá um erro imediato
    """
    for elemento in notas:
        if elemento == str(elemento):
            return print('\033[1;31mVocê só pode escrever números!\033[m')
        elif elemento > 10:
            return print('\033[1;31mVocê só pode cadastrar notas menores que 10\033[m')
    gaveta = dict()
    registro = list()
    somaNotas = cont = 0

    while True:
        gaveta['Nome'] = f'Aluno {cont + 1}'
        gaveta['Nota'] = notas[cont]
        somaNotas += gaveta['Nota']
        if notas[cont] >= 6:
            gaveta['Situação'] = '\033[1;32mAPROVADO\033[m'
        else:
            gaveta['Situação'] = '\033[1;31mREPROVADO\033[m'
        registro.append(gaveta.copy())
        gaveta.clear()
        cont += 1
        if cont == len(notas):
            break
    gaveta['Media das notas'] = f'{somaNotas / len(notas):.2f}'
    gaveta['Quantidade de notas'] = len(notas)
    gaveta['Maior nota'] = max(notas)
    gaveta['Menor nota'] = min(notas)
    # Gaveta não foi limpa
    registro.append(gaveta.copy())

    for cadastrados in registro:
        for k, v in cadastrados.items():
            if k == 'Media das notas':
                print(end='\033[1;34m')
            print(end=f'{k}: ')
            print(v)
        print('-' * 20)


notas(6, 4, 3, 2, 8, 9, 7.8, 6.5, 3)  # Mude os valores a seguir

# Os códigos a seguir são apenas para mostrar que a função evita erros!
notas('x')
notas(32, 2, 145)
