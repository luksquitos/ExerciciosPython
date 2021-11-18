# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

registro = {}
anoAtual = datetime.today().year


registro['nome'] = input('Nome: ')
registro['idade'] = anoAtual - int(input('Data de nascimento: '))
registro['CTPS'] = int(input('Carteira de trabalho: (0)Não tem'))
if registro['CTPS'] != 0:
    registro['anoContratado'] = int(input('Ano de contratação'))
    registro['Salario'] = float(input('Salário : R$'))
    registro['aposentadoria'] = (35 - (anoAtual - registro['anoContratado'])) + registro['idade']

for k, v in registro.items():
    print(f'{k}, {v}')


