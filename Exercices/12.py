#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
#a sua porção Inteira.

from math import floor

num = float(input("Digite o número desejado: "))
print("A parte inteira do número {} é {}".format(num,floor(num)))

