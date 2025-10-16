
soma_notas = 0 
numero_de_alunos = 0

while True:
    nota = int(input(f"Digite a nota do aluno {numero_de_alunos + 1}° (-1 para finalizar) > > > "))
    
    
    if nota == -1:
        break 

   
    soma_notas += nota
    numero_de_alunos += 1
    
if numero_de_alunos > 0:
    media_final = soma_notas / numero_de_alunos
    print(f"\nNotas computadas: {numero_de_alunos}")
    print(f"Soma total das notas: {soma_notas}")
    print(f"A média da turma é: {media_final:.2f}")
else:
    print("Nenhuma nota foi inserida.")