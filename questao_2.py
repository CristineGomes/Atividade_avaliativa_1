salario_fixo = float(input('Conte-nos seu salário fixo: R$'))
valor_vendas = float(input('Quanto você vendeu? R$'))

if valor_vendas <= 1500:
    bonus_total = valor_vendas * 0.05

else:
    bonus_1 = 1500 * 0.05
    bonus_2 = (valor_vendas - 1500) * 0.07
    bonus_total = bonus_1 + bonus_2

salario_final = salario_fixo + bonus_total

print(f'Seu salário final será: R${salario_final:.2f}.')