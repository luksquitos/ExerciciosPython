# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('sacode', 'cabeça', 'jambo', 'lambisomem', 'pizza', 'ronaldinho')  # Tem que adicionar as palavras aí
cont = 0

print(f'{"ANALISADOR DE VOGAIS":=^40}')

while cont <= len(palavras) - 1:
    print(f'{palavras[cont]:=<20}', end='')

    for anali in palavras[cont]:
        if anali in 'aeiou':
            print(anali, end=',')
    print()
    cont += 1
print('\033[1;31mFim da execução do programa.')
