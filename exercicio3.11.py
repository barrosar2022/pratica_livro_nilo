preco = float(input('Digite o preço de uma mercadoria: R$: '))
desconto = float(input('Digite o percentual do desconto: '))
valor_desconto = desconto/100*preco

preco = preco - valor_desconto

print('Valor do desconto: R$: ',valor_desconto)
print('Novo preço: R$: ',preco)