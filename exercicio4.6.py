distancia = float(input())
preco = 0

if distancia <= 200:
    preco = preco + 0.5*distancia
else:
    preco = preco + 0.45*distancia

print(f'Preço da passagem: R${preco}')