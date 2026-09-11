# Atividade 013
# Recebe o valor do salário de um funcionário e aplica um aumento de 15%
salario = float(input('Digite o valor do seu salário: '))
aumento = salario + ( 15/100 * salario )
print(f'O valor do seu salário com aumento é: R$ {aumento:.2f}')