#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

city = str(input('Digite aqui o nome da cidade ')).strip().lower()

print(city[:5] == 'santo')