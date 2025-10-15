"""
3. Soma Interativa
Crie um programa que continue pedindo números ao usuário. O programa deve somar todos os números digitados e só deve parar quando o usuário digitar a palavra "fim". Ao final, imprima a soma total.
"""


lista_de_numeros = []
while True:

    n1 = input("Digite o numero para somar: ").lower().strip()

    if n1 == str('sair'):
        print("Finalizando")
        break

    else:
        lista_de_numeros.append(int(n1))


soma = sum(lista_de_numeros)

print(soma)
