n1=float(input("Número 1: "))
n2=float(input("Número 2: "))
n3=float(input("Número 3: "))
n4=float(input("Número 4: "))
produto=n1*n2*n3*n4
if produto > 0:
    print(f"O produto dos 4 números é: {produto}", "O produto é positivo.", sep="\n")
else:
    print(f"O produto dos 4 números é: {produto}", "O produto não é positivo.", sep="\n")