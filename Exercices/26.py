# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o
#preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
#para viagens mais longas.

km = int(input("Digite a distância da viagem em km: "))
if(km <= 200):
    preço = km * 0.50
    print("A viagem irá lhe custar R$:",preço)
else:
    preço = km * 0.45
    print("A viagem irá lhe custar R$:",preço)
