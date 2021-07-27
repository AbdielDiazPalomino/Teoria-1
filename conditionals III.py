edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#tambien hay otra forma de acerlo, no es muy efectiva
#ya que es mas larga pero para tenerla en cuenta
#momento latam xD

"""
def mayor_edad(num):
    if num >= 18:
        return True
    else:
        return False

edad = input("Ingrese su edad: ")

if mayor_edad(int(edad)):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")