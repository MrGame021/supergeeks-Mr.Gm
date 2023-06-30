print("- Programa para Calculador de Notas: -\n\n")

print("ATENÇÃO: sempre que escrever uma nota, escreva com ponto. Ex.: 86 = 8.6\n")
materia = input("Escreva a matéria que quiser: ")
media = float(input("Digite a média onde estuda: "))

print("Da matéria de",materia,", escreva:\n")

print("- Primeiro Trimestre -\n\n")
nota1tri1 = float(input("A nota do trabalho: "))
nota2tri1 = float(input("A nota do teste: "))
nota3tri1 = float(input("A nota da prova: "))
tri1 = (nota1tri1+nota2tri1+nota3tri1)/3

print("\n- Segundo Trimestre: -\n\n")
nota1tri2 = float(input("A nota do trabalho: "))
nota2tri2 = float(input("A nota do teste: "))
nota3tri2 = float(input("A nota da prova: "))
tri2 = (nota1tri2+nota2tri2+nota3tri2)/3

print("\n- Terceiro Trimestre: -\n\n")
nota1tri3 = float(input("A nota do trabalho: "))
nota2tri3 = float(input("A nota do teste: "))
nota3tri3 = float(input("A nota da prova: "))
tri3 = (nota1tri3+nota2tri3+nota3tri3)/3

notaAno = (tri1+tri2+tri3)/3

print("\nNota do Primeiro Trimestre: ",tri1,"\n-------------")
print("Nota do Segundo Trimestre: ",tri2,"\n-------------")
print("Nota do Terceiro Trimestre: ",tri3)
print("\n\n- Nota Anual:",notaAno,"-\n")

print("- Passou ou não Passou? -\n\n")
if (notaAno >= media):
    print("Parabéns, você passou de ano!")
elif (notaAno >= 5):
    print("Você não passou de ano, se esforce para não rodar")
else:
    print("Você PODE passar! Se esforce na recuperação...")
    notaRec = int(input("Escreva a nota da recuperação: "))
    if (notaRec >= 5):
        print("Você passou!")
    else:
        print("Se esforce no ano que vem!")
