import random, time, math

print("Sorteador de Times")

quantidade = int(input("Quantas pessoas você quer sortear -> "))
t1 = (quantidade % 2) #modulo tem q ser == a 0 para a quantidade de pessoas ser par
if t1 != 0:
    print("Você está sorteando um time com número impar, um dos times ficará com 1 a mais.")

players = []

for i in range(1, quantidade + 1):
    player = str(input(f"Player {i} -> "))
    players.append(player)
print(*players)

meio = math.ceil(len(players) / 2)
print(meio)
sorteador = random.shuffle(players)

print("\n\nPrimeiro time...\n")
print(20*"=")
print(*players[0:meio])
print(20*"=")
print("\nSegundo Time...\n")
print(20*"=")
print(*players[meio:])
print(20*"=")

time.sleep(1.2)
print("S para sim\nN para não")
mapa = str(input("Você deseja sortear o mapa ? ")).upper()


if mapa == "S":
    
    print(17*"=")
    print("Sorteador de mapa")
    print(17*"=")

    mapas = []

    quantidade_mapas = int(input("Digite a quantidade de mapas que você deseja sortear: "))
    for i in range(1, quantidade_mapas + 1):
        print(f"Map_{i}")
        time.sleep(0.1)
        mapas.append(quantidade_mapas)

    sorteador_mapas = random.randint(1, quantidade_mapas)
    time.sleep(0.7)
    print(f"\nMapa sorteado --> Map_{sorteador_mapas}")


    time.sleep(1.7)
    input("\n\nAperte ENTER para sair...")
else:
    print("Ok, Terminamos...")
    time.sleep(1.7)
    input("\n\nAperte ENTER para sair...")

