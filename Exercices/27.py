#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
if(n1 > n2) and (n2 > n3):
    print("A ordem será: {},{},{}".format(n1,n2,n3))
