#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
#dígitos separados.

num = str(input("Digite um número de 0 a 9999: "))
print('Analisando o número!')
x = 0
tam = len(num)
while(x<tam):
    print("O {}° número é: {}".format(x+1,num[x]))
    x+=1
