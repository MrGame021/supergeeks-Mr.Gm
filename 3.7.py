print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n\n")
f = 190410
g = 'Murillo'
print("Bem vindo ao programa!\n\n")
a = input("Essa é sua primeira vez(sim ou não)?\n")
if (a == 'sim' or a == 'SIM' or a == 'Sim'):
    print("Vamo fazer seu cadastro então!")
    input("Por favor, digite seu usuário/nome ou e-mail:")
    b = input("Digite sua senha:\n")
    c = input("Confirme sua senha:\n")
    if (b == c):
        print("bem vindo ao programa!")
    else: print("Sua senha foi recusada, tente novamente!")
else:
    d = input("Digite seu usuário: ")
    e = input("Digite sua senha: ")
    if (f == e and g == d ):
        print("Bem-vindo",g,"!")
    else:
        print("Você não está registrado! Reeinicie seu programa para se registrar!")
