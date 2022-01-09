consumo = float(input('Qual o consumo em kWh? '))
tipo = input('Qual o tipo de instalção?'+'\n'+ 'R - Residencial'+'\n'+'I - Industrial'+'\n'+'C - Coméricos')

if tipo == 'R':
    if consumo <= 500:
        preco = consumo*0.4
    else:
        preco = consumo*0.5
if tipo == 'C':
    if consumo <= 1000:
        preco = consumo*0.55
    else:
        preco = consumo*0.6
if tipo == 'I':
    if consumo <= 5000:
        preco = consumo*0.55
    else:
        preco = consumo*0.6
    
print(f'Preço a ser pago R$: {preco}')