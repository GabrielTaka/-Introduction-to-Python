#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
#salário, com 15% de aumento.

salario = float(input("Digite o seu salário: "))
aumento = (15*salario)/100
salario = salario + aumento
print("O seu salário com reajuste será de: {}".format(salario))
