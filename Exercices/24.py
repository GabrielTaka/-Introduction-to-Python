#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
#R$7,00 por cada Km acima do limite.

speed = float(input("Insira a sua velocidade: "))
if(speed > 80):
    multa = (speed - 80) * 7.00
    print("A multa foi de R${}".format(multa))
else:
    print("Você não foi multado!")
