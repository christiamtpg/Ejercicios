num1=int(input("ingresa un numero:"))
num2=int(input("ingresa un numero:"))
num3=int(input("ingresa un numero:"))

if num1 >= num2:
  if num1 >=num3:
    print("El número mayor es",num1)
elif num2 >= num1:
  if num2 >=num3:
    print("El número mayor es",num2)
  else:
    print("El número mayor es",num3)