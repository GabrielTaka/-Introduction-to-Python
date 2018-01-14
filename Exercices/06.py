#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua
#tabuada.

num = int(input("Entre com um número: "))
a = 1
while(a<=10):
    x = num * a
    print("{} x {} = {}".format(num,a,x))
    a+=1
    
