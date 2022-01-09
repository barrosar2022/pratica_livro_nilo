A = int(input("Diga um número: "))
B = A
Resultado = 1
print("{}! =" .format(A) ,end = ' ') 
for numero in range (1,A + 1) :
  if B > 0 :
    print("{}" .format(B) ,end = ' ')
  if B > 1 :
    print("x" ,end = ' ')
  Resultado *= B
  B = B - 1
print("=" ,Resultado ,end = ' ')