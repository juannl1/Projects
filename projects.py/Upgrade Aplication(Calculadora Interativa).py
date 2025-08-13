from time import sleep
from math import factorial, sqrt
from os import system



# limpar terminal
def limpar_terminal():
    system("cls")

# Criando uma opção de "Restart"
def entrada(mensagem):
    resposta = input(mensagem).strip().lower()

    if resposta == "restart":
        sleep(1)
        for contador in range(3, 0, -1): # contagem regressiva
            print(f"\r🔄 Reiniciando programa...{contador}", end="")
            sleep(0.8)
        rodar_programa_principal()
        exit()

    return resposta

# Criando opção de começar de novo o programa
def rodar_decisao_de_saida():
        print("Ok, vamos continuar 🤓 ☝.")
        sleep(1.7)
        rodar_programa_principal()
        exit()

# Funções matemáticas
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

# Calculos específicos
def adicao(n1, n2):
    total = n1 + n2
    print(f"Total: {total}")

def subtração(n1, n2):
    total = n1 - n2
    print(f"Total: {total:.2f}".replace(".", ","))

def multiplicacao(n1, n2):
    total = n1 * n2
    print(f"Total: {total:.2f}".replace(".", ","))

def divisao(n1, n2):
    total = n1 / n2
    print(f"Total: {total:.2f}".replace(".", ","))

def modulo(n1, n2):
    total = n1 % n2
    print(f"O resto da divisão {n1} / {n2} = {total:.2f}".replace(".", ","))

def potenciacao(n1, n2):
    total = n1 ** n2
    print(f"Total: {total}")
    
def raiz_quadrada(n1):
    total = sqrt(n1)

    # pega parte decimal se existir
    parte_decimal = str(total).split(".")[1] if "." in str(total) else ""
    if len(parte_decimal) > 2:
        print(f"\nParabéns! operação realizada com êxito ✅.\nTotal: {total:.2f}\nRaiz não exata\n".replace(".", ","))
    else:
        print(f"Total: {total:.2f}\nRaiz exata\n".replace(".", ","))

def porcentagem():
    while True:
            try:
                decisao_porcentagem = int(entrada(" 1. Taxa adicional\n 2. Desconto\n\n#Responda com números: "))

                if decisao_porcentagem in [1, 2]:
                    break

                else:
                    print("⚠️ Aviso: valor fora do intervalo permitido.\n\n")
                    sleep(1)
                    print("Tente novamente...")
                    sleep(2)

            except ValueError:
                print("❌ Erro: insira um número válido.\n")
                sleep(2)


    if decisao_porcentagem == 1:

        print("\n\n", 28*'='," Taxa adicional ",28*'=', "\n\n")

        while True:
            try:
                valor_taxa_adicional = float(entrada("Digite o valor do produto: "))
                porcentagem_taxa_adicional = int(entrada("% de taxa adicional: "))
                
                taxa_adicional = (porcentagem_taxa_adicional / 100) * valor_taxa_adicional
                total_taxa_adicional = taxa_adicional + valor_taxa_adicional

                sleep(1)
                print(f"\nParabéns! operação realizada com êxito.\n\nTaxa adicional: R${taxa_adicional:.2f}\nTotal a pagar: R${total_taxa_adicional:.2f}".replace(".", ","))

                sleep(1.5)

                decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                
                if decisão_de_saida == 1:
                    rodar_decisao_de_saida()
                    exit()

                else:
                    print("🛑 Interrupção: saindo do programa.")
                    exit()
                    break
                    

            except ValueError:
                print("❌ Erro: insira um número válido.\n")
                sleep(2)

    elif decisao_porcentagem == 2:

        print("\n\n", 28*'='," Desconto ",28*'=', "\n\n")
        while True:
            try:
                valor_desconto = float(entrada("Digite o valor do produto: "))
                porcentagem_desconto = int(entrada("% de desconto: "))

                desconto = (porcentagem_desconto / 100) * valor_desconto
                total_desconto = valor_desconto - desconto

                print(f"\nParabéns! operação realizada com êxito.\nDesconto: R${desconto:.2f}\nTotal a pagar: R${total_desconto:.2f}".replace(".", ","))
                print("\nDigite (restart) para reiniciar o programa...")
            
                decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                
                if decisão_de_saida == 1:
                    rodar_decisao_de_saida()
                    exit()

                else:
                    print("🛑 Interrupção: saindo do programa.")
                    exit()
                    break

            except ValueError:
                print("❌ Erro: insira um número válido.\n")



# Programa principal # Rodar_programa_principal()
def rodar_programa_principal():

    limpar_terminal()
    print(28*'=',"Calculadora Interativa",27*'=')
    sleep(1)

    # Perguntando ao usuário qual operação ele vai utilizar


    while True:
        try:
            lista_opcoes = [" Tabuada", " Fatorial(Tabuada)", " Cálculo específico"]

            for indice, opcoes in enumerate(lista_opcoes, start=1):
                print(f"{indice}. {opcoes}")
                sleep(0.1)

            print("\n💡 Dica: use 'restart' para reiniciar o programa em qualquer entrada.\n")

            sleep(1)

            decisao = int(entrada("\n#Responda com números: "))

            if decisao in [1, 2, 3]:
                break

            else:
                print("❌ Erro: insira algumas das opções (1,2,3)")
                sleep(2)

        except ValueError:
            print("❌ Erro: insira um número válido.\n")
            sleep(2)


    # Usuário escolheu tabuada...
    if decisao == 1:
        
        # Rodando tabuada
        print("\n\n", 28*'='," Tabuada ", 27*'=', "\n\n")
        
        while True:
            try:
                numero_tabuado = int(entrada("Qual número você deseja tabuar: "))
                quantos_numeros = int(entrada("Até qual número: "))
                tabuada(numero_tabuado, quantos_numeros)
                
                sleep(1.5)

                decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                
                if decisão_de_saida == 1:
                    rodar_decisao_de_saida()
                    exit()

                else:
                    print("🛑 Interrupção: saindo do programa.")
                    exit()
                    break

            except ValueError:
                print("❌ Erro: insira um número válido.\n")
                sleep(2)

    # Usuário escolheu fatorial... 
    elif decisao == 2:

        # Rodando fatorial(tabuada)
        print("\n\n", 28*'='," Fatorial ", 27*'=', "\n\n")

        while True:
            try:
                numero_fatorial = int(entrada("Digite o número que deseja: "))
                fatorial(numero_fatorial)
                
                sleep(1.5)

                decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                
                if decisão_de_saida == 1:
                    rodar_decisao_de_saida()
                    exit()

                else:
                    print("🛑 Interrupção: saindo do programa.")
                    exit()
                    break

            except ValueError:
                print("❌ Erro: insira um número válido.\n")
        
    # Usuário escolheu cálculo específico...
    elif decisao == 3:

        # Rodando cálculo específico
        print("\n\n", 28*'='," Cálculo Específico ", 27*'=', "\n\n")

        # Perguntando ao usuário qual operador matemático
        while True:
            try:
                operadores_matematicos = ["Adição", "Subtração", "Multiplicação", "Divisão", "Módulo (Resto da divisão)", "Potênciação", "Raiz Quadrada", "Porcentagem (Calcular desconto ou taxa adicional)"]

                for indice, operadores in enumerate(operadores_matematicos, start=1):
                    print(f"{indice}. {operadores}")
                    sleep(0.1)

                decisao_operador_matemático = int(entrada("\n#Responda com números: "))
                
                break

            except ValueError:
                print("❌ Erro: operador inválido.")
                sleep(2)
        
        if decisao_operador_matemático == 1:

            # Rodando adição
            print("\n\n", 28*'='," Adição ", 27*'=', "\n\n")

            while True:
                try:
                    adiçao_n1 = int(entrada("1° número: "))
                    adiçao_n2 = int(entrada("2° número: "))

                    adicao(adiçao_n1, adiçao_n2)

                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                
                    if decisão_de_saida == 1:
                        rodar_decisao_de_saida()
                        exit()

                    else:
                        print("🛑 Interrupção: saindo do programa.")
                        exit()
                        break
                except ValueError:
                    print("❌ Erro: insira um número válido.\n")
                    sleep(2)
                    

        elif decisao_operador_matemático == 2:

            # Rodando subtração
            print("\n\n", 28*'='," Subtração ", 27*'=', "\n\n")

            while True:
                try:
                    subtração_n1 = int(entrada("1° número: "))
                    subtração_n2 = int(entrada("2° número: "))

                    subtração(subtração_n1, subtração_n2)

                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                
                    if decisão_de_saida == 1:
                        rodar_decisao_de_saida()
                        exit()

                    else:
                        print("🛑 Interrupção: saindo do programa.")
                        exit()
                        break

                except ValueError:
                    print("❌ Erro: insira um número válido.\n")
                    sleep(2)


        elif decisao_operador_matemático == 3:

            # Rodando multiplicação
            print("\n\n", 28*'='," Multiplicação ", 27*'=', "\n\n")
            while True:
                try:
                    multiplicacao_n1 = int(entrada("1° número: "))
                    multiplicacao_n2 = int(entrada("2° número: "))

                    multiplicacao(multiplicacao_n1, multiplicacao_n2)
                    
                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                
                    if decisão_de_saida == 1:
                        rodar_decisao_de_saida()
                        exit()

                    else:
                        print("🛑 Interrupção: saindo do programa.")
                        exit()
                        break

                except ValueError:
                    print("❌ Erro: insira um número válido.\n")
                    sleep(2)

        elif decisao_operador_matemático == 4:

            # Rodando divisão
            print("\n\n", 28*'='," Divisão ", 27*'=', "\n\n")

            while True:
                try:
                    divisao_n1 = float(entrada("Valor a ser repartido: "))
                    divisao_n2 = float(entrada("Quantas vezes a ser repartido: "))

                    divisao(divisao_n1, divisao_n2)
                    
                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                    if decisão_de_saida == 1:
                        rodar_decisao_de_saida()
                        exit()

                    else:
                        print("🛑 Interrupção: saindo do programa.")
                        exit()
                        break

                except ValueError:
                    print("❌ Erro: insira um número válido.\n")
                    sleep(2)

        elif decisao_operador_matemático == 5:

            # Rodando módulo
            print("\n\n", 28*'='," Módulo ", 27*'=', "\n\n")
            
            while True:
                try:
                    modulo_n1 = float(entrada("Valor a ser repartido: "))
                    modulo_n2 = float(entrada("Quantas vezes a ser repartido: "))

                    modulo(modulo_n1, modulo_n2)
                    
                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        rodar_decisao_de_saida()
                        exit()

                    else:
                        print("🛑 Interrupção: saindo do programa.")
                        exit()
                        break

                except ValueError:
                    print("❌ Erro: insira um número válido.\n")
                    sleep(2)

        elif decisao_operador_matemático == 6:

            # Rodando potenciação
            print("\n\n", 28*'='," Potenciação ", 27*'=', "\n\n")

            while True:
                try:
                    base = int(entrada("Base: "))
                    expoente = int(entrada("Expoente: "))

                    potenciacao(base, expoente)

                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                    if decisão_de_saida == 1:
                        rodar_decisao_de_saida()
                        exit()

                    else:
                        print("🛑 Interrupção: saindo do programa.")
                        exit()
                        break

                except ValueError:
                    print("❌ Erro: insira um número válido.\n")
                    sleep(2)
                    
                

        elif decisao_operador_matemático == 7:

            # Rodando raiz quadrada (sqrt)
            print("\n\n", 28*'='," Raiz Quadrada ", 27*'=', "\n\n")
            while True:
                try:
                    raiz = int(entrada("Raiz: "))

                    raiz_quadrada(raiz)

                    sleep(1.5)

                    decisão_de_saida = int(entrada("\n1. Continuar\n2. Finalizar Programa\n\n#Responda com números: "))

                    
                    if decisão_de_saida == 1:
                        rodar_decisao_de_saida()
                        exit()

                    else:
                        print("🛑 Interrupção: saindo do programa.")
                        exit()
                        break

                except ValueError:
                    print("❌ Erro: insira um número válido.\n")
                    sleep(2)

        elif decisao_operador_matemático == 8:

            # Rodando porcentagem
            print("\n\n", 28*'='," Porcentagem ", 27*'=', "\n\n")
            porcentagem()

rodar_programa_principal()