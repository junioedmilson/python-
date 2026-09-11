# Atividade 017
# Calculando a hipotenusa
import math
co = float(input('digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'o comprimento da hipotenusa e {h:.2f}')
