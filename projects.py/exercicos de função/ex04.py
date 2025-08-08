def contar(a, b):
    for x in range(a, b + 1):
        print(x)
        for x in range(a, b + 1):
            print(x)



a = int(input("Digite o valor: "))
b = int(input("Digite o valor: "))
contar(a, b)