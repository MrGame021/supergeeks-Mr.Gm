print(" - Tabela de Preços 'Seu Manoel' - \n\n")
a = float(input("Quanto que custa 1 pão?\n"))
b = int(input("\nQuantos pães que você quer comprar?\n"))

for c in range (1,b+1):
    if (c == 1):
        print(c,"pão:",a)
    else:
        print(c,"pães:",a*c)
