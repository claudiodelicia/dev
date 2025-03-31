def main():
    miar(pegar_numero())

def miar(miaus):
    print("miau\n" * miaus, end="")

def pegar_numero():
    while True:
         miaus = int(input("quantas vezes seu gato mia ?"))

         if miaus > 0:
             break


    return miaus

main()
