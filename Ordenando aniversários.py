# Alinhando aniversários usando lambda
# Código com erro!!!

aniversários = [{'nome': 'José', 'dia': '11/04'}, {'nome': 'Juliana', 'dia': '16/01'},
                {'nome': 'marcos', 'dia': '01/01'},
                {'nome': 'maria', 'dia': '17/12'}, {'nome': 'Julius', 'dia': '05/08'}]

aniversários.sort(key=lambda data: data['dia'])

print('A ordem correta foi: ')
for dicio in aniversários:
    print()
    for valores in dicio.values():
        print(end=f'{valores} ')
