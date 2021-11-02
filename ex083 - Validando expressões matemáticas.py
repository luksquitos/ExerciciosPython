# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite aqui uma expressão matemática: '))

esquerdo = 0
direito = 0

for letra in expressao:
    if letra == '(':
        esquerdo += 1
    elif letra == ')':
        direito += 1

if esquerdo == direito and expressao[0] == '(' and expressao[-1] == ')':
    print('A expressão é válida')
else:
    print('A expressão não é válida')