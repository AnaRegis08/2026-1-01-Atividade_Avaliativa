n1=int(input("Número 1: "))
n2=int(input("Número 2: "))
n3=int(input("Número 3: "))
n4=int(input("Número 4: "))
media=(n1+n2+n3+n4)/4
if media >= 6:
    print(f"A média é: {media}", "Situação: Aprovado(a)!", sep="\n")
else:
    print(f"A média é: {media}", "Situação: Reprovado(a)!", sep="\n")
