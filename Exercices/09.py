#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto.

preço = float(input("Entre com o preço do produto: "))
desconto = (preço * 5) / 100
preço = preço - desconto
print("O novo preço do produto será de {} com 5% de desconto!".format(preço))

