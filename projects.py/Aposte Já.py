import random, time

lista_de_bets = [
    #Futebol
    "Sobre Futebol...\n\nO jogador chutou a bola. \n\nFoi gol ou não?",
    "Sobre Futebol...\n\nO goleiro pulou para o lado certo. \n\nDefendeu ou não?",
    "Sobre Futebol...\n\nO árbitro consultou o VAR. \n\nMarcou pênalti ou não?",
    "Sobre Futebol...\n\nO atacante estava impedido. \n\nO gol foi anulado ou não?",
    "Sobre Futebol...\n\nO zagueiro tocou com a mão na bola. \n\nO juiz marcou pênalti ou não?",
    "Sobre Futebol...\n\nO técnico fez uma substituição ofensiva. \n\nO time marcou um gol depois ou não?",
    "Sobre Futebol...\n\nO jogador recebeu um cartão amarelo. \n\nFoi expulso depois ou não?",
    "Sobre Futebol...\n\nO time ganhou o escanteio. \n\nConverteu em gol ou não?",
    "Sobre Futebol...\n\nO atacante ficou cara a cara com o goleiro. \n\nFez o gol ou não?",
    "Sobre Futebol...\n\nO jogador cobrou a falta direta. \n\nAcertou o gol ou não?",
    "Sobre Futebol...\n\nO time perdeu um jogador por lesão. \n\nGanhou o jogo mesmo assim ou não?",
    "Sobre Futebol...\n\nO juiz deu mais de 5 minutos de acréscimo. \n\nSaiu gol nos acréscimos ou não?",
    "Sobre Futebol...\n\nO lateral bateu um arremesso rápido. \n\nCriou uma jogada perigosa ou não?",
    "Sobre Futebol...\n\nO jogador fez embaixadinhas no jogo. \n\nFoi advertido pelo árbitro ou não?",
    "Sobre Futebol...\n\nO time teve mais posse de bola. \n\nVenceu a partida ou não?",
    "Sobre Futebol...\n\nO jogador chutou a bola. \n\nFoi gol ou não?",
    "Sobre Futebol...\n\nO goleiro pulou para o lado certo. \n\nDefendeu ou não?",
    "Sobre Futebol...\n\nO árbitro consultou o VAR. \n\nMarcou pênalti ou não?",
    "Sobre Futebol...\n\nO atacante estava impedido. \n\nO gol foi anulado ou não?",
    "Sobre Futebol...\n\nO zagueiro tocou com a mão na bola. \n\nO juiz marcou pênalti ou não?",
    "Sobre Futebol...\n\nO técnico fez uma substituição ofensiva. \n\nO time marcou um gol depois ou não?",
    "Sobre Futebol...\n\nO jogador recebeu um cartão amarelo. \n\nFoi expulso depois ou não?",
    "Sobre Futebol...\n\nO time ganhou o escanteio. \n\nConverteu em gol ou não?",
    "Sobre Futebol...\n\nO atacante ficou cara a cara com o goleiro. \n\nFez o gol ou não?",
    "Sobre Futebol...\n\nO juiz deu mais de 5 minutos de acréscimo. \n\nSaiu gol nos acréscimos ou não?",

    #Futsal
    "Sobre Futsal...\n\nO goleiro-linha entrou em quadra. \n\nO time empatou o jogo ou não?",
    "Sobre Futsal...\n\nO jogador bateu lateral com pressa. \n\nCriou chance clara de gol ou não?",
    "Sobre Futsal...\n\nA equipe cometeu 5 faltas no tempo. \n\nSofreu tiro livre direto ou não?",
    "Sobre Futsal...\n\nO pivô recebeu de costas para o gol. \n\nFinalizou com perigo ou não?",
    "Sobre Futsal...\n\nO jogador fez um drible no um contra um. \n\nGanhou o duelo ou não?",

    # Vôlei
    "Sobre Volei...\n\nO time sacou com força. \n\nConseguiu ace ou não?",
    "Sobre Volei...\n\nA equipe pediu desafio. \n\nA bola foi dentro ou não?",
    "Sobre Volei...\n\nO atacante explorou o bloqueio. \n\nA bola tocou no adversário ou não?",
    "Sobre Volei...\n\nO time salvou uma bola difícil na defesa. \n\nGanhou o ponto depois ou não?",
    "Sobre Volei...\n\nO bloqueio foi montado com dois jogadores. \n\nPararam o ataque ou não?",

    # Surf
    "Sobre Surf...\n\nO surfista entrou na onda. \n\nCompletou a manobra ou não?",
    "Sobre Surf...\n\nO atleta pegou uma onda grande. \n\nGanhou nota acima de 8.0 ou não?",
    "Sobre Surf...\n\nO surfista caiu durante a manobra. \n\nConseguiu se recuperar ou não?",
    "Sobre Surf...\n\nO competidor esperou por uma série de ondas a bateria toda. \n\nPegou a melhor onda da bateria ou não?",
    "Sobre Surf...\n\nO surfista tentou um aéreo. \n\nConseguiu completar a manobra ou não?"
]
lista_de_odds = {

    0: ['Sim',2.38, 'Não', 2.26],
    1: ['Sim', 2.33, 'Não', 2.22],
    2: ['Sim', 2.10, 'Não', 1.96],
    3: ['Sim', 1.86, 'Não', 1.80],
    4: ['Sim', 2.11, 'Não', 1.85],
    5: ['Sim', 2.46, 'Não', 2.05],
    6: ['Sim', 4.45, 'Não', 1.15],
    7: ['Sim', 6.56, 'Não', 1.25],
    8: ['Sim', 2.49, 'Não', 2.17],
    9: ['Sim', 6.99, 'Não', 1.12],
    10: ['Sim', 2.16, 'Não', 2.17],
    11: ['Sim', 2.38, 'Não', 1.73],
    12: ['Sim', 2.00, 'Não', 1.63],
    13: ['Sim', 4.12, 'Não', 1.12],
    14: ['Sim', 2.10, 'Não', 2.05],
    15: ['Sim', 2.43, 'Não', 2.06],
    16: ['Sim', 2.19, 'Não', 2.04],
    17: ['Sim', 2.43, 'Não', 1.79],
    18: ['Sim', 2.10, 'Não', 1.97],
    19: ['Sim', 2.01, 'Não', 1.78],
    20: ['Sim', 2.26, 'Não', 2.05],
    21: ['Sim', 4.53, 'Não', 1.11],
    22: ['Sim', 7.04, 'Não', 1.30],
    23: ['Sim', 2.02, 'Não', 2.14],
    24: ['Sim', 2.13, 'Não', 1.78],
    25: ['Sim', 2.20, 'Não', 2.09],
    26: ['Sim', 2.18, 'Não', 2.16],
    27: ['Sim', 1.84, 'Não', 1.78],
    28: ['Sim', 1.92, 'Não', 1.79],
    29: ['Sim', 1.93, 'Não', 1.63],
    30: ['Sim', 1.94, 'Não', 1.77],
    31: ['Sim', 2.18, 'Não', 2.00],
    32: ['Sim', 2.10, 'Não', 1.96],
    33: ['Sim', 1.83, 'Não', 1.69],
    34: ['Sim', 2.17, 'Não', 2.07],
    35: ['Sim', 2.14, 'Não', 2.00],
    36: ['Sim', 2.35, 'Não', 2.07],
    37: ['Sim', 2.95, 'Não', 1.65],
    38: ['Sim', 2.38, 'Não', 1.65],
    39: ['Sim', 2.91, 'Não', 1.75],
    40: ['Sim', 2.60, 'Não', 1.65],
    41: ['Sim', 2.53, 'Não', 1.72]
}
saldo_na_conta = [
    122, 418, 474, 269, 496, 33, 310, 132, 341, 297,
    94, 252, 115, 148, 448, 181, 346, 83, 113, 185,
    495, 30, 307, 390, 487, 199, 133, 303, 330, 134,
    260, 316, 343, 388, 275, 208, 44, 481, 422, 35,
    366, 87, 189, 266, 326, 301, 83, 450, 392, 124,
    127, 140, 263, 411, 337, 222, 444, 144, 417, 88,
    474, 379, 298, 293, 385, 40, 89, 94, 460, 117,
    204, 118, 486, 21, 223, 135, 431, 80, 142, 409,
    67, 289, 453, 394, 161, 437, 442, 248, 185, 159,
    150, 287, 370, 460, 127, 178, 100, 313, 208, 480,
    213, 314, 186, 136, 221, 139, 497, 83, 417, 99,
    47, 389, 196, 229, 412, 333, 470, 374, 103, 423,
    120, 106, 290, 38, 353, 465, 441, 70, 28, 498,
    195, 450, 367, 55, 349, 92, 121, 283, 27, 470,
    172, 443, 203, 462, 128, 71, 174, 100, 297, 251,
    93, 230, 306, 484, 193, 239, 59, 275, 244, 160,
    228, 411, 442, 36, 114, 497, 186, 78, 361, 220,
    408, 380, 11, 499, 299, 285, 33, 265, 396, 477
]




