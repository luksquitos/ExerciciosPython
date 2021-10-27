#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo da P.A:\n- '))
razao = int(input('Digite a razão:\n- '))
cont = 10
soma = primeiro
termos = 0

while cont != 0:
    while cont != 0:
        print(soma, end=', ')
        soma += razao
        cont -= 1
        termos += 1
    print()
    pergunta = int(input('Gostaria de adicionar mais valores ?'))
    cont = pergunta
print(f'Você viu {termos} termos.')
