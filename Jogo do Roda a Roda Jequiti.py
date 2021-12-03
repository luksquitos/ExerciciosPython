print('''\033[1;36mVAMOS BRINCAR DE RODA A RODA JEQUITI!!
Uma palavra foi escolhida e você pode errar 4 vezes
BOA SORTE!!\033[m''')

secreto = input('Escreva a palavra secreta: ')
dica = input('Escreva aqui a dica: ')
print(f'A palavra escolhida tem {"*"*len(secreto)}')
print(f'A dica é {dica}')
chances = 4
letra_correta = []

while chances > 0:
    escolha = input('Qual letra você escolhe ?\n- ').lower()
    if len(escolha) > 1:
        print('Boa tentativa, mas você deve escrever apenas uma letra!')
        continue
    if escolha in secreto:
        print('\033[1;36mVocê acertou, continue!!\033[m')
        letra_correta.append(escolha)
    else:
        print('\033[1;31mVocê errou!')
        chances -= 1
        print(f'Lhe restam {chances} chances\033[m')

    print()
    mostrado = ''
    for anal in secreto:
        if anal in letra_correta:
            mostrado += anal
        else:
            mostrado += '_'
    print(f'\033[1;33mSeu progresso:\n{mostrado}\033[m')

    if mostrado == secreto:
        print(f'\033[1;32m=======Você venceu!!=======\033[m')
        break
    elif chances == 0:
        print('\033[1;31m=======Você perdeu!!=======\033[m')
        break
