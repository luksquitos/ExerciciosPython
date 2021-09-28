#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome : ")).strip()   #Cortar os espaços que foram adicionados no começo e no fim por engano.
pnome = nome.split()

print("Maiúsculo ", nome.upper())
print("Minúsculo ", nome.lower())
print("Seu nome possui {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome é {} e tem {} letras" .format(pnome[0], len(pnome[0])))
