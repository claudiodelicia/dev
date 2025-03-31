def main():
    resposta = input("Voce concorda ?").lower()
    concordo(resposta)


def concordo(resposta):
    if resposta == "sim " or resposta == "s":
        print(" Eu concordo")
    elif resposta == "nao" or resposta == "N" or resposta == "n":
        print("nao concordo")

main()