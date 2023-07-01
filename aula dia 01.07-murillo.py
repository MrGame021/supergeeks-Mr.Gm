print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n\n")
print("Bem vindo ao programa!\n\n")
a = input("Essa é sua primeira vez(sim ou não)?")
if (a == 'sim' or a == 'SIM' or a == 'Sim'):
    print("Vamo fazer seu cadastro então!")
    input("Por favor, digite seu usuário/nome ou e-mail:\n")
    b = input("Digite sua senha:\n")
    c = input("Confirme sua senha:\n")
    if (b == c):
        print("bem vindo ao programa!")
