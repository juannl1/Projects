def determinando_temperatura():
    while True:
        try:
            temp_do_termostato = int(input("\nNova temperatura: \n\n> "))

            if temp_do_termostato < 16 or temp_do_termostato > 32:
                print("O termostato tem um limite de temperaturas (16.....32)")
                

            else:
                print(f"Temperatura alterada para: {temp_do_termostato}°C")
                break

            return temp_do_termostato

        except ValueError:
            print("Insira algo válido...")
            

determinando_temperatura()
temp_do_termostato = determinando_temperatura()
print(temp_do_termostato)