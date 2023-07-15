import os
import random

nome = ''
senha = ''
logado = 0
confsenha = 0

while True:
    os.system("pause")
    os.system('cls')
    menu = int(input('''
---- MENU ----
[1] Cadastrar
[2] Logar
[3] Dado
[4] (Em breve)
[5] Encerrar
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
        print('''
---- LOGIN: ----
''')
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
[1] Cadastrar
[2] Logar
[3] Dado
[4] (Em breve)
[5] Encerrar
'''))
            if(opcao == 1):
                print('Continua conectado')
            elif(opcao == 2):
                print('Pong')
            elif(opcao == 3):
                nDados = int(input('Quantos dados quer jogar?\n'))
                total_d = 0
                for i in range (nDados):
                    dado = random.randint(1,6)
                    total_d += dado
                print('O total de',nDados,'dados são, ao todo,',total_d)
            elif(opcao == 4):
                print('Ainda não tem nada aqui, em breve entrará mais conteudo!')
            elif(opcao == 5):
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