#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o
#nome do escolhido.

import random
lista = []
a = 0
while(a<4):
    lista.append(str(input("Digite o nome do aluno: ")))
    a+=1
x = random.choice(lista)
print("{}".format(x))
