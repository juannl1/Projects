from datetime import datetime, timedelta
import pandas as pd
import os

class FormularioOnibus():
    def __init__(self):
        self.matricula_fiscal = None 
        self.numero_da_linha = None 
        self.ponto_de_controle = None 
        self.numero_do_carro = None
        self.matricula_do_motorista = None
        self.hora_de_saida = None
        self.hora_de_chegada = None
        self.tempo_viagem_total = None
        self.roleta_inicial = None
        self.roleta_local = None
        self.data_anotacao = None
        self.hora_anotacao = None
        self.pessoas_em_pe = None

        # Atualiza data e hora no momento da criação do objeto
        agora = datetime.now()
        self.data_anotacao = agora.strftime("%d/%m/%Y")
        self.hora_anotacao = agora.strftime("%H:%M:%S")

    def verificar_lotacao(self, roleta_inicial, roleta_local):

        calculo_de_pessoas_no_onibus = roleta_local - roleta_inicial
        calculo_de_pessoas_em_pe = calculo_de_pessoas_no_onibus - 52

        if calculo_de_pessoas_em_pe >= 1:
            self.pessoas_em_pe = calculo_de_pessoas_em_pe

        if calculo_de_pessoas_no_onibus > 52:
            print(f"Ônibus lotado {calculo_de_pessoas_no_onibus}/52\n{calculo_de_pessoas_em_pe} pessoas em pé\n")

        elif calculo_de_pessoas_no_onibus < 52:
            calculo_vagas = 52 - calculo_de_pessoas_no_onibus 
            print(f"Ônibus com {calculo_vagas} vagas\nVagas no Ônibus {calculo_de_pessoas_no_onibus}/52\n")

        else:
            print("Ônibus lotado... Sem vagas (52/52)\n")

    def calcular_percurso(self, hora_de_saida, hora_chegada):
        def limpar(h):
            h = h.replace(":", "").strip()
            return h.zfill(4)

        saida_limpa = limpar(hora_de_saida)
        chegada_limpa = limpar(hora_chegada)
        obj_saida = datetime.strptime(saida_limpa, "%H%M")
        obj_chegada = datetime.strptime(chegada_limpa, "%H%M")

        if obj_chegada < obj_saida:
            duracao = (obj_chegada + timedelta(days=1)) - obj_saida
        else:
            duracao = obj_chegada - obj_saida
        
        total_segundos = int(duracao.total_seconds())
        horas = total_segundos // 3600
        minutos = (total_segundos % 3600) // 60
        self.tempo_viagem_total = f"{horas:02d}:{minutos:02d}"
        return obj_saida.strftime("%H:%M"), obj_chegada.strftime("%H:%M")






# ----------------------- INICIANDO FORMULÁRIO -----------------------

while True:
    form = FormularioOnibus()
    
    # --- COLETA DE DADOS ---
    try:
        form.matricula_fiscal = int(input("\nNúmero da matrícula fiscal: "))
        
        lista_pontos = ["ESTAÇÃO N.S. MERCÊS (RIO)", "ESTAÇÃO JOÃO BRASIL (NIT)", "ESTAÇÃO N.S. MERCÊS (VOLTA)", "ESTAÇÃO JOÃO BRASIL (VOLTA)"]
        print("\nEscolha o ponto de controle:")

        for i, p in enumerate(lista_pontos, 1): print(f"{i}. {p}") # MOSTRANDO A LISTA DE PONTOS PARA O USUÁRIO

        ponto_idx = int(input(" > "))
        form.ponto_de_controle = lista_pontos[ponto_idx-1]

        linhas_jb = ("2144R", "4144R")
        linhas_merces = ("2146D", "4146D", "6146D", "2590R")
        
        if ponto_idx in [1, 3]:
            print("\nEscolha a linha:")
            for i, l in enumerate(linhas_merces, 1): print(f"{i}. {l}") # MOSTRANDO A LISTA DE LINHAS DA MERÇES PARA O USUÁRIO

            form.numero_da_linha = linhas_merces[int(input(" > ")) - 1]
        else:
            print("\nEscolha a linha:")
            for i, l in enumerate(linhas_jb, 1): print(f"{i}. {l}") # MOSTRANDO A LISTA DE LINHAS DA JOÃO BRASIL PARA O USUÁRIO

            form.numero_da_linha = linhas_jb[int(input(" > "))-  1]

        form.numero_do_carro = int(input("\nNúmero do carro: "))
        form.matricula_do_motorista = int(input("Matrícula do motorista: "))
        
        h_saida = input("\nHora de saída (ex: 07:50): ")
        h_chegada = input("Hora de chegada (ex: 09:00): ")
        form.hora_de_saida, form.hora_de_chegada = form.calcular_percurso(h_saida, h_chegada)

        form.roleta_inicial = int(input("\nRoleta Inicial: "))
        form.roleta_local = int(input("Roleta Final: "))
        
        # --- RELATÓRIO E SALVAMENTO ---
        print("\n" + "="*30 + "\nRELATÓRIO DE CONFERÊNCIA\n" + "="*30)

        form.verificar_lotacao(form.roleta_inicial, form.roleta_local)

        print(f"Linha: {form.numero_da_linha} | Carro: {form.numero_do_carro}")
        print(f"Tempo Total: {form.tempo_viagem_total}")
        
        opcao = input("\n1. Salvar Informações\n2. Corrigir (Reiniciar)\n0. Sair\n > ")

        if opcao == "1":
            # Configuração de Caminhos (FORA DO IF DE EXISTÊNCIA)
            caminho_script = os.path.dirname(os.path.abspath(__file__))
            pasta_banco = os.path.join(caminho_script, 'banco-de-dados')
            
            if not os.path.exists(pasta_banco):
                os.makedirs(pasta_banco)
            
            caminho_final = os.path.join(pasta_banco, 'base-de-dados-form.csv')

            
            dados_form = {
                "Data": [form.data_anotacao],
                "Hora Anotação": [form.hora_anotacao],
                "Fiscal": [form.matricula_fiscal],
                "Linha": [form.numero_da_linha],
                "Ponto": [form.ponto_de_controle],
                "Carro": [form.numero_do_carro],
                "Motorista": [form.matricula_do_motorista],
                "Saída": [form.hora_de_saida],
                "Chegada": [form.hora_de_chegada],
                "Duração": [form.tempo_viagem_total],
                "Roleta Inicial": [form.roleta_inicial],
                "Roleta Local": [form.roleta_local]
            }

            df = pd.DataFrame(dados_form)
            # SALVANDO NO CSV
            df.to_csv(caminho_final, mode="a", index=False, header=not os.path.exists(caminho_final), sep=';', encoding="utf-8-sig")
            print(f"\n✅ Salvo com sucesso em: {caminho_final}")
            
            cont = input("\nDeseja realizar novo cadastro? (s/n): ").lower()
            if cont != 's': break

        elif opcao == "0":
            break
        else:
            print("\nReiniciando formulário...")

    except Exception as e:
        print(f"\n❌ Erro: {e}. Tente novamente.")

        
