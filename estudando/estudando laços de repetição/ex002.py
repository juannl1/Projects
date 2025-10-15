"""
2. Tabuada Simples
Peça ao usuário para digitar um número inteiro. Em seguida, imprima a tabuada completa (do 1 ao 10) desse número.
"""

numero_escolhido = int(input("Digite um número: "))

for i in range(1, 10 + 1):
    multiplicacao = i * numero_escolhido
    print(f"{i} x {numero_escolhido} = {multiplicacao}")


