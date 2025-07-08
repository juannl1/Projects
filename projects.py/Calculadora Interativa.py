import time, math


print("1. Tabuada\n2. Cálculo específico\n\n*Responda com números*")
c1 = int(input("\nVocê quer alguma tabuada ou algum cálculo específico: "))

#Código da Tabuada abaixo 
if c1 == 1:
    print("\n   TABUADA   ")
    time.sleep(0.9)
    n1 = int(input("\nVamos calcular a tabuada de qual número: "))
    print("1. Adição\n2. Subtração\n3. Multiplicação\n")
    time.sleep(0.5)
    print("*Responda usando os números*\n")
    time.sleep(0.9)
    n2 = int(input("Digite um operador matemático: "))
    n3 = int(input("Até qual número você gostaria de ver a tabuada: "))
    print("\nPerfeito! Agora, vamos calcular a tabuada do número que você escolheu, utilizando o operador que você digitou.")
    n3 += 1
    if n2 == 1:
        print(f"Número escolhido: {n1}")
        print(f"Operador matemático: Adição (+)")
        print(f"Calcular até o número: {n3 - 1}")
        time.sleep(3.9)
        for i in range(1, n3):
            print(f"{n1} + {i} = {n1 + i}")
            time.sleep(0.1)
    elif n2 == 2:
        print(f"Número escolhido: {n1}")
        print(f"Operador matemático: Subtração (-)")
        print(f"Calcular até o número: {n3 - 1}")
        time.sleep(3.9)
        for i in range(1, n3):
            print(f"{n1} - {i} = {n1 - i}")
            time.sleep(0.1)
    elif n2 == 3:
        print(f"Número escolhido: {n1}")
        print(f"Operador matemático: Multiplicação (x)")
        print(f"Calcular até o número: {n3 - 1}")
        time.sleep(3.9)
        for i in range(1, n3):
            print(f"{n1} X {i} = {n1 * i}")
            time.sleep(0.1)
    else:
        print("Ocorreu um erro...")
        time.sleep(0.7)
        print("Recomeçando...")
        time.sleep(1.5)
        while True:
            print("1. Tabuada\n2. Cálculo específico\n\n*Responda com números*")
            c1 = int(input("\nVocê quer alguma tabuada ou algum cálculo específico: "))

            #Código da Tabuada abaixo 
            if c1 == 1:
                print("\n   TABUADA   ")
                time.sleep(0.9)
                n1 = int(input("\nVamos calcular a tabuada de qual número: "))
                print("1. Adição\n2. Subtração\n3. Multiplicação\n")
                time.sleep(0.5)
                print("*Responda usando os números*\n")
                time.sleep(0.9)
                n2 = int(input("Digite um operador matemático: "))
                n3 = int(input("Até qual número você gostaria de ver a tabuada: "))
                print("\nPerfeito! Agora, vamos calcular a tabuada do número que você escolheu, utilizando o operador que você digitou.")
                n3 += 1
                if n2 == 1:
                    print(f"Número escolhido: {n1}")
                    print(f"Operador matemático: Adição (+)")
                    print(f"Calcular até o número: {n3 - 1}")
                    time.sleep(3.9)
                    for i in range(1, n3):
                        print(f"{n1} + {i} = {n1 + i}")
                        time.sleep(0.1)
                elif n2 == 2:
                    print(f"Número escolhido: {n1}")
                    print(f"Operador matemático: Subtração (-)")
                    print(f"Calcular até o número: {n3 - 1}")
                    time.sleep(3.9)
                    for i in range(1, n3):
                        print(f"{n1} - {i} = {n1 - i}")
                        time.sleep(0.1)
                elif n2 == 3:
                    print(f"Número escolhido: {n1}")
                    print(f"Operador matemático: Multiplicação (x)")
                    print(f"Calcular até o número: {n3 - 1}")
                    time.sleep(3.9)
                    for i in range(1, n3):
                        print(f"{n1} X {i} = {n1 * i}")
                        time.sleep(0.1)
                else:
                    print("Ocorreu um erro...")
            #Código dos Cálculos específicos abaixo
            elif c1 == 2:
                print("\n   Cálculo Específico   ")
                time.sleep(1)
                print("\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Módulo (Resto da divisão)\n6. Potênciação\n7. Raiz Quadrada\n8. Porcentagem (Calcular Desconto ou taxa adicional)\n9. Fatorial(Tabuada)\n")
                time.sleep(1.6)
                n1 = int(input("Digite o número do operador matemático: "))
                if n1 == 1:
                    print("Ok, adição")
                    time.sleep(0.5)
                    n2 = int(input("Primeiro valor da adição: "))
                    n3 = int(input("Segundo valor da adição: "))
                    print(f"{n2} + {n3} = {n2 + n3}")
                elif n1 == 2:
                    print("Ok, Subtração")
                    time.sleep(0.5)
                    n2 = int(input("Primeiro valor da Subtração: "))
                    n3 = int(input("Segundo valor da Subtração: "))
                    print(f"{n2} - {n3} = {n2 - n3}")
                elif n1 == 3:
                    print("Ok, Multiplicação")
                    time.sleep(0.5)
                    n2 = int(input("Primeiro valor da Multiplicação: "))
                    n3 = int(input("Segundo valor da Multiplicação: "))
                    print(f"{n2} x {n3} = {n2 * n3}")
                elif n1 == 4:
                    print("Ok, Divisão")
                    time.sleep(0.5)
                    n2 = int(input("Primeiro valor da Divisão: "))
                    n3 = int(input("Segundo valor da Divisão: "))
                    print(f"{n2} / {n3} = {n2 / n3}")
                elif n1 == 5:
                    print("Ok, Módulo")
                    time.sleep(0.5)
                    n2 = int(input("Primeiro valor do Módulo: "))
                    n3 = int(input("Segundo valor do Módulo: "))
                    print(f"O resto da divisão {n2} / {n3} =  {n2 % n3}")
                elif n1 == 6:
                    print("Ok, Potênciação")
                    time.sleep(0.5)
                    n2 = int(input("Base: "))
                    n3 = int(input("Valor elevado: "))
                    print(f"{n2} ^ {n3} = {n2 ** n3}")
                elif n1 == 7:
                    print("Ok, Raiz quadrada")
                    time.sleep(0.5)
                    n2 = float(input("Digite o valor da Raiz: "))
                    print(f"A Raiz quadrada de {n2} = {math.sqrt(n2)}")
                elif n1 == 8:
                    print("\nOk, Porcentagem.")
                    time.sleep(0.5)
                    c1 = int(input("1. Taxa adicional\n2. Desconto\n\nDigite: "))
                    if c1 == 1:
                        print("não coloque operadores matemáticos")
                        time.sleep(0.5)
                        n2 = float(input("Valor cheio do produto: "))
                        n3 = float(input("Porcentagem da taxa adicional: %"))
                        porcentagem = n3 /100
                        taxa = porcentagem * n2
                        total = taxa + n2
                        print(f"Taxa adicional: R${taxa} \nTotal a pagar: R${total}")
                    elif c1 == 2:
                        print("não coloque operadores matemáticos")
                        time.sleep(1)
                        n2 = float(input("Valor cheio do produto: "))
                        n3 = float(input("Porcentagem do desconto: %"))
                        porcentagem = n3 /100
                        desconto = porcentagem * n2
                        total = n2 - desconto
                        print(f"O desconto é: R${desconto}\nTotal a pagar: R${total}")
                elif n1 == 9:
                    print("Ok, Fatorial")
                    n2 = int(input("\nDigite o fatorial que deseja saber o valor: !"))
                    time.sleep(0.5)
                    for i in range(1, n2):
                        i += 1
                        print(f"{i}! = {math.factorial(i)}")
                        time.sleep(0.1)
            else:
                print("Ocorreu um erro...")
