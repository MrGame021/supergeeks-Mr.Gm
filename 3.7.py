print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")
f = '190410'
g = 'Murillo'
print("Bem vindo ao programa!\n\n")
a = input("Essa é sua primeira vez(sim ou não)?\n")
#---------------------------------------------------------------------------------------------------------------
if (a == 'sim' or a == 'SIM' or a == 'Sim' or a == 'S' or a == 's'):
    print("Vamo fazer seu cadastro então!")
    h = input("Por favor, digite seu usuário ou e-mail:\n")
    b = input("Digite sua senha:\n")
    c = input("Confirme sua senha:\n")
    if (b == c):
        print("Cadastro realizado com sucesso!")
        print("LOGIN:\n")
        d = input("Digite seu usuário: ")
        e = input("Digite sua senha: ")
        if (h == d and b == e or c == e ):
            print("Bem-vindo",h,"!")
#---------------------------------------------------------------------------------------------------------------     
    else:
        print("Sua senha foi recusada, tente novamente!")
#---------------------------------------------------------------------------------------------------------------     
elif (a == 'Não' or a == 'não' or a == 'Nao' or a == 'nao' or a == 'N' or a == 'n'):
    print("LOGIN:\n")
    d = input("Digite seu usuário: ")
    e = input("Digite sua senha: ")
    if (f == e and g == d ):
        print("Bem-vindo",g,"!")
    else:
        print("Você não está registrado! Reeinicie seu programa para se registrar!")
        input("\nDigite 'enter' para sair do programa: ")
#---------------------------------------------------------------------------------------------------------------     
else:
    input("\nDigite 'enter' para sair do programa: ")
#---------------------------------------------------------------------------------------------------------------
input("\nDigite 'enter' para sair do programa: ")
