# Atividade 012
# Recebe o valor de um produto e aplica um desconto de 5%
produto = float(input('digite o valor do produto: '))
desc = 5/100 * produto
valor_final = produto - desc
print(f'O valor do produto com desconto é: R$ {valor_final:.2f}')