def rodar_aposta(saldo_atual):
    bet_sorteada = random.choice(lista_de_bets)
    posição_bet_sorteada = lista_de_bets.index(bet_sorteada)
    sim_ou_nao = random.choice(["Sim", "Não"])

    print(f"\n\n{bet_sorteada}")
    print(f"\nOdds:\nSim: ODD: {lista_de_odds[posição_bet_sorteada][1]}\nNão: ODD: {lista_de_odds[posição_bet_sorteada][3]}")
    time.sleep(2)

    while True:
        try:
            decisao = int(input("1. Sim | 2. Não\n\n= "))
            if decisao in [1, 2]:
                break
        except ValueError:
            pass
        print("\nTente novamente...\n")

    print(f"Seu saldo de freebet: R${saldo_atual:.2f}")
    
    while True:
        try:
            aposta = float(input("Valor da aposta: "))
            if aposta <= saldo_atual and aposta > 0:
                break
            print("Você não tem esse valor.")
        except ValueError:
            print("Digite um número válido.")

    saldo_restante = saldo_atual - aposta
    green_sim = (aposta * lista_de_odds[posição_bet_sorteada][1]) + saldo_restante
    green_nao = (aposta * lista_de_odds[posição_bet_sorteada][3]) + saldo_restante

    resposta = sim_ou_nao
    for x in range(1, 4):
        print(f"{x}")
        time.sleep(0.5)

    if resposta == "Sim" and decisao == 1:
        print("Você ganhou!!!!")
        novo_saldo = green_sim
    elif resposta == "Sim" and decisao == 2:
        print("Você perdeu, que pena.")
        novo_saldo = saldo_restante
    elif resposta == "Não" and decisao == 2:
        print("Você ganhou!!!!")
        novo_saldo = green_nao
    elif resposta == "Não" and decisao == 1:
        print("Você perdeu, que pena.")
        novo_saldo = saldo_restante
    else:
        print("Decisão inválida.")
        novo_saldo = saldo_restante

    print(f"Saldo atual: R${novo_saldo:.2f}")
    return novo_saldo

#Iniciando a casa de aposta

print(20*"=","APOSTE JÁ", 20*"=")
print("\n\nBem-vindo à APOSTE JÁ, a casa de aposta que te dá 50% de vencer\n")
print("Vamos começar...\n\n")
time.sleep(2)

#saldo inicial
saldo_inicial = random.choice(saldo_na_conta)
print("Antes de começar, vamos sortear o seu saldo para apostar...")
for _ in range(3):
    print(".")
    time.sleep(1)
print(f"Você recebeu R$ {saldo_inicial:.2f} de freebet!")
time.sleep(2)

#primeira aposta
saldo_atual = rodar_aposta(saldo_inicial)

# Enquanto quiser continuar e tiver saldo
while saldo_atual >= 5:
    continuar = input("\nDeseja continuar apostando? (s/n): ").lower()
    if continuar == "s":
        saldo_atual = rodar_aposta(saldo_atual)
    else:
        break

#Saldo final
print(f"\nObrigado por jogar! Seu saldo final é R${saldo_atual:.2f}")
