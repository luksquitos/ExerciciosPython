#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite aqui sua frase ')).lower().strip()


print('Essa frase tem {} letras A'.format(frase.count('a')))
print('A primeira vez que ela aparece é {}' .format(frase.find('a')))
print('A ultima vez que ele aparece é {}'.format(frase.rfind('a')))

# O 'frase.find()', começa ler a variável da esquerda pra direita pra achar o que foi pedido
# O 'frase.rfind()', começa a ler a variavel da direita pra esquerda pra achar o que foi pedido.
