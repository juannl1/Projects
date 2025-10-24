#formulário

from os import system
system("cls")


print(30*"=")
print("Viação Nossa Senhora do Amparo")
print(30*"=")

matricula_do_fiscal = int(input("\nNº Matrícula: "))

ponto_de_contole = int(input("1. ESTAÇÃO N.S. MERCÊS (RIO)\n2. ESTAÇÃO JOÃO BRASIL (NIT)\n3. ESTAÇÃO N.S. MERCÊS (VOLTA)\n4. ESTAÇÃO JOÃO BRASIL (VOLTA)\n5. TRIBOBÓ VOLTA (RIO)\n6. TRIBOBÓ VOLTA (NIT)\n7. TRIBOBÓ URBn\n\n> > > "))

data = int(input("Data(Dia): "))

numero_da_linha = int(input("Nº da Linha\n1. 2146D   //   2. 4146D\n> > > "))

numero_do_carro = int(input("Nº Carro: "))

matricula_do_motorista = int(input("Matrícula Motorista: "))

saida_de_origem = str(input("Hora saída origem: "))
print(type(saida_de_origem))

chegada_no_ponto = str(input("Hora Chegada Ponto: "))
while True:
    try:
        roleta_inicial = int(input("Nº Roleta (INICIAL): "))
        roleta_local = int(input("Nº Roleta (local): "))

        calculo_de_passageiros = roleta_inicial - roleta_local

        if calculo_de_passageiros <= 50:
            print("Tente novamente...\nO número da roleta não está batendo")

        else:
            break

    except:
        print("Erro...")


passageiros_em_pé = int(input("Nº Passageiro em pé: "))

dados {
    
}