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
|   [1] - Jogo                                 |
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
    if (d == 1):#dificuldade
        dif = int(input('''
 ----------------------------------------------
|        Escolha a dificuldade do jogo:        |
|                                              |
|                                              |
|    [1] - Normal                              |
|                                              |
|                                              |
|    [2] - Difícil                             |
|                                              |
|                                              |
|    [3] - Muito Difícil                       |
|                                              |
|                                              |
|                                              |          
|                                              |
 ----------------------------------------------

'''))
        os.system('cls')     #palavras
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
        if(dif == 1 or dif == 2):
            vida = 5
        elif(dif == 3):
            vida = 3
            dica = '▓▓▓▓▓▓▓'
        else:
            input('Reinicie o jogo!')
            break
forca = []














    elif(d == 2):
        print('''
 ----------------------------------------------
|                 Sobre o jogo:                |
|                                              |
|       O jogo da forca é um jogo em que o     |
|         jogador tem que acertar qual         |
|    é a palavra proposta, tendo como dica     |
|     o número de letras e o tema ligado       |
|                 à palavra.                   |
|     A cada letra errada, é desenhado uma     |
|         parte do corpo do enforcado.         |
|                                              |
|                                              |
|                  BOA SORTE!                  |
|                                              |
|                                              |
 ----------------------------------------------
 ''')
        input()
        os.system('cls')
    elif(d == 3):
        break
        input("Aperte ENTER para sair do programa!")




            #else:
               # print("Essa opção não existe ou ainda não foi incrementada!")
               # input()
               # os.system('cls')





