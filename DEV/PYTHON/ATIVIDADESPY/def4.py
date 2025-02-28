def main():
    nome =input("Qual seu nome?")
    diga_ola(nome)

def diga_ola(para="mundo"):
    print(f"Olá, {para}!")

main()