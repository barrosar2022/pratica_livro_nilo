cigarros_dia = int(input('Quantos cigarros por dia? '))
anos = int(input('Quantos anos foi fumante? '))

# 1 ano = 365 dias = 525600 minutos
# 1 cigarro = 10 min a menos de vida

vida = anos*525600 + cigarros_dia*10

dias = vida/1440

print('Dias a menos de vida: ',dias)