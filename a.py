import random
import os
# os.system('cls')
a = "=-"*10+"="


p4 = ['Urso', 'Caos', 'Vida', 'Auto', 'Doce']
p7 = ['Celular', 'Abóbora', 'Etienne', 'Empatia', 'Família']
p8 = ['Capivara', 'Suricato', 'Panelada', 'Nintendo', 'Educação']
p10 = ['Computador', 'Comparador', 'Dicionário', 'Maturidade', 'Referência']
p11 = ['Playstation', 'Perspectiva', 'Dissimulado', 'Compreensão', 'Preconceito']


while True:
    print(f"{a}  Acerte a palavra  {a}")
    b = int(input("""
 ----------------------------------------------
|    Digite um número de 1 a 5:                |
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
"""))
    text = ''

    if(b == 1):
      p = p4[random.randint(0, len(p4)-1)]
      for i in range(len(p)):
        text += '_ '
      print(text)
      if(p == 'Urso'):
          print("\nDica: Animal")
          input()
      elif(p == 'Caos'):
          print("\nDica: Situação")
          input()
      elif(p == 'Vida'):
          print("\nDica: S2")
          input()
      elif(p == 'Auto'):
          print("\nDica: Altura")
          input()
      elif(p == 'Doce'):
          print("\nDica: Gosto/Comida")
          input()
      
      

      
    elif(b == 2):
      p = p7[random.randint(0, len(p7)-1)]
      for i in range(len(p)):
        text += '_ '
      print(text)
      if(p == 'Celular'):
          print("\nDica: Eletrônico")
          input()
      elif(p == 'Abóbora'):
          print("\nDica: Comida")
          input()
      elif(p == 'Etienne'):
          print("\nDica: Nome")
          input()
      elif(p == 'Empatia'):
          print("\nDica: Sentimento")
          input()
      elif(p == 'Família'):
          print("\nDica: Pais")
          input()
      

      
    elif(b == 3):
      p = p8[random.randint(0, len(p8)-1)]
      for i in range(len(p)):
        text += '_ '
      print(text)
      if(p == 'Capivara'):
          print("\nDica: Animal")
          input()
      elif(p == 'Suricato'):
          print("\nDica: Animal")
          input()
      elif(p == 'Panelada'):
          print("\nDica: Tipo de Protesto")
          input()
      elif(p == 'Nintendo'):
          print("\nDica: Desenvolvedora de Jogos")
          input()
      elif(p == 'Educação'):
          print("\nDica: Ensino")
          input()
      


      
    elif(b == 4):
      p = p10[random.randint(0, len(p10)-1)]
      for i in range(len(p)):
        text += '_ '
      print(text)
      if(p == 'Computador'):
          print("\nDica: Eletrônico")
          input()
      elif(p == 'Comparador'):
          print("\nDica: Compara")
          input()
      elif(p == 'Dicionário'):
          print("\nDica: Palavras")
          input()
      elif(p == 'Maturidade'):
          print("\nDica: Crescimento")
          input()
      elif(p == 'Referência'):
          print("\nDica: ??")
          input()
      


      
    elif(b == 5):
      p = p11[random.randint(0, len(p11)-1)]
      for i in range(len(p)):
        text += '_ '
      print(text)
      if(p == 'Playstation'):
          print("\nDica: Desenvolvedora de Jogos")
          input()
      elif(p == 'Perspectiva'):
          print("\nDica: Ponto de Vista")
          input()
      elif(p == 'Dissimulado'):
          print("\nDica: ??")
          input()
      elif(p == 'Compreensão'):
          print("\nDica: Entendimento")
          input()
      elif(p == 'Preconceito'):
          print("\nDica: ??")
          input()
      

      
    else:
        print("Essa opção não existe ou ainda não foi incrementada!")
        input()
        break
    os.system('cls')

print('oi')
input()