#Código dos Cálculos específicos abaixo
elif c1 == 2:
    print("\n   Cálculo Específico   ")
    time.sleep(1)
    print("\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Módulo (Resto da divisão)\n6. Potênciação\n7. Raiz Quadrada\n8. Porcentagem (Calcular Desconto ou taxa adicional)\n9. Fatorial(Tabuada)\n")
    time.sleep(1.6)
    n1 = int(input("Digite o número do operador matemático: "))
    if n1 == 1:
        print("Ok, adição")
        time.sleep(0.5)
        n2 = int(input("Primeiro valor da adição: "))
        n3 = int(input("Segundo valor da adição: "))
        print(f"{n2} + {n3} = {n2 + n3}")
    elif n1 == 2:
        print("Ok, Subtração")
        time.sleep(0.5)
        n2 = int(input("Primeiro valor da Subtração: "))
        n3 = int(input("Segundo valor da Subtração: "))
        print(f"{n2} - {n3} = {n2 - n3}")
    elif n1 == 3:
        print("Ok, Multiplicação")
        time.sleep(0.5)
        n2 = int(input("Primeiro valor da Multiplicação: "))
        n3 = int(input("Segundo valor da Multiplicação: "))
        print(f"{n2} x {n3} = {n2 * n3}")
    elif n1 == 4:
        print("Ok, Divisão")
        time.sleep(0.5)
        n2 = int(input("Primeiro valor da Divisão: "))
        n3 = int(input("Segundo valor da Divisão: "))
        print(f"{n2} / {n3} = {n2 / n3}")
    elif n1 == 5:
        print("Ok, Módulo")
        time.sleep(0.5)
        n2 = int(input("Primeiro valor do Módulo: "))
        n3 = int(input("Segundo valor do Módulo: "))
        print(f"O resto da divisão {n2} / {n3} =  {n2 % n3}")
    elif n1 == 6:
        print("Ok, Potênciação")
        time.sleep(0.5)
        n2 = int(input("Base: "))
        n3 = int(input("Valor elevado: "))
        print(f"{n2} ^ {n3} = {n2 ** n3}")
    elif n1 == 7:
        print("Ok, Raiz quadrada")
        time.sleep(0.5)
        n2 = float(input("Digite o valor da Raiz: "))
        print(f"A Raiz quadrada de {n2} = {math.sqrt(n2)}")
    elif n1 == 8:
        print("\nOk, Porcentagem.")
        time.sleep(0.5)
        c1 = int(input("1. Taxa adicional\n2. Desconto\n\nDigite: "))
        if c1 == 1:
            print("não coloque operadores matemáticos")
            time.sleep(0.5)
            n2 = float(input("Valor cheio do produto: "))
            n3 = float(input("Porcentagem da taxa adicional: %"))
            porcentagem = n3 /100
            taxa = porcentagem * n2
            total = taxa + n2
            print(f"Taxa adicional: R${taxa} \nTotal a pagar: R${total}")
        elif c1 == 2:
            print("não coloque operadores matemáticos")
            time.sleep(1)
            n2 = float(input("Valor cheio do produto: "))
            n3 = float(input("Porcentagem do desconto: %"))
            porcentagem = n3 /100
            desconto = porcentagem * n2
            total = n2 - desconto
            print(f"O desconto é: R${desconto}\nTotal a pagar: R${total}")
    elif n1 == 9:
        print("Ok, Fatorial")
        n2 = int(input("\nDigite o fatorial que deseja saber o valor: !"))
        time.sleep(0.5)
        for i in range(1, n2):
            i += 1
            print(f"{i}! = {math.factorial(i)}")
            time.sleep(0.1)

