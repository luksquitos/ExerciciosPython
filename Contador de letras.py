from pprint import pprint

dic = dict()

frase = 'juliano foi no farol vender paçoca estragada'

for letra in frase:
    dic.setdefault(letra, 0)
    dic[letra] += 1
    
pprint(dic)