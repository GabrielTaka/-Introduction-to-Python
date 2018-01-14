# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com
#o nome "SANTO".

nome = str(input("Digite o nome da sua cidade: ")).upper().strip()
nome = nome.split()

if("SANTO" in nome[0]):
    print("Sim, o nome de sua cidade começa com a palavra SANTO")
