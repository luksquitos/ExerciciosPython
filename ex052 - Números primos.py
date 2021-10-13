n = int(input('Digite um número: '))

tot = 0

for c in range(1, n + 1):

    if n % c == 0:
        print('\033[1;36m', end=' ')
        print(c, end=' ')   #Essa luinha mostra os valores que foram divididos por C.
        tot = tot + 1
    else:
        print('\033[1;31m', end=' ')
        print(c, end=' ')   #Essa linha mostra os valores que não foram divididos por C.

if tot == 2:
    print('\n\033[1;32mEsse número é primo')
else:
    print('\n\033[1;31mEsse número não é primo')

print(f'O número total de divisores é {tot}')

