# Lista de cadastros genérica.

cont = input('Quantas pessoas gostaria de cadastrar? ')
while not cont.isnumeric():
    cont = input('Digite um número válido')
cont = int(cont) - 1

dados = []
pessoas = []

while cont >= 0:
    dados.append(input('Digite aqui seu nome: '))
    dados.append(input('Digite aqui sua idade: '))
    pessoas.append(dados[:])
    del(dados[:])
    print('--X--')
    cont -= 1
for c in pessoas:
    print(c[0])