else:
    print("Ocorreu um erro...")
    time.sleep(1.5)
    print("Recomeçando...")
    time.sleep(1.5)
    while True:
        print("1. Tabuada\n2. Cálculo específico\n\n*Responda com números*")
        c1 = int(input("\nVocê quer alguma tabuada ou algum cálculo específico: "))

        #Código da Tabuada abaixo 
        if c1 == 1:
            print("\n   TABUADA   ")
            time.sleep(0.9)
            n1 = int(input("\nVamos calcular a tabuada de qual número: "))
            print("1. Adição\n2. Subtração\n3. Multiplicação\n")
            time.sleep(0.5)
            print("*Responda usando os números*\n")
            time.sleep(0.9)
            n2 = int(input("Digite um operador matemático: "))
            n3 = int(input("Até qual número você gostaria de ver a tabuada: "))
            print("\nPerfeito! Agora, vamos calcular a tabuada do número que você escolheu, utilizando o operador que você digitou.")
            n3 += 1
            if n2 == 1:
                print(f"Número escolhido: {n1}")
                print(f"Operador matemático: Adição (+)")
                print(f"Calcular até o número: {n3 - 1}")
                time.sleep(3.9)
                for i in range(1, n3):
                    print(f"{n1} + {i} = {n1 + i}")
                    time.sleep(0.1)
            elif n2 == 2:
                print(f"Número escolhido: {n1}")
                print(f"Operador matemático: Subtração (-)")
                print(f"Calcular até o número: {n3 - 1}")
                time.sleep(3.9)
                for i in range(1, n3):
                    print(f"{n1} - {i} = {n1 - i}")
                    time.sleep(0.1)
            elif n2 == 3:
                print(f"Número escolhido: {n1}")
                print(f"Operador matemático: Multiplicação (x)")
                print(f"Calcular até o número: {n3 - 1}")
                time.sleep(3.9)
                for i in range(1, n3):
                    print(f"{n1} X {i} = {n1 * i}")
                    time.sleep(0.1)
            else:
                print("Ocorreu um erro...")
        #Código dos Cálculos específicos abaixo
        elif c1 == 2:
            print("\n   Cálculo Específico   ")
            time.sleep(1)
            print("\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Módulo (Resto da divisão)\n6. Potênciação\n7. Raiz Quadrada\n8. Porcentagem (Calcular Desconto ou taxa adicional)\n9. Fatorial(Tabuada)\n")
            time.sleep(1.6)
            n1 = int(input("Digite o número do operador matemático: "))
            if n1 == 1:
                print("Ok, adição")
                time.sleep(0.5)
                n2 = int(input("Primeiro valor da adição: "))
                n3 = int(input("Segundo valor da adição: "))
                print(f"{n2} + {n3} = {n2 + n3}")
            elif n1 == 2:
                print("Ok, Subtração")
                time.sleep(0.5)
                n2 = int(input("Primeiro valor da Subtração: "))
                n3 = int(input("Segundo valor da Subtração: "))
                print(f"{n2} - {n3} = {n2 - n3}")
            elif n1 == 3:
                print("Ok, Multiplicação")
                time.sleep(0.5)
                n2 = int(input("Primeiro valor da Multiplicação: "))
                n3 = int(input("Segundo valor da Multiplicação: "))
                print(f"{n2} x {n3} = {n2 * n3}")
            elif n1 == 4:
                print("Ok, Divisão")
                time.sleep(0.5)
                n2 = int(input("Primeiro valor da Divisão: "))
                n3 = int(input("Segundo valor da Divisão: "))
                print(f"{n2} / {n3} = {n2 / n3}")
            elif n1 == 5:
                print("Ok, Módulo")
                time.sleep(0.5)
                n2 = int(input("Primeiro valor do Módulo: "))
                n3 = int(input("Segundo valor do Módulo: "))
                print(f"O resto da divisão {n2} / {n3} =  {n2 % n3}")
            elif n1 == 6:
                print("Ok, Potênciação")
                time.sleep(0.5)
                n2 = int(input("Base: "))
                n3 = int(input("Valor elevado: "))
                print(f"{n2} ^ {n3} = {n2 ** n3}")
            elif n1 == 7:
                print("Ok, Raiz quadrada")
                time.sleep(0.5)
                n2 = float(input("Digite o valor da Raiz: "))
                print(f"A Raiz quadrada de {n2} = {math.sqrt(n2)}")
            elif n1 == 8:
                print("\nOk, Porcentagem.")
                time.sleep(0.5)
                c1 = int(input("1. Taxa adicional\n2. Desconto\n\nDigite: "))
                if c1 == 1:
                    print("não coloque operadores matemáticos")
                    time.sleep(0.5)
                    n2 = float(input("Valor cheio do produto: "))
                    n3 = float(input("Porcentagem da taxa adicional: %"))
                    porcentagem = n3 /100
                    taxa = porcentagem * n2
                    total = taxa + n2
                    print(f"Taxa adicional: R${taxa} \nTotal a pagar: R${total}")
                elif c1 == 2:
                    print("não coloque operadores matemáticos")
                    time.sleep(1)
                    n2 = float(input("Valor cheio do produto: "))
                    n3 = float(input("Porcentagem do desconto: %"))
                    porcentagem = n3 /100
                    desconto = porcentagem * n2
                    total = n2 - desconto
                    print(f"O desconto é: R${desconto}\nTotal a pagar: R${total}")
            elif n1 == 9:
                print("Ok, Fatorial")
                n2 = int(input("\nDigite o fatorial que deseja saber o valor: !"))
                time.sleep(0.5)
                for i in range(1, n2):
                    i += 1
                    print(f"{i}! = {math.factorial(i)}")
                    time.sleep(0.1)
        else:
            print("Ocorreu um erro...")