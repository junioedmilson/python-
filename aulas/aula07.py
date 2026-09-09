# aula 07 Operadores Aritméticos
# video https://www.youtube.com/watch?v=Vw6gLypRKmY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=13
# adição, subtração, multiplicação, divisão, divisão inteira, potência, resto da divisão, raiz quadrada
n1 = int(input('diga um numero: '))
n2 = int(input('diga outro numero: '))
adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
potencia = n1 ** n2
resto_da_divisao = n1 % n2
raiz_quadrada = n1 ** (1/2)
print (f' a adição entre {n1} + {n2}  = {adicao} \n a subtração entre {n1} - {n2}  = {subtracao} \n a multiplicação entre {n1} * {n2}  = {multiplicacao} \n a divisão entre {n1} / {n2}  = {divisao} \n a divisão inteira entre {n1} // {n2}  = {divisao_inteira} \n a potência entre {n1} ** {n2}  = {potencia} \n o resto da divisão entre {n1} % {n2}  = {resto_da_divisao} \n a raiz quadrada de {n1}  = {raiz_quadrada}')
# stings
print ('oi' * 5)
print ('oi' + 'tudo bem?')
nome = input('qual é o seu nome? ')
print (f'prazer em te conhecer {nome:=^20}!')
print (f'prazer em te conhecer {nome:-<20}!')
print (f'prazer em te conhecer {nome:->20}!')
