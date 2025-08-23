from os import system
from random import choice

system("cls") #limpando terminal

print(20*'=', "Termostato", 20*'=')

temp_do_ambiente = [21, 20, 24, 23, 26, 30, 31, 38, 35, 25]
temp_do_ambiente_sorteada = choice(temp_do_ambiente)
temp_do_ar_condicionado_padrão = 24 #24°C padrão


print(f"\n\nTEMPERATURA EXTERNA: {temp_do_ambiente_sorteada}°C")
temp_do_ar_condicionado = str(input("\nO Termostato da casa está em 24°C.\n\nVocê deseja trocar a temperatura?\n\n> ")).lower().strip()

if temp_do_ar_condicionado != "nao" or "não" or "n" or "no":
    print(f"Temperatuda do termostato está em {temp_do_ar_condicionado_padrão}°C")
else:
    temp_do_ar_condicionado = int(input("Nova temperatura: \n\n> "))
    print(f"Temperatura alterada para: {temp_do_ar_condicionado}°C")




#while True:
    