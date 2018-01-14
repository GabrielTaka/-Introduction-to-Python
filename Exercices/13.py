#grama que leia o comprimento do cateto oposto e do cateto adjacente de um
#triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
cat1 = float(input("Insira o tamanho do cateto adjacente: "))
cat2 = float(input("Insira o tamanho do cateto oposto: "))

cat1 = math.pow(cat1,2)
cat2 = math.pow(cat2,2)
h = cat1 + cat2
h = math.sqrt(h)

print("O comprimento da hipotenusa é de {:.2f}".format(h))
