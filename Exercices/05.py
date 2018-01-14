#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
#mostre quantos dólares ela pode comprar.


m = float(input("Digite o tamanho em metros: "))
cem = m * 100
mil = m * 1000
print("A medida {} em metros é {:.2f} em centímetros".format(m,cem))
print("A medida %.2f em metros é %.2f em milímetros" %(m, mil))
