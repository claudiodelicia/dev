"""
1- pegar a pontuação do aluno
2- verificar qual o conceito com base na pontuação 
3- exibir ao usuario o conceito obtido
"""


#recebe os dados do usuario
pontos = float(input("qual a pontuação do aluno"))

#faz a verificação 
if pontos >= 80 and pontos <=100:
    print("\no aluno tirou A na prova")
elif pontos >= 60 and pontos <=80:
    print("\no aluno tirou B na prova")
elif pontos >= 40 and pontos <=60:
    print("\no aluno tirou C na prova")
elif pontos >= 20 and pontos <=40:
    print("\no aluno tirou D na prova")
elif pontos >= 10 and pontos <=20:
    print("\no aluno tirou E na prova")
else:
    print("\no aluno tirou F na prova")