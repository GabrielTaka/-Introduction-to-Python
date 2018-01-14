#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece
#a letra "A", em que posição ela aparece a primeira vez e em que posição ela
#aparece a última vez.

frase = str(input("Digite a frase desejada: ")).upper().strip()
count = frase.count("A")
print("A letra 'A' foi encontranda {} vezes".format(count))
count = frase.find("A")
print("A palavra 'A' apareceu pela primeira vez na posição",count + 1)
tam = len(frase)
x = 0
while (x < tam):
    if("A" in frase[x]):
        count = x
    x+=1
print("A plavra 'A' apareceu pela ultimavez na posição", count + 1)
        
