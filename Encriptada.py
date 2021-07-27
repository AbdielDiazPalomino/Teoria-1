#acá vamos a encriptar mensajes, porq somos hackers y refacheros xD

caracter_elegido = input("Inserte caracter para encriptar: ")

def encriptar(frase, caracter):
    encriptada =""
    for letra in frase:
        if letra.lower() in "aeiouáéíóú":
            if letra.isupper():
                encriptada = encriptada + caracter.upper()
            else:
                encriptada = encriptada +caracter
        else:
            encriptada = encriptada + letra
    return encriptada

while True:
    print(encriptar(input("Ingresa una frase: "), caracter_elegido))

    print("Ingresa (1) para encriptar otra frase")
    print("Y (2) para finalizar")
    opcion = int(input("Seleccione 1 o 2: "))

    if opcion == 2:
        break
        