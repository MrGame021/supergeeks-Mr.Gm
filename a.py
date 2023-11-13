import random, os
# os.system('cls')

p4 = ['Urso', 'Caos', 'Copo', 'Alto', 'Doce']
d4 = ['Animal', 'Situação', 'Cozinha', 'Altura', 'Gosto/Sentimento']
x4 = random.randint(0, len(p4)-1)
palaEsc4 = p4[x4]
dicaEsc4 = d4[x4]

p7 = ['Celular', 'Abóbora', 'Etienne', 'Empatia', 'Família']
d7 = ['Eletrônico', 'Comida', 'Nome', 'Sentimento', 'Pais']
x7 = random.randint(0, len(p7)-1)
palaEsc7 = p7[x7]
dicaEsc7 = d7[x7]

p8 = ['Capivara', 'Suricato', 'Nintendo', 'Educação']
d8 = ['Animal', 'Animal','Desenvolvedora de Jogos','Estudo']
x8 = random.randint(0, len(p8)-1)
palaEsc8 = p8[x8]
dicaEsc8 = d8[x8]

p10 = ['Computador', 'Fleumático', 'Dicionário', 'Maturidade', 'Pragmático']
d10 = ['Eletrônico','Muito Paciente','Palavras','Crescimento','Ordem Prática']
x10 = random.randint(0, len(p10)-1)
palaEsc10 = p10[x10]
dicaEsc10 = d10[x10]

p11 = ['Playstation', 'Perspectiva', 'Compreensão']
d11 = ['Desenvolvedora de Jogos','Ponto de Vista', 'Entendimento',]
x11 = random.randint(0, len(p11)-1)
palaEsc11 = p11[x11]
dicaEsc11 = d11[x11]

forca4 = []
forca7 = []
forca8 = []
forca10 = []
forca11 = []

