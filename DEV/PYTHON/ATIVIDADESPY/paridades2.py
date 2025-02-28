def main():
    n = int(input("digite o numero: "))
    pares(n)

def pares(n):
    if n % 2 == 0:
        print("par")
    else:
        print("impar")

main()