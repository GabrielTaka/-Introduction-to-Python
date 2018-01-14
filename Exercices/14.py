#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse ângulo.

import math

num = float(input("Digite o angulo desejado: "))
x1 = math.cos(math.radians(num))
x2 = math.sin(math.radians(num))
x3 = math.tan(math.radians(num))
print("O cosseno de {} é {:.2f}".format(num,x1))
print("O seno de {} é {:.2f}".format(num,x2))
print("A tangente de {} é {:.2f}".format(num,x3))
