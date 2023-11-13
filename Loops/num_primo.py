numero= int(input("Digite un numero: "))
divisible= False

for n in range(2,numero-1):
    if numero%n ==0:
        print("No es primo, es divisible por", n )
        divisible= True
        break
if divisible == False:
    print("El número es primo.")