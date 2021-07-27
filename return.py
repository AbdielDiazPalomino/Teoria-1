#es verdad que no necesariamente tenemos que
#escribir return para imprimir esa operación
#pero el return no solo sirve para imprimir esos valores 
#sino tambien para tenerlos ahí pero no imprimirlos
#como el daño de ataque de un personaje en un videogame.
#o para hacer operaciones como esta

#acá le estamos diciendo que numero es mayor
#utilizando el return
"""
def num_mayor (n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

print(num_mayor(100,20,3000))
"""

def multi(num1, num2):
    return num1 * num2

resol = multi(5, 2)
print(resol)