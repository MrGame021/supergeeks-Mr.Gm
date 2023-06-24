print(" - Elefantinho - \n\n")
a = int(input("Quantos elefantes você quer: "))
print("\nA música pronta ficou assim: \n")

for b in range (1,a+1):
    if (b == 1):
        print(b,"elefante incomoda muita gente")

    elif (b%2 == 1):
        print(b,"elefantes incomodam muita gente")
    else:
        c = 'incomodam '*b
        print(b,"elefantes",c,"muito mais")
