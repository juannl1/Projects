
from time import sleep
from math import factorial, sqrt
from os import system
import colorama

init() #inicilizar colorama


#limpar terminal

def limpar_terminal():
    system("cls")

#Criando uma opção de "Restart"
def entrada(mensagem):
    resposta = input(mensagem).strip().lower()

    if resposta == "restart":
        print("\n🔄 Reiniciando programa...\n")
        sleep(1)
        for contador in range(5, 0, -1): #contagem regressiva
            print(contador)
            sleep(0.3)
        rodar_programa_principal()
        exit()

    return resposta


#Funções matemáticas


def tabuada(numero_tabuado, quantos_numeros):
    for i in range(1, quantos_numeros + 1):
        total = numero_tabuado * i
        print(f"{numero_tabuado} x {i} = {total}")
        sleep(0.01)

def fatorial(n1):
    for i in range(1, n1):
            i += 1
            print(f"{i}! = {factorial(i)}")
            sleep(0.01)

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
    total = sqrt(n1)

    # pega parte decimal se existir
    parte_decimal = str(total).split(".")[1] if "." in str(total) else ""
    if len(parte_decimal) > 2:
        print(f"Total: {total}\nRaiz não exata\n")
    else:
        print(f"Total: {total}\nRaiz exata\n")



def porcentagem():
    while True:
            try:
                decisao_porcentagem = int(entrada(" 1. Taxa adicional\n 2. Desconto\n\n#Responda com números: "))

                if decisao_porcentagem in [1, 2]:
                    break

                else:
                    print("ERRO.\nInsira um número inteiro.\n\n")
                    sleep(1)
                    print("Tente novamente...")
                    sleep(2)

            except ValueError:
                print("Resposta Inválida.\n")
                sleep(2)


    if decisao_porcentagem == 1:

        print("\n\n", 28*'='," Taxa adicional ",28*'=', "\n\n")

        while True:
            try:
                valor_taxa_adicional = int(entrada("Digite o valor do produto: "))
                porcentagem_taxa_adicional = int(entrada("% De taxa adicional: "))
                
                taxa_adicional = (porcentagem_taxa_adicional / 100) * valor_taxa_adicional
                total_taxa_adicinal = taxa_adicional + valor_taxa_adicional

                sleep(1)
                print(f"\nTaxa Adicional: R${taxa_adicional}\nTotal a pagar: R${total_taxa_adicinal}")

                sleep(1.5)

                decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                
                if decisão_de_saida == 1:
                    print("Obrigado!")
                    exit()
                    break
                    
                else:
                    print("Ok, Vamos continuar")
                    sleep(0.7)
                    rodar_programa_principal()
                    

            except ValueError:
                print("Resposta Inválida.\n")
                sleep(2)

    elif decisao_porcentagem == 2:

        print("\n\n", 28*'='," Desconto ",28*'=', "\n\n")
        while True:
            try:
                valor_desconto = int(entrada("Digite o valor do produto: "))
                porcentagem_desconto = int(entrada("% De desconto: "))

                desconto = (porcentagem_desconto / 100) * valor_desconto
                total_desconto = valor_desconto - desconto

                print(f"Desconto: R${desconto}\nTotal a pagar: R${total_desconto}")
                print("\nDigite (restart) para reniciar o programa...")
            
                break

            except ValueError:
                print("Resposta Inválida.\n")



