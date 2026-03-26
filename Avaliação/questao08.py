n1=int(input("Número 1: "))
n2=int(input("Número 2: "))
n3=int(input("Número 3: "))
n4=int(input("Número 4: "))
soma=n1+n2+n3+n4
if soma > 100:
    print(f"A soma dos 4 números é: {soma}", "A soma é maior que 100.", sep="\n")
else:
    print(f"A soma dos 4 números é: {soma}", "A soma não é maior que 100.", sep="\n")