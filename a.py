import random
import os
a = "=-"*10+"="
print(f"{a}  Acerte a palavra  {a}")

p4 = ['Urso', 'Caos', 'Vida', 'Auto', 'Doce']
p7 = ['Celular', 'Abóbora', 'Etienne', 'Empatia', 'Família']
p8 = ['Capivara', 'Suricato', 'Panelada', 'Nintendo', 'Educação']
p10 = ['Computador', 'Comparador', 'Dicionário', 'Maturidade', 'Referência']
p11 = ['Playstation', 'Perspectiva', 'Dissimulado', 'Compreensão', 'Preconceito']



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
print(p)
print(text)

