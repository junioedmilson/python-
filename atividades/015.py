# Atividade 015
# Aluguel de carro
# O preço do aluguel de um carro é R$ 60 por dia e R$ 0,15 por km rodado.
km = float(input('quantos km foram percorridos? '))
dias = int(input('por quantos dias o carro foi alugado? '))
preco = (60 * dias) + (0.15 * km)
print(f'O preço do aluguel do carro é R$ {preco:.2f} \nSendo R$ {60 * dias:.2f} referente aos dias e R$ {0.15 * km:.2f} referente aos km percorridos')