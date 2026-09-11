# Aula 06 - tipos primitivos
# Video https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=10
# sem int
n1 = input('digite um numero: ')
n2 = input('digite outro numero: ')
soma = n1 + n2
print (f'a soma entre {n1} e {n2} é igual a {soma}')
# com int
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
soma = n1 + n2
print (f'a soma entre {n1} e {n2} é igual a {soma}')
# comvertendo float
n1 = float(input('digite um numero: '))
print (f'o numero digitado foi {n1}')
# usando.is 
n1 = input('digite algo: ')
print (n1.isnumeric())
print (n1.isalpha())
print (n1.isalnum())
print (n1.isupper())

