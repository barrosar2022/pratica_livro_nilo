valor = float(input('Qual o valor da casa? R$: '))
salario = float(input('Qual o salário do cliente? R$: '))
parcelas = int(input('Quantos anos de pagamento? '))
meses = parcelas*12
prestacao = valor/meses
limite = 0.3*salario
if prestacao <= limite:
    print('Emprestimo aprovado!')
    print(f'Valor da prestação R$: {prestacao}')
else:
    print('Emprestimo não autorizado!')
    print(f'Prestação calculada: R${prestacao}')
    print(f'Valor da prestação deve ser abaixo de R$: {limite}')