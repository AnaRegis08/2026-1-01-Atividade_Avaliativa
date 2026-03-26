alunos = []
for indice in range(15):
    entrada = input("Insira as notas e o nome do aluno(a)(*seguindo esse modelo: N1 N2 N3 N4 Nome): ")
    vetor = entrada.split()
    [n1, n2, n3, n4, nome] = vetor
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)
    media = (n1 + n2 + n3 + n4) / 4
    situacao = ""
    if media >= 6:
        situacao = "aprovado"
    if media < 4:
        situacao = "reprovado"
    if 4 <= media < 6:
        situacao = "recuperação"
    alunos.append([n1, n2, n3, n4, media, situacao, nome,])

for aluno in alunos:
    print(aluno)
