#En esta operación damos un numero con el input, luego lo dividimos
#pero si es un numero flotante o decimal no lo podemos dividir
#y en vez que nos salga error del sistema con el except nos sale
#el error que nosotros escribimos momento hackerman

try:
    num1 = int(input("Ingresa un número: "))
    num2 =2
    print(num1)
    print(num1/num2)
except:
    print("Entrada inválida, debe ser un entero")
