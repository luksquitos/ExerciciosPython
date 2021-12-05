# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.


def ajuda(x):
    help(x)


def cor(x):
    cores = ('\033[m',
             '\033[7;40m'  # Branco
             '\033[41m')  # Vermelho
    print(cores[x])


print(f'{"Interactive HELP":}')
while True:
    pergunta = input('Função ou Biblioteca:\n- ')
    cor(1)
    ajuda(pergunta)
    cor(0)
