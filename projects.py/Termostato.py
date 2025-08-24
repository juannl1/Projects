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
                print(f"Temperatura alterada para: {temp_do_termostato}°C")
                break

            return temp_do_termostato

        except ValueError:
            print("Insira algo válido...")
            sleep(1)

temp_do_termostato = determinando_temperatura()
print(temp_do_termostato)
#def termostato():

    

print(20*'=', "Termostato", 20*'=')

temp_do_ambiente = [17, 4, 0, 3, 10, 7, 9, 2, 21, 20, 24, 23, 26, 30, 31, 38 , 35, 25]
temp_do_ambiente_sorteada = choice(temp_do_ambiente)
temp_do_termostato_padrao = 24 #24°C padrão



print(f"\n\nTEMPERATURA EXTERNA: {temp_do_ambiente_sorteada}°C")
print("\nO Termostato da casa está em 24°C.")

decisao = str(input("\n\nVocê deseja trocar a temperatura?\n\n> ")).lower().strip()

if decisao in ["não", "nao", "n", "no"]:
    print(f"Temperatuda do termostato está em {temp_do_termostato_padrao}°C")
    
else:
    determinando_temperatura()



#while True:
   