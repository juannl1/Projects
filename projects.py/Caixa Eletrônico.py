"""
Primeiro Desafio

História

João precisa sacar dinheiro para suas despesas semanais. Ele decide ir até o caixa eletrônico mais próximo de sua casa. Ao chegar, ele insere seu cartão e espera o sistema iniciar. João sabe que precisa digitar sua senha corretamente e escolher o tipo de operação que deseja realizar. Ele também está ciente de que, dependendo do valor que deseja sacar, o caixa pode solicitar a confirmação de algumas informações adicionais ou informar sobre a indisponibilidade de notas para o valor solicitado. Após completar sua transação, João espera receber o dinheiro, o recibo da operação (caso deseje) e seu cartão de volta, para então poder sair do caixa eletrônico e continuar seu dia.
"""




from os import system
from time import sleep
from random import randint, choice, sample



def limpar_terminal():
    system("cls")

def saque():
        print("4 Digitos")
        for x in range(1, 4):
            
            informando_codigo_para_saque = int(input("Senha de saque > > > "))

            if informando_codigo_para_saque == 1234:
                print("\n✅ Sucesso\n")
                break

        else:
            print("\n❌ Acesso Negado.")
            exit()

        valores_disponiveis_para_saque = (20, 40, 50, 100, 300, 500, 900, 1000)

        print("\nSaque\n")
        for i, valores in enumerate(valores_disponiveis_para_saque, start=1):
            print(f"\nNota: R${i} - Quantidade de notas no caixa: {valores}")
        
        qtd_de_saque = int(input("Digite sua opção > > > "))
        print("Digite")



limpar_terminal()

print("<", 20*'-', "CAIXA ELETRÔNICO", 20*'-', ">")

print("Insira o cartão...\n")
comecando_programa = input("Aperte (ENTER) para inserir o cartão\n\n> > > ")

print("\b\nIniciando...")
sleep(1)


senha_do_joao = 123456
codigo_do_saque = 1234
print("Você tem 3 tentativas para inserir sua senha")
for i in range(1, 4):
    senha = int(input("\nDigite sua senha: "))
    
    if senha == senha_do_joao:
        print("\n✅ Sucesso\n")
        break
    
    elif senha != senha_do_joao:
        print("\n❌ Senha Incorreta\n")

else:
    print("\nSuas tentativas acabaram\n")
    sleep(1.5)
    print("\n❌ Acesso negado...\n")
    exit()


print("<", 20*'-', "Bem vindo, João", 20*'-', ">\n")

menu_de_opcoes = ("Saque", "Consulta de saldo", "Extrato", "Depósitos", "Transferências", "Pagamentos", "Alterar senha")

for i , opcoes in enumerate(menu_de_opcoes, start=1):
    print(f"{i}. {opcoes}")
    sleep(0.3)
sleep(1)
decisao_do_menu_de_opcoes = int(input("\n> > > "))


banco_de_notas = {
    #notas #qtd de notas
    2: 30,
    5: 37,
    10: 52,
    20: 60,
    50: 47,
    100: 213,
    200: 143
}



if decisao_do_menu_de_opcoes == 1:
    saque()




