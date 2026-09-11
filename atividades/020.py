# Atividade 020
# sortear orden de apresentacao de trabalhos
import random
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
random.shuffle( alunos := [aluno1, aluno2, aluno3, aluno4])
print(f'A ordem de apresentação é: {alunos}')