days = {"lu": "Lunes", "ma": "Martes", "mi": "Miércoles"}

#acá le decimos que para clave y valor en la variable days me de los items
#clave sería lu, ma, mi y valor lunes, martes, miercoles
for clave, valor in days.items():

    #por eso acá podemos imprimir (clave) o (valor) e incluso los 2
    #con (clave, valor)
    print(clave)

"""
#for es el comando, cosas es la variable q creamos
for cosas in range(1,11):
    #en este print decimos q nos ponga el numero de la variable cosas
    #Luego ponemos el * como texto solo para q lo ponga, igual que el =
    #y luego ponemos cosas*2 para el resultado
    print(cosas, "*", 2, "=", cosas*2)
    print(cosas)

"""