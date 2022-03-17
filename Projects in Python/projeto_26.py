# desafio 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas
# o nome com todas minusculas
# Quantas letras(sem os espaços)
# quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo:'))
print(nome.upper())
print(nome.lower())
print('O nome completo possui {} letras.'.format(len(nome.strip())))
pn = nome.split()
print('O primeiro nome possui {} letras.'.format(len(pn[0].strip())))
