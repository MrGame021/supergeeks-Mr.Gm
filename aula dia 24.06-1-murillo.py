print("- Tabuada -\n\n")
a = int(input("Escreva um número que queira saber a tabuada: "))
print("\nA tabuada do número",a,"até 10 é:\n")
for c in range (1,11):
    print(a,"x",c,"=",a*c)
input(" - Aperte qualquer tecla para sair do pregrama: - \n")
