def main():
    tamanho = int(input("informe o tamanho da linha"))
    linha(tamanho)


def linha(tamanho):
    print("⬜" * tamanho, end="")

main()