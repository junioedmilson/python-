# Atividade 012
# Recebe o valor de um produto e aplica um desconto de 5%
produto = float(input('digite o valor do produto: R$ '))
desc = produto - (5/100 * produto)
print(f'O valor do produto com desconto é: R$ {desc:.2f}')