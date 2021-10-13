#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ').lower().replace(' ', ''))
comprimento = len(frase)
t = 0
letras_iguais = 0
#print(comprimento)

for c in range(comprimento - 1, -1, -1):
    if frase[c] == frase[t]:
        letras_iguais = letras_iguais + 1
        #print(frase[c], end='')
        #print(frase[t], end='')
        t = t + 1
if letras_iguais == comprimento:
    print('\033[1;32mEssa frase é palíndroma.')
else:
    print('\033[1;31mEssa frase não é palíndroma.')
#print(f'O número de letras iguais foram: {letras_iguais}')
