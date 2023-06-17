import random
a = random.randint(1,10)

print("- Par ou Ímpar: -\n\n")
b = input("Escolha: Par ou Ímpar?\n")
c = int(input("Escreva um número inteiro de 1 a 10: "))
d = a+c

if(d%2 == 0):
    if (b == 'par' or b == 'Par'):
        print("\nO número que o computador escolheu:",a)
        print("O número que você escolheu:",c)
        print(a,"+",c,"=",d)
        print("Parabéns, você ganhou o jogo!")
    else:
        print("\nO número que o computador escolheu:",a)
        print("O número que você escolheu:",c)
        print(a,"+",c,"=",d)
        print("Tente outra vez, você perdeu o jogo!")
else:
    if (b == 'ímpar' or b == 'impar' or b == 'Ímpar' or b == 'Impar'):
        print("\nO número que o computador escolheu:",a)
        print("O número que você escolheu:",c)
        print(a,"+",c,"=",d)
        print("Parabéns, você ganhou o jogo!")
    else:
        print("\nO número que o computador escolheu:",a)
        print("O número que você escolheu:",c)
        print(a,"+",c,"=",d)
        print("Tente outra vez, você perdeu o jogo!")
