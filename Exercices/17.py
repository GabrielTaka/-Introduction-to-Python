# Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo
#(sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo: ")).strip()
print('Nome com todas as letras minusculas: {}'.format(nome.upper()))
print('Nome com todas as letras maiusculas: {}'.format(nome.lower()))
tamanho = len(nome)
space = nome.count(' ')
tamanhofinal = tamanho - space
print("A palavra tem o tamanho de: {}".format(tamanhofinal))
separa = nome.split()
print("O seu primeiro nome tem {} letras".format(len(separa[0])))
