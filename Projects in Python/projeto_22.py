#desafio 019
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random

no1 = str(input('Insira o nome do 1° aluno:'))
no2 = str(input('Insira o nome do 2° aluno:'))
no3 = str(input('insira o nome do 3° anulo:'))
no4 = str(input('insira o nome do 4° anulo:')) 
lista = [no1,no2,no3,no4]
als = random.choice(lista)
print('O aluno escolhido foi {}'.format(als))



 