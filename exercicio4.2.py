velocidade = float(input('Digite a velocidade do carro: '))
multa = 0
if velocidade > 80:
    print('Você foi multado!')
    multa = 5*(velocidade - 80)
    print(f'Valor da multa R$: {multa} reais')

print('fim do programa')

