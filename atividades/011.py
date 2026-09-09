# Atividade 011
# Recebe a altura e largura de uma parede e calcula a quantidade de tinta necessária para pintá-la
# Supondo que 1 litro de tinta pinta 2 metros quadrados
altura = float(input('digite a altura da parede: '))
largura = float(input('digite a largura da parede: '))
area = altura * largura
print(f' A quantudade de tinta necessaria para pintar a parede e {area /2 :.2f} litros')