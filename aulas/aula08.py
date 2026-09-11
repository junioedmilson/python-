# Aula 08 - Utilizando Módulos
# Vídeo https://www.youtube.com/watch?v=oOUyhGNib2Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=25
# math
import math
num = int(input('Digite um número: '))
print(f'A raiz quadrada é {math.sqrt(num):.2f}')
print(f'Arredondando para cima {math.ceil(num)}')
print(f'Arredondando para baixo {math.floor(num)}')
print(f'O valor de {num} elevado a 2 é {math.pow(num, 2)}')
print(f'o fatorial de {num} é {math.factorial(num)}')
# Random
import random 
num1 = random.randint(1, 10)
print(f'{num1}')