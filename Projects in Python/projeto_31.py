#Faça um programa que leia o nome de uma pessoa, mostrando o primeiro e o ultimo nome semapradamente

nome = str(input('Insira o nome:')).strip()
nome = nome.split()
print('Seu primeiro nome:{}'.format(nome[0]))
print('Seu ultimo nome:{}'.format(nome[len(nome)-1]))