#Programa principal #Rodar_programa_principal()
def rodar_programa_principal():

    limpar_terminal()
    print(28*'=',"Calculadora Interativa",27*'=')
    sleep(1)

    #Perguntando ao usuário qual operação ele vai utilizar


    while True:
        try:
            lista_opcoes = [" Tabuada", " Fatorial(Tabuada)", " Cálculo Específico"]

            for indice, opcoes in enumerate(lista_opcoes, start=1):
                print(f"{indice}. {opcoes}")
                sleep(0.1)

            print("\nSe for preciso reniciar o programa escreva (restart) em qualquer caixa de texto\n")

            sleep(1)

            decisao = int(entrada("\n#Responda com números: "))
            
            break

        except ValueError:
            print("Resposta Inválida.\n")
            sleep(2)


    #Usuário escolheu tabuada...
    if decisao == 1:
        
        #Rodando Tabuada
        print("\n\n", 28*'='," Tabuada ",27*'=', "\n\n")
        
        while True:
            try:
                numero_tabuado = int(entrada("Qual número você deseja tabuar: "))
                quantos_numeros = int(entrada("Até qual número: "))
                tabuada(numero_tabuado, quantos_numeros)
                
                sleep(1.5)

                decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                
                if decisão_de_saida == 1:
                    print("Obrigado!")
                    exit()
                    break
                    
                else:
                    print("Ok, Vamos continuar")
                    sleep(0.7)
                    rodar_programa_principal()

            except ValueError:
                print("Resposta Inválida.\n")
                sleep(2)

    #Usuário escolheu Fatorial... 
    elif decisao == 2:

        #Rodando Fatorial(tabuada)
        print("\n\n", 28*'='," Fatorial ",27*'=', "\n\n")

        while True:
            try:
                numero_fatorial = int(entrada("Digite o número que deseja: "))
                fatorial(numero_fatorial)
                
                sleep(1.5)

                decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                
                if decisão_de_saida == 1:
                    print("Obrigado!")
                    exit()
                    break
                    
                else:
                    print("Ok, Vamos continuar")
                    sleep(0.7)
                    rodar_programa_principal()

            except ValueError:
                print("Resposta Inválida.\n")
        
    #Usuário escolheu Cálculo específico...
    elif decisao == 3:

        #Rodando Cálculo Específico
        print("\n\n", 28*'=', " Cálculo Específico ",27*'=', "\n\n")

        #Perguntando ao usuário qual operador matemático
        while True:
            try:
                operadores_matematicos = ["Adição", "Subtração", "Multiplicação", "Divisão", "Módulo (Resto da divisão", "Potênciação", "Raiz Quadrada", "Porcentagem (Calcular Desconto ou taxa adicional)"]

                for indice, operadores in enumerate(operadores_matematicos, start=1):
                    print(f"{indice}. {operadores}")
                    sleep(0.1)

                decisao_operador_matemático = int(entrada("\n#Responda com números: "))
                
                break

            except ValueError:
                print("Resposta Inválida.\n")
                sleep(2)
        
        if decisao_operador_matemático == 1:

            #Rodando adição
            print("\n\n", 28*'='," Adição ",27*'=', "\n\n")

            while True:
                try:
                    adiçao_n1 = int(entrada("1° Número: "))
                    adiçao_n2 = int(entrada("2° Numero: "))

                    adicao(adiçao_n1, adiçao_n2)

                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        print("Obrigado!")
                        exit()
                        break
                        
                    else:
                        print("Ok, Vamos continuar")
                        sleep(0.7)
                        rodar_programa_principal()

                except ValueError:
                    print("Resposta Inválida.\n")
                    sleep(2)
                    

        elif decisao_operador_matemático == 3:

            #Rodando Subtração
            print("\n\n", 28*'='," Subtração ",27*'=', "\n\n")

            while True:
                try:
                    subtração_n1 = int(entrada("1° Número: "))
                    subtração_n2 = int(entrada("2° Numero: "))

                    subtração(subtração_n1, subtração_n2)

                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        print("Obrigado!")
                        exit()
                        break
                        
                    else:
                        print("Ok, Vamos continuar")
                        sleep(0.7)
                        rodar_programa_principal()

                except ValueError:
                    print("Resposta Inválida.\n")
                    sleep(2)


        elif decisao_operador_matemático == 3:

            #Rodando Multiplicação
            print("\n\n", 28*'='," Multiplicação ",27*'=', "\n\n")
            while True:
                try:
                    multiplicacao_n1 = int(entrada("1° Número: "))
                    multiplicacao_n2 = int(entrada("2° Numero: "))

                    multiplicacao(multiplicacao_n1, multiplicacao_n2)
                    
                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        print("Obrigado!")
                        exit()
                        break
                        
                    else:
                        print("Ok, Vamos continuar")
                        sleep(0.7)
                        rodar_programa_principal()

                except ValueError:
                    print("Resposta Inválida.\n")
                    sleep(2)

        elif decisao_operador_matemático == 4:

            #Rodando Divisão
            print("\n\n", 28*'='," Divisão ",27*'=', "\n\n")

            while True:
                try:
                    divisao_n1 = float(entrada("Valor a ser repartido: "))
                    divisao_n2 = float(entrada("Quantas vezes a ser repartido: "))

                    divisao(divisao_n1, divisao_n2)
                    
                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        print("Obrigado!")
                        exit()
                        break
                        
                    else:
                        print("Ok, Vamos continuar")
                        sleep(0.7)
                        rodar_programa_principal()

                except ValueError:
                    print("Resposta Inválida.\n")
                    sleep(2)

        elif decisao_operador_matemático == 5:

            #Rodando Módulo
            print("\n\n", 28*'='," Módulo ",27*'=', "\n\n")
            
            while True:
                try:
                    modulo_n1 = float(entrada("Valor a ser repartido: "))
                    modulo_n2 = float(entrada("Quantas vezes a ser repartido: "))

                    modulo(modulo_n1, modulo_n2)
                    
                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        print("Obrigado!")
                        exit()
                        break
                        
                    else:
                        print("Ok, Vamos continuar")
                        sleep(0.7)
                        rodar_programa_principal()

                except ValueError:
                    print("Resposta Inválida.\n")
                    sleep(2)

        elif decisao_operador_matemático == 6:

            #Rodando Potenciação
            print("\n\n", 28*'='," Potenciação ",27*'=', "\n\n")

            while True:
                try:
                    base = int(entrada("Base: "))
                    expoente = int(entrada("Expoente: "))

                    potenciacao(base, expoente)

                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        print("Obrigado!")
                        exit()
                        break
                        
                    else:
                        print("Ok, Vamos continuar")
                        sleep(0.7)
                        rodar_programa_principal()

                except ValueError:
                    print("Resposta Inválida.\n")
                    sleep(2)
                    
                

        elif decisao_operador_matemático == 7:

            #Rodando Raiz Quadrada (sqrt)
            print("\n\n", 28*'='," Raiz Quadrada ",27*'=', "\n\n")
            while True:
                try:
                    raiz = int(entrada("Raiz: "))

                    raiz_quadrada(raiz)

                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Finalizar programa\n2. Continuar\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        print("Obrigado!")
                        exit()
                        break
                        
                    else:
                        print("Ok, Vamos continuar")
                        sleep(0.7)
                        
                        rodar_programa_principal()

                except ValueError:
                    print("Resposta Inválida.\n")
                    sleep(2)

        elif decisao_operador_matemático == 8:

            #Rodando Porcentagem
            print("\n\n", 28*'='," Porcentagem ",27*'=', "\n\n")
            porcentagem()

rodar_programa_principal()