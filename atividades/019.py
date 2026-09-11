# Atividade 019
# Sorteando um dos alunos
import random
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
print(f'O aluno sorteado foi {random.choice([aluno1, aluno2, aluno3, aluno4])}')