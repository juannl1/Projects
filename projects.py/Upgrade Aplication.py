import time, math, os




#limpar terminal

def limpar_terminal():
    os.system("cls")

#Funções matemáticas


def tabuada(numero_tabuado, quantos_numeros):
    for i in range(1, quantos_numeros + 1):
        total = numero_tabuado * i
        print(f"{numero_tabuado} x {i} = {total}")
        time.sleep(0.01)

def fatorial(n1):
    for i in range(1, n1):
            i += 1
            print(f"{i}! = {math.factorial(i)}")
            time.sleep(0.01)

#Calculos específicos
def adicao(n1, n2):
    total = n1 + n2
    print(f"Total: {total}")

def subtração(n1, n2):
    total = n1 - n2
    print(f"Total: {total}")

def multiplicacao(n1, n2):
    total = n1 * n2
    print(f"Total: {total}")

def divisao(n1, n2):
    total = n1 / n2
    print(f"Total: {total:.2f}")

def modulo(n1, n2):
    total = n1 % n2
    print(f"O resto da divisão {n1} / {n2} = {total}")

def potenciacao(n1, n2):
    total = n1 ** n2
    print(f"Total: {total}")
    
def raiz_quadrada(n1):
    total = math.sqrt(n1)

    # pega parte decimal se existir
    parte_decimal = str(total).split(".")[1] if "." in str(total) else ""
    if len(parte_decimal) > 2:
        print(f"Total: {total}\nRaiz não exata\n")
    else:
        print(f"Total: {total}\nRaiz exata\n")

def porcentagem():
    while True:
            try:
                decisao_porcentagem = int(input(" 1. Taxa adicional\n 2. Desconto\n\n#Responda com números: "))

                if decisao_porcentagem in [1, 2]:
                    break

            except ValueError:
                print("Algo deu errado\nInsira algo válido...")


    if decisao_porcentagem == 1:
        print("\n\n", 20*'='," Taxa adicional ",20*'=', "\n\n")

        valor_taxa_adicional = int(input("Digite o valor do produto: "))
        porcentagem_taxa_adicional = int(input("% De taxa adicional: "))
        
        taxa_adicional = (porcentagem_taxa_adicional / 100) * valor_taxa_adicional
        total_taxa_adicinal = taxa_adicional + valor_taxa_adicional

        
        print(f"Taxa Adicional: R${taxa_adicional}\nTotal a pagar: R${total_taxa_adicinal}")

    elif decisao_porcentagem== 2:
        print("\n\n", 20*'='," Desconto ",20*'=', "\n\n")

        valor_desconto = int(input("Digite o valor do produto: "))
        porcentagem_desconto = int(input("% De desconto: "))

        desconto = (porcentagem_desconto / 100) * valor_desconto
        total_desconto = valor_desconto - desconto

        print(f"Desconto: R${desconto}\nTotal a pagar: R${total_desconto}")







#Programa principal

limpar_terminal()

print(20*'=',"Calculadora Interativa",20*'=')

#Perguntando ao usuário
while True:
    try:
        decisao = int(input("1. Tabuada\n2. Cálculo específico\n3. Fatorial(Tabuada)\n\n#Responda com números: "))

        if decisao in [1, 2]:
            break

        else:
            print("Tente novamente...\n(1/2)")
            time.sleep(2)

    except ValueError:
        print("Tente novamente...\n(1/2)")
        time.sleep(2)


#Usuário escolheu tabuada...
if decisao == 1:
    
    #Rodando Tabuada
    print("\n\n", 20*'='," Tabuada ",20*'=', "\n\n")

    numero_tabuado = int(input("Qual número você deseja tabuar: "))
    quantos_numeros = int(input("Até qual número: "))
    tabuada(numero_tabuado, quantos_numeros)


#Usuário escolheu Cálculo específico
elif decisao == 2:

    #Rodando Cálculo Específico
    print("\n\n", 20*'=', " Cálculo Específico ",20*'=', "\n\n")

    #Perguntando ao usuário 
    while True:
        try:
            decisao_calculo_especifico = int(input("\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Módulo (Resto da divisão)\n6. Potênciação\n7. Raiz Quadrada\n8. Porcentagem (Calcular Desconto ou taxa adicional)\n\n#Responda com números: "))
            
            if decisao_calculo_especifico in [1, 2, 3, 4, 5, 6, 7, 8]:
                break
            else:
                print("\nTente novamente...")
                time.sleep(2)
        except ValueError:
            print("\nTente novamente...")
            time.sleep(2)
    
    if decisao_calculo_especifico == 1:

        #Rodando adição
        print("\n\n", 20*'='," Adição ",20*'=', "\n\n")

        adiçao_n1 = int(input("1° Número: "))
        adiçao_n2 = int(input("2° Numero: "))

        adicao(adiçao_n1, adiçao_n2)

    elif decisao_calculo_especifico == 2:

        #Rodando adição
        print("\n\n", 20*'='," Subtração ",20*'=', "\n\n")

        subtração_n1 = int(input("1° Número: "))
        subtração_n2 = int(input("2° Numero: "))

        subtração(subtração_n1, subtração_n2)

    elif decisao_calculo_especifico == 3:

        #Rodando Multiplicação
        print("\n\n", 20*'='," Multiplicação ",20*'=', "\n\n")

        multiplicacao_n1 = int(input("1° Número: "))
        multiplicacao_n2 = int(input("2° Numero: "))

        multiplicacao(multiplicacao_n1, multiplicacao_n2)

    elif decisao_calculo_especifico == 4:

        #Rodando Divisão
        print("\n\n", 20*'='," Divisão ",20*'=', "\n\n")

        divisao_n1 = float(input("Valor a ser repartido: "))
        divisao_n2 = float(input("Quantas vezes a ser repartido: "))

        divisao(divisao_n1, divisao_n2)

    elif decisao_calculo_especifico == 5:

        #Rodando Módulo
        print("\n\n", 20*'='," Módulo ",20*'=', "\n\n")

        modulo_n1 = int(input("Valor a ser repartido: "))
        modulo_n2 = int(input("Quantas vezes a ser repartido: "))

        modulo(modulo_n1, modulo_n2)

    elif decisao_calculo_especifico == 6:

        #Rodando Potenciação
        print("\n\n", 20*'='," Potenciação ",20*'=', "\n\n")

        base = int(input("Base: "))
        expoente = int(input("Expoente: "))

        potenciacao(base, expoente)

    elif decisao_calculo_especifico == 7:

        #Rodando Raiz Quadrada (math.sqrt)
        print("\n\n", 20*'='," Raiz Quadrada ",20*'=', "\n\n")

        raiz = int(input("Raiz: "))

        raiz_quadrada(raiz)

    elif decisao_calculo_especifico == 8:

        #Rodando Porcentagem (math.sqrt)
        print("\n\n", 20*'='," Porcentagem ",20*'=', "\n\n")

        porcentagem()

    