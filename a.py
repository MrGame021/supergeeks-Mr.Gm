import random, os, time

# os.system('cls')



d = ''
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
|                                               |
|   por: Murillo Souza                          |
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

p7 = ['Celular', 'Abóbora', 'Etienne', 'Empatia', 'Família']
d7 = ['Eletrônico', 'Comida', 'Nome', 'Sentimento', 'Pais']

p8 = ['Capivara', 'Suricato', '', 'Nintendo', 'Educação']
d8 = ['Animal', 'Animal','','Desenvolvedora de Jogos','Estudo']

p10 = ['Computador', 'Fleumático', 'Dicionário', 'Maturidade', 'Pragmático']
d10 = ['Eletrônico','Muito Paciente','Palavras','Crescimento','Ordem Prática']

p11 = ['Playstation', 'Perspectiva', 'Dissimulado', 'Compreensão', 'Preconceito']
d11 = ['Desenvolvedora de Jogos','Ponto de Vista','','Entendimento','']


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
    while True:
        print(f"{a}  Acerte a palavra  {a}")
        b = int(input('''
 ----------------------------------------------
|          Digite um número de 1 a 5:          |
|                                              |
|                                              |
|    1) ____                                   |
|                                              |
|    2) _______                                |
|                                              |
|    3) ________                               |
|                                              |
|    4) __________                             |
|                                              |
|    5) ___________                            |
|                                              |          
|                                              |
 ----------------------------------------------
'''))
        text = ''

        
        if(b == 1):
            x = random.randint(0, len(p4)-1)
            p = p4[x]
            d = d4[x]
              
        elif(b == 2):
            x = random.randint(0, len(p7)-1)
            p = p7[x]
            d = d7[x]
          
        
        elif(b == 3):
            x = random.randint(0, len(p8)-1)
            p = p8[x]
            d = d8[x]
          
        elif(b == 4):
            x = random.randint(0, len(p10)-1)
            p = p10[x]
            d = d10[x]
          
        elif(b == 5):
            x = random.randint(0, len(p11)-1)
            p = p11[x]
            d = d11[x]
        else:
            print("Essa opção não existe ou ainda não foi incrementada!")
            input()
            break
        os.system('cls')
    print("oi")
    input()
elif(c == 'B' or c == 'b'):
    while True:
        print(f"{a}  Acerte a palavra  {a}")
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
        text = ''

        
        if(b == 1):
            x = random.randint(0, len(p4)-1)
            p = p4[x]
            
              
        elif(b == 2):
            x = random.randint(0, len(p7)-1)
            p = p7[x]
            
          
        
        elif(b == 3):
            x = random.randint(0, len(p8)-1)
            p = p8[x]
            
          
        elif(b == 4):
            x = random.randint(0, len(p10)-1)
            p = p10[x]

          
        elif(b == 5):
            x = random.randint(0, len(p11)-1)
            p = p11[x]

            
        else:
            print("Essa opção não existe ou ainda não foi incrementada!")
            input()
            break
        
        os.system('cls')
    print("oi")
    input()





elif(c == 'C' or c == 'c'):
    while True:
        print(f"{a}  Acerte a palavra  {a}")
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
        text = ''

        
        if(b == 1):
            x = random.randint(0, len(p4)-1)
            p = p4[x]
            
              
        elif(b == 2):
            x = random.randint(0, len(p7)-1)
            p = p7[x]
            
            
            
        
        elif(b == 3):
            x = random.randint(0, len(p8)-1)
            p = p8[x]
            d = d8[x]
          
        elif(b == 4):
            x = random.randint(0, len(p10)-1)
            p = p10[x]

            
        elif(b == 5):
            x = random.randint(0, len(p11)-1)
            p = p11[x]
            
        else:
            print("Essa opção não existe ou ainda não foi incrementada!")
            input()
            break
        
        os.system('cls')
    
    input()
    
else:
    print("Não existe essa dificuldade. Favor, reinicie o programa")

