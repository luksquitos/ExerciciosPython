# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C)
# Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoa = {}
pessoasCadastradas = []
resp = 'S'
quantPessoas = somaIdades = mulheres = 0

while resp == 'S':
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    somaIdades += pessoa['idade']
    pessoa['sexo'] = input('Sexo: [M/F]').upper()
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('M ou F?').upper()
    pessoasCadastradas.append(pessoa.copy())
    quantPessoas += 1
    resp = input('Gostaria de continuar ? [S/N] ').upper()
    while resp not in 'SN':
        resp = input('S ou N ?').upper()
mediaIdades = somaIdades / quantPessoas
idadeAcimaMedia = []
listaMulheres = []
for dicionario in pessoasCadastradas:
    if dicionario['sexo'] == 'F':
        listaMulheres.append(dicionario['nome'])
        mulheres += 1
    if dicionario['idade'] > mediaIdades:
        idadeAcimaMedia.append(dicionario['nome'])

print(f'O grupo tem {quantPessoas}')
print(f'A media de idades é {mediaIdades}')
print(f'As mulheres cadastradas foram {listaMulheres}')
print(f'As pessoas que estão com o peso acima da media são {idadeAcimaMedia}')





