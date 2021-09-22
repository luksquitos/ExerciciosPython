n = input("Digite algo ")

print("O tipo {}".format(n), type(n))
print(type(n))
print("O tipo de {} é".format(n), type(n))
print("É numérico", n.isnumeric())
print("É minúsculo", n.islower())
print("É maiúsculo", n.isupper())
print("É alfabético?", n.isalpha())
print("É alfanumérico?", n.isalnum())


