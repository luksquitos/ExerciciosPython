# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

from math import pow

peso = float(input('Digite aqui seu peso (KG): '))
altura = float(input('Digite aqui sua altura(Metros): '))
IMC = (peso / pow(altura, 2))

print('\033[1;35mSeu Índice de Massa Córporea é: {:.1f}\033[m'.format(IMC))
print('')
if IMC < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC <= 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade Mórbida')
