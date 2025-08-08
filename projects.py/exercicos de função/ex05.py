
def contar_vogais(n1):
    vogal = ['a', 'e', 'i', 'o', 'u']
    letras = list(n1)
    if letras == vogal:
        print("não tem vogal")
    else:
        print("Tem vogal")


n1 = str(input("Digite a palavra: "))

contar_vogais(n1)