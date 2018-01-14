#Faça um programa que leia a largura e a altura de uma parede em metros, calcule
#a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
#litro de tinta pinta uma área de 2 metros quadrados.

altura = int(input("Digite a altura da parede: "))
largura = int(input("Digite a largura da parede: "))
perimetro = altura * largura
latas = perimetro / 2
if(perimetro%4==0):
    print("A quantidade de latas será de: {}".format(latas))

else:
    print("A quantidade de latas será de: %d" %(latas +1))
