
"""def contar_vogais(n1):
    vogal = ['a', 'e', 'i', 'o', 'u']
    letras = list(n1)
    if letras == vogal:
        print("não tem vogal")
    else:
        print("Tem vogal")


n1 = str(input("Digite a palavra: "))

contar_vogais(n1)"""

def colorir(texto, cor):
    cores = {
        "vermelho": "\033[31m",
        "amarelo": "\033[33m",
        "verde": "\033[32m",
        "laranja": "\033[93m",  # amarelo brilhante como laranja
        "preto": "\033[30m",
        "reset": "\033[0m"
    }
    return f"{cores.get(cor, cores['reset'])}{texto}{cores['reset']}"

lista_cores = [
    colorir("Vermelho", "vermelho"),
    colorir("Amarelo", "amarelo"),
    colorir("Verde", "verde"),
    colorir("Laranja", "laranja"),
    colorir("Preto", "preto"),
]

for item in lista_cores:
    print(item)
