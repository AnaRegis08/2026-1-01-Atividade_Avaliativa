alunos = []
for indice in range(15):
    entrada = input("N1 N2 N3 N4 Nome")
    vetor = entrada.split()
    # N1 = vetor[0]
    # n2 = vetor[1]
    [n1, n2, n3, n4, nome] = vetor
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)
    media = (n1 + n2 + n3 + n4) / 4
    # aprovado = media >= 6
    # reprovado = media < 4
    # recuperação = 4 <= media < 6
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
