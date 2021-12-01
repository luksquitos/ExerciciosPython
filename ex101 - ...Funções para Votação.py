# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import datetime


def voto(age):
    if age >= 65:
        return 'op'
    elif 65 > age >= 17:
        return True
    elif age < 17:
        return False


idade = datetime.now().year - int(input('Ano de nascimento: '))
print(f'A função retorna {voto(idade)}')

if voto(idade) == 'op':
    print('\033[1;33mVoto Opcional')
if voto(idade) == True:
#if voto(idade):  Dessa forma o código não funciona e independente da idade, esse if será executado
    print('\033[1;31mVoto Obrigatório')
if not voto(idade):
    print('\033[1;32mSem idade para votar')
