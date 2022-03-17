#desafio 020
#O memso professor do desafio anterior qier sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

a1 = str(input('Insira o nome do 1° aluno:'))
a2 = str(input('insira o nome do 2° aluno:'))
a3 = str(input('insira o nome do 3° aluno:'))
a4 = str(input('insira o nome do 4° aluno:'))

li = [a1,a2,a3,a4]

random.shuffle(li)

print('A ordem de apresentação será \n {}' .format(li))
