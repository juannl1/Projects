print("Verificando números multiplos\n")

n1 = int(input("Número que deseja verificar: "))
numero_para_divisao = int(input("Digite o numero divisor: "))

multiplo = n1 % numero_para_divisao #modulo, Saber o resto da divisao

#verificando se é multiplo
if multiplo == 0:
    print("É multiplo")
else:
    print("Não é multiplo")



if numero_para_divisao > 0:
    print("O número é positivo")
elif numero_para_divisao < 0:
    print("O número é negativo")
else:
    print("O número é 0")