#acá creamos una función llamada "hello"
def hello(name="Invitado"):
    print("Hola " + name)

hello("Abdiel")
hello("Jorge")
hello()

numero1 =int(input("Numero1: "))
numero2 =int(input("Numero2: "))
def add(numero1, numero2):
    return numero1 + numero2
print(add(numero1, numero2))