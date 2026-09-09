# Atividade 013
# Recebe o valor do salário de um funcionário e aplica um aumento de 15%
salario = float(input('Digite o valor do seu salário: '))
aumento = 15/100 * salario
v_final = salario + aumento
print(f'O valor do seu salário com aumento é: R$ {v_final:.2f}')