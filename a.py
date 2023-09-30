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

p7 = ['Celular', 'Abóbora', 'Etienne', 'Empatia', 'Família']
d7 = ['Eletrônico', 'Comida', 'Nome', 'Sentimento', 'Pais']
x7 = random.randint(0, len(p7)-1)

p8 = ['Capivara', 'Suricato', '', 'Nintendo', 'Educação']#
d8 = ['Animal', 'Animal','','Desenvolvedora de Jogos','Estudo']
x8 = random.randint(0, len(p8)-1)

p10 = ['Computador', 'Fleumático', 'Dicionário', 'Maturidade', 'Pragmático']
d10 = ['Eletrônico','Muito Paciente','Palavras','Crescimento','Ordem Prática']
x10 = random.randint(0, len(p10)-1)

p11 = ['Playstation', 'Perspectiva', '', 'Compreensão', 'Preconceito']
d11 = ['Desenvolvedora de Jogos','Ponto de Vista','','Entendimento','']#
x11 = random.randint(0, len(p11)-1)










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

if(c == 'A' or c == 'a'):
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
    text = ''

        
    if(b == 1):
        print(x4)
            
              
        
    else:
        print("Essa opção não existe ou ainda não foi incrementada!")
        input()
        
    os.system('cls')
print("oi")
input()
