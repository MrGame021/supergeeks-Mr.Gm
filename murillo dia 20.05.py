print("-------------------------------------------------------------------------------\nEx1:\n")
b = int(input("Diga sua idade: "))
if(b >= 18):
        print("Você é adulto!!")
elif(b >= 13):
        print("Você é adolecente, espere",18-b,"anos para ser adulto!")
elif(b >= 4):
        print("Você é criança, espere",13-b,"para ser adolecente!")
else:
        print("Você é bebê!")

print("-------------------------------------------------------------------------------\nEx:2\n")
print("-=-Primeira dupla-=-\n")
c = int(input("Diga a idade: "))
d = int(input("Diga a idade: "))
print("\n-=-Segunda dupla-=-\n")
e = int(input("Diga a idade: "))
f = int(input("Diga a idade: "))
g = c+d
h = e+f
print("\n-=-Resposta final-=-\n")
print("A primeira dupla tem",g,"anos")]
print("A primeira dupla tem",h,"anos")
if(g<h):
        print("A segunda dupla são os mais velhos, somando suas idades!")
elif(g==h):
        print("As duas duplas tem a mesma idade")
else:
        print("A primeira dupla são os mais velhos, somando suas idades!")

print("-------------------------------------------------------------------------------\nEx:3\n")
print("=-=Ganhos=-=\n")
i = int(input("Me diga quantas horas você trabalha por dia/noite: "))
j = int(input("Me diga quanto você ganha por hora: "))
print("\n=-=Boletos=-=")
k = int(input("Gastos em água: "))
l = int(input("Gastos em luz: "))
m = int(input("Gastos em internet: "))
n = int(input("Gastos em comida: "))
o = i*j
p = k+l+m+n
if(o>=p):
    print("Você conseguiu pagar tudo!!")
else:
    print("Não teve dinheiro o suficiente! Faltou",p-o,"reais")
