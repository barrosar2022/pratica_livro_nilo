salario = float(input('Digite o salário atual: '))
aumento = float(input('Digite o percentual do aumento: '))
valor_aumento = salario*aumento/100
salario = salario + valor_aumento
print('Valor do aumento: ',valor_aumento)
print('Novo salário: R$ ',salario)