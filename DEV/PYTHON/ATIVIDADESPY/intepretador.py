def main():
    valores = input("digite os numeros como no exemplo (9 + 7) --> ").split()
    

    if calcular(valores[0], valores[1], valores[2]):
        print(end="")
    else:
        print("comando não encontrado")


def calcular(num1, operador, num2):
    num1 = int(num1)
    num2 = int(num2)
#indetifique o operador

    if operador == "-":
        print(num1 - num2)
        return True

    if operador == "+":
        print(num1 + num2)
        return True

    if operador == "/":
        print(num1 / num2)
        return True

    if operador == "*":
        print(num1 * num2)
        return True

    if operador == "**":
        print(num1 - num2)
        return True

    else:
        return False

main()