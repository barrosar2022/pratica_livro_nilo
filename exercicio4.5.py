salario = float(input())
aumento = 0
if salario >= 1250:
    aumento = 0.1*salario
    salario = salario + aumento
else:
    aumento = 0.15*salario
    salario = salario + aumento

print(f'Novo salário {salario}')