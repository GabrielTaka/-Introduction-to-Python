#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
#primitivo e todas as informações possíveis sobre ele.


num = input("Digite algo: ")
x = type(num)
print("{}".format(x))
print('É um número? ', num.isnumeric())
print('É só espaço?', num.isspace())
print("É só letra maiuscula?",num.isupper())
print("É só letra minuscula? ", num.islower())
