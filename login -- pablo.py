import os

nome = ''
senha = ''
logado = 0
confsenha = 0

while True:
    input()
    os.system('cls')
    menu = int(input('''
---- MENU ----
[1] Cadastrar
[2] Logar
[3] Encerrar
--------------
'''))
    if(menu == 1):
        print('CADASTRO: ')
        nome = input('Defina seu nome: ')
        while True:
            senha = input('Defina sua senha: ')
            confsenha = input('Confirme sua senha: ')
            if(senha == confsenha):
                print('Cadastro realizado com sucesso.')
                break
            else:
                print('As senhas não coincidem.')
        
    elif(menu == 2):
        print('LOGIN: ')
        while (logado == 0):
            t_nome = input('Informe seu nome: ')
            t_senha = input('Informe sua senha: ')
            if(t_nome == nome and t_senha == senha):
                print('\nBoas-vindas',nome)
                logado = 1
            else:
                print('Login incorreto.\n')
                
        while (logado == 1):
            opcao = int(input('''
O que deseja fazer?
[1] Continuar conectado
[2] Ping
[3] Desconectar
'''))
            if(opcao == 1):
                print('Continua conectado')
            elif(opcao == 2):
                print('Pong')
            elif(opcao == 3):
                logado = 0
                print(nome,'desconectou-se')
            else:
                print('Essa opção não existe.')
        
    elif(menu == 3):
        sair = input('Digite "sair" se tem certeza: ')
        if(sair == 'sair' or sair == 'Sair'):
            break
    else:
        print('Opção inválida.')


print('O programa finalizou.')