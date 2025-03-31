def main():
    tamanho = int(input("informe o tamanho da coluna"))
    coluna(tamanho)


def coluna(tamanho):
    print("[]\n" * tamanho, end="")

main()