from os import system
from random import choice
from time import sleep

system("cls") #limpando terminal

def determinando_temperatura():
    while True:
        try:
            temp_do_termostato = int(input("\nNova temperatura: \n\n> "))

            if temp_do_termostato < 16 or temp_do_termostato > 32:
                print("O termostato tem um limite de temperaturas (16.....32)")
                sleep(1)

            else:
                return temp_do_termostato
                

        except ValueError:
            print("Insira algo válido...")
            sleep(1)




def Temperatura(temperatura_definida):

    while True:
        temperatura_definida += 1
        print(f"Temperatura ambiente: {temperatura_definida}°C")
        
        if temperatura_definida == temp_do_ambiente:
            print("ligando")
            
    


    

print(20*'=', "Termostato", 20*'=')

temp_do_ambiente = [17, 4, 0, 3, 10, 7, 9, 2, 21, 20, 24, 23, 26, 30, 31, 38 , 35, 25]
temp_do_ambiente_sorteada = choice(temp_do_ambiente)
temp_do_termostato_padrao = 22 #22°C padrão



print(f"\n\nTEMPERATURA EXTERNA: {temp_do_ambiente_sorteada}°C")
print("\nO Termostato da casa está em 22°C.")

decisao = str(input("\n\nVocê deseja trocar a temperatura?\n\n> ")).lower().strip()

if decisao in ["não", "nao", "n", "no"]:
    print(f"Temperatuda do termostato está em {temp_do_termostato_padrao}°C")
    
else:
    temperatura_alterada = determinando_temperatura() #Temperatura escolhida pelo usuário
    print(f"A temperatura foi alterada para {temperatura_alterada}°C")

if temp_do_termostato_padrao > temperatura_alterada:

    print("➡  Ar-Condicionado LIGADO ❄️  ...\n")

    while True: #Diminuindo temperatura

        temp_do_termostato_padrao -= 1
        sleep(3)

        if temp_do_termostato_padrao == temperatura_alterada - 1:
            print(f"\nTemperatura alcançada {temperatura_alterada}°C")
            sleep(1.5)
            print("\nDesligando Ar-Condicionado...")
            Temperatura(temperatura_alterada)
            break

        print(f"Temperatura do ambiente: {temp_do_termostato_padrao}°C")


elif temp_do_termostato_padrao < temperatura_alterada:

    print("➡  Aquecedor LIGADO 🔥  ...")

    while True:
        temp_do_termostato_padrao += 1
        sleep(2)

        if temp_do_termostato_padrao == temperatura_alterada + 1:
            print(f"Temperatura alcançada {temperatura_alterada}°C")
            sleep(1)
            print("Desligando aquecedor...")
            break

        print(f"Temperatura do ambiente: {temp_do_termostato_padrao}°C")
else:
    print(f"Ok, mantendo em {temp_do_termostato_padrao}")

Temperatura()



    
    

   