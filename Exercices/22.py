#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
#primeiro e o último nome separadamente.

nome = str(input("Digite o seu nome completo: ")).strip().split()
tam = len(nome)
print(nome)
print(tam)
print("O seu primeiro nome é:",nome[0])
print("O seu ultimo nomé:", nome[tam-1])
