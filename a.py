import random, os

# os.system('cls')


a = "=-"*7+"="
print(f'''
 -----------------------------------------------
|                                               |
|                                               |
|  {a}    Forca    {a}  |
|                                               |
|                                               |
|                                               |
|                                               |
|               por: Murillo Souza              |
|                                               |
|                                               |
|                                               |
|                                               |
|                                               |          
|                                               |
 -----------------------------------------------

''')
input()
os.system('cls')

p4 = ['Urso', 'Caos', 'Copo', 'Alto', 'Doce']
d4 = ['Animal', 'Situação', 'Cosinha', 'Altura', 'Gosto/Sentimento']
x4 = random.randint(0, len(p4)-1)
palaEsc4 = p4[x4]
dicaEsc4 = d4[x4]

p7 = ['Celular', 'Abóbora', 'Etienne', 'Empatia', 'Família']
d7 = ['Eletrônico', 'Comida', 'Nome', 'Sentimento', 'Pais']
x7 = random.randint(0, len(p7)-1)
palaEsc7 = p7[x7]
dicaEsc7 = d7[x7]

p8 = ['Capivara', 'Suricato', '', 'Nintendo', 'Educação']#
d8 = ['Animal', 'Animal','','Desenvolvedora de Jogos','Estudo']
x8 = random.randint(0, len(p8)-1)
palaEsc8 = p8[x8]
dicaEsc8 = d8[x8]

p10 = ['Computador', 'Fleumático', 'Dicionário', 'Maturidade', 'Pragmático']
d10 = ['Eletrônico','Muito Paciente','Palavras','Crescimento','Ordem Prática']
x10 = random.randint(0, len(p10)-1)
palaEsc10 = p10[x10]
dicaEsc10 = d10[x10]

p11 = ['Playstation', 'Perspectiva', '', 'Compreensão', 'Preconceito']
d11 = ['Desenvolvedora de Jogos','Ponto de Vista','','Entendimento','']#
x11 = random.randint(0, len(p11)-1)
palaEsc11 = d11[x11]
dicaEsc11 = d11[x11]

while True:
    d = int(input('''
 ----------------------------------------------
|            Painel de Informações:            |
|                                              |
|                                              |
|   [1] - Escolher Dificuldade                 |
|                                              |
|                                              |
|   [2] - Sobre                                |
|                                              |
|                                              |
|   [3] - Sair                                 |
|                                              |
|                                              |
|                                              |          
|                                              |
 ----------------------------------------------
'''))
    os.system('cls')
    if (d == 1):
        c = input('''
 ----------------------------------------------
|        Escolha a dificuldade do jogo:        |
|                                              |
|                                              |
|    A - Normal                                |
|                                              |
|                                              |
|    B - Difícil                               |
|                                              |
|                                              |
|    C - Muito Difícil                         |
|                                              |
|                                              |
|                                              |          
|                                              |
 ----------------------------------------------

''')
        os.system('cls')
        b = int(input('''
 ----------------------------------------------
|          Digite um número de 1 a 5:          |
|                                              |
|                                              |
|    1) _ _ _ _                                |
|                                              |
|    2) _ _ _ _ _ _ _                          |
|                                              |
|    3) _ _ _ _ _ _ _ _                        |
|                                              |
|    4) _ _ _ _ _ _ _ _ _                      |
|                                              |
|    5) _ _ _ _ _ _ _ _ _ _ _                  |
|                                              |          
|                                              |
 ----------------------------------------------
'''))
        os.system('cls')
        if(c == 'A' or c == 'a'):
            if(b == 1):
                print(palaEsc4)
                print(dicaEsc4)
                print(x4)
            elif(b == 2):
                print(palaEsc7)
                print(dicaEsc7)
                print(x7)
            elif(b == 3):
                print(palaEsc8)
                print(dicaEsc8)
                print(x8)
            elif(b == 4):
                print(palaEsc10)
                print(dicaEsc10)
                print(x10)
            elif(b == 5):
                print(palaEsc11)
                print(dicaEsc11)
                print(x11)
            else:
                print("Essa opção não existe ou ainda não foi incrementada!")
                input()
                os.system('cls')
                print("oi")
                input()
    elif(d == 2):
        print('''
 ----------------------------------------------
|                 Sobre o jogo:                 |
|                                               |
|     O jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra proposta, tendo como dica o número de letras e o tema ligado à palavra. A cada letra errada, é desenhado uma parte do corpo do enforcado.|
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |          
|     |
 ----------------------------------------------
 ''')
