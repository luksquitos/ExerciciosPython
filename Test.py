def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 da base {origem} para a base {destino}")
        return ';'
    hanoi(n-1, origem, auxiliar, destino)
    print(f'Mova o disco{n} da base {origem} para a base {destino}')
    hanoi(n-1, auxiliar, destino, origem)


n = int(input("Num de discos"))
hanoi(n, 'A', 'B', 'C')