while True:
    d = input('''
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
''')
    os.system('cls')
    if (d == '1'):            #dificuldade
        di = int(input('''
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
        


        
        if(di == 1):
            dif = 1
            
        elif(di == 2):
            dif = 2
            
        elif(di == 3):
            dif = 2
            dicaEsc4 = '▓▓▓▓▓▓▓'
            dicaEsc7 = '▓▓▓▓▓▓▓'
            dicaEsc8 = '▓▓▓▓▓▓▓'
            dicaEsc10 = '▓▓▓▓▓▓▓'
            dicaEsc11 = '▓▓▓▓▓▓▓'

        
        arte = [
    '''
    ┌───┐    
    │
    │
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │   |
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │  /|
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │  /|\\
    │
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │  /|\\
    │  /
    ┴
    ''',
    '''
    ┌───┐    
    │   O
    │  /|\\
    │  / \\
    ┴
    ''',
    ]
        erros = ''
        vida = 0

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
    #gerando texto da forca
        if(b == 1):
            for i in palaEsc4:
                if(i == '-'):
                    forca4.append('- ')
                elif(i == ' '):
                    forca4.append(' ')
                else:
                    forca4.append('_ ')

        elif(b == 2):
            for i in palaEsc7:
                if(i == '-'):
                    forca7.append('- ')
                elif(i == ' '):
                    forca7.append(' ')
                else:
                    forca7.append('_ ')

        elif(b == 3):
            for i in palaEsc8:
                if(i == '-'):
                    forca8.append('- ')
                elif(i == ' '):
                    forca8.append(' ')
                else:
                    forca8.append('_ ')

        elif(b == 4):
            for i in palaEsc10:
                if(i == '-'):
                    forca10.append('- ')
                elif(i == ' '):
                    forca10.append(' ')
                else:
                    forca10.append('_ ')

        elif(b == 5):
            for i in palaEsc11:
                if(i == '-'):
                    forca11.append('- ')
                elif(i == ' '):
                    forca11.append(' ')
                else:
                    forca11.append('_ ')
        while True:
            os.system('cls')
            texto = ''

            #montando texto da forca
            if(b == 1):
                for i in forca4:
                    texto += i
            elif(b == 2):
                for i in forca7:
                    texto += i
            elif(b == 3):
                for i in forca8:
                    texto += i
            elif(b == 4):
                for i in forca10:
                    texto += i
            elif(b == 5):
                for i in forca11:
                    texto += i
            #verificando vitoria
            if(b == 1):
                if(palaEsc4 == texto):
                    
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc4}
    Erros: {erros}

            PARABÉNS, VOCÊ ACERTOU A PALAVRA\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
                else:
                    letra = input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc4}
    Erros: {erros}

    Escolha uma letra: ''')
            elif(b == 2):
                if(palaEsc7 == texto):
                    
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc7}
    Erros: {erros}

            PARABÉNS, VOCÊ ACERTOU A PALAVRA\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
                else:
                    letra = input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc7}
    Erros: {erros}

    Escolha uma letra: ''')
                    
            elif(b == 3):
                if(palaEsc8 == texto):
                    os.system('cls')
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc8}
    Erros: {erros}

            PARABÉNS, VOCÊ ACERTOU A PALAVRA\n           Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
                else:
                    letra = input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc8}
    Erros: {erros}

    Escolha uma letra: ''')
            elif(b == 4):
                if(palaEsc10 == texto):
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc10}
    Erros: {erros}

            PARABÉNS, VOCÊ ACERTOU A PALAVRA\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
                else:
                    letra = input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc10}
    Erros: {erros}

    Escolha uma letra: ''')
            elif(b == 5):
                if(palaEsc11 == texto):
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc11}
    Erros: {erros}

            PARABÉNS, VOCÊ ACERTOU A PALAVRA\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
                else:
                    letra = input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc11}
    Erros: {erros}

    Escolha uma letra: ''')
            else:
                print('    Essa opção ainda não existe!')

            acerto = False
            if(b == 1):
                for i in range(len(palaEsc4)):
                    if(letra.lower() == palaEsc4[i].lower()):
                        acerto = True
                        forca4[i] = palaEsc4[i]
                if(acerto == False):
                    vida += dif
                    erros += letra.upper()
            elif(b == 2):
                for i in range(len(palaEsc7)):
                    if(letra.lower() == palaEsc7[i].lower()):
                        acerto = True
                        forca7[i] = palaEsc7[i]
                if(acerto == False):
                    vida += dif
                    erros += letra.upper()
            elif(b == 3):
                for i in range(len(palaEsc8)):
                    if(letra.lower() == palaEsc8[i].lower()):
                        acerto = True
                        forca8[i] = palaEsc8[i]
                if(acerto == False):
                    vida += dif
                    erros += letra.upper()
            elif(b == 4):
                for i in range(len(palaEsc10)):
                    if(letra.lower() == palaEsc10[i].lower()):
                        acerto = True
                        forca10[i] = palaEsc10[i]
                if(acerto == False):
                    vida += dif
                    erros += letra.upper()
            elif(b == 5):
                for i in range(len(palaEsc11)):
                    if(letra.lower() == palaEsc11[i].lower()):
                        acerto = True
                        forca11[i] = palaEsc11[i]
                if(acerto == False):
                    vida += dif
                    erros += letra.upper()

            if(b == 1):
                if(vida >= 6):
                    os.system('cls')
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc4}
    Erros: {erros}

            Você perdeu. Mais sorte da próxima vez!\n\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
                
            elif(b == 2):
                if(vida >= 6):
                    os.system('cls')
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc7}
    Erros: {erros}

            Você perdeu. Mais sorte da próxima vez!\n\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
            elif(b == 3):
                if(vida >= 6):
                    os.system('cls')
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc8}
    Erros: {erros}

            Você perdeu. Mais sorte da próxima vez!\n\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
            elif(b == 4):
                if(vida >= 6):
                    os.system('cls')
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc10}
    Erros: {erros}

            Você perdeu. Mais sorte da próxima vez!\n\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
            elif(b == 5):
                if(vida >= 6):
                    os.system('cls')
                    input(f'''
    {arte[vida]}
    Palavra: {texto}
    Dica: {dicaEsc11}
    Erros: {erros}

            Você perdeu. Mais sorte da próxima vez!\n\n            Aperte ENTER para voltar ao painel principal!''')
                    os.system('cls')
                    break
            
    elif(d == '2'):
        input('''
 ----------------------------------------------
|                 Sobre o jogo:                |
|                                              |
|       O jogo da forca é um jogo em que o     |
|         jogador tem que acertar qual         |
|    é a palavra proposta, tendo como dica     |
|     o número de letras e o tema ligado       |
|                 à palavra.                   |
|     A cada letra errada, é desenhado uma     |
|         parte do corpo de um boneco.         |
|                                              |
|                                              |
|                  BOA SORTE!                  |
|                                              |
|                                              |
 ----------------------------------------------
 ''')
        os.system('cls')
    elif(d == '3'):
        input("     Aperte ENTER para sair do programa!\n\n")
        break
    else:
        print('     Essa opção ainda não foi adicionada!')
        input('     Aperte ENTER para fechar o programa!\n')
        break
