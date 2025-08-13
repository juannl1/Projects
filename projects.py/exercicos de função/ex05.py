
"""def contar_vogais(n1):
    vogal = ['a', 'e', 'i', 'o', 'u']
    letras = list(n1)
    if letras == vogal:
        print("não tem vogal")
    else:
        print("Tem vogal")


n1 = str(input("Digite a palavra: "))

contar_vogais(n1)"""

import random
"""banco_de_notas = {
    #notas #qtd de notas
    2: [30, 5, 1, 12, 36, 60],
    5: [120, 4, 65, 10, 2, 32],
    10: [52, 30, 10, 2, 5, 2],
    20: [70, 12, 50, 600, 120, 600],
    50: [20, 500, 60, 40, 21, 45],
    100: [213, 201, 24, 30, 540, 45],
    200: [143, 12, 43, 63, 11, 23]
}

sorteador_notas_2 = random.choice(list(banco_de_notas.keys()))
sorteador_notas_5 = 
sorteador_notas_10 = 
sorteador_notas_20 = 
sorteador_notas_50 = 
sorteador_notas_100 = 
sorteador_notas_200 =  
print(f"Chave: {sorteador_notas_2}\nValor: {banco_de_notas[sorteador_notas_2]}")"""

banco_de_notas = {
    2: [30, 5, 1, 12, 36, 60],
    5: [120, 4, 65, 10, 2, 32],
    10: [52, 30, 10, 2, 5, 2],
    20: [70, 12, 50, 600, 120, 600],
    50: [20, 500, 60, 40, 21, 45],
    100: [213, 201, 24, 30, 540, 45],
    200: [143, 12, 43, 63, 11, 23]
}

# Para cada chave (nota), sorteia um valor da lista
for nota, quantidades in banco_de_notas.items():
    quantidade_sorteada = random.choice(quantidades)
    print(f"Nota: R${nota} - Quantidade sorteada: {quantidade_sorteada}")
