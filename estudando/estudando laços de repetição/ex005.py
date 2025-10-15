"""
4. Média de Notas de Alunos
Crie um programa que peça a nota de 2 alunos e armazene-as em uma lista. Após coletar todas as notas, calcule e imprima a média dessas notas.
"""

alunos = []
notas = []
for i in range(1, 2 + 1):
    nome = str(input("Digite o nome do aluno(a): "))
    nota1 = float(input("Digite a 1° nota: "))
    nota2 = float(input("Digite a 2° nota: "))

    alunos.append(nome)
    notas.append(nota1)
    notas.append(nota2)


media1 = (notas[0] + notas[1]) / 2
media2 = (notas[2] + notas[3]) / 2

print(f"{alunos[0]}: Média: {media1}")
print(f"{alunos[1]} Média: {media2}")

