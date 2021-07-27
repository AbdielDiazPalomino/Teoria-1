r = list(range(1, 101))

colors = ["rojo", "azul", "celeste", "verde"]

#aquí ponemos los numeros como texto, pero no son numeros
#o valores enteros como tales.
numbers = ["1", "2", "3"]

#con esta forma el sistema si los reconoce como numeros.
numeros = list((1, 3, 5))

#print(r)
#print(colors)
#print(numeros)

#acá vemos si el elemnto "xd" está en la lista de la varialble colors.
#print ("xd" in colors)

#acá reemplazamos el valor 3 de la variable colors
colors[3]= "abdiel es el mejor"

#acá agregamos a la lista con el comando append, pero solo se puede agrgar una.
#colors.append("pos si cierto")

# NO SE PUEDE USAR APPEND Y EXTEND JUNTOS SOLO EXPEND AGREGAR PARA VARIOS 
#ELEMENTOS A LA LISTA Y APPEND PARA UN SOLO ELEMENTO
#acá con el metodo extend logramos agrgar 2 o mas elementos a la lista.
#ES UN METODO YA QUE TIENE UN PUNTITO
colors.extend(("yes sure","jaja xd"))

#acá insertamos un texto y ponemos la posición donde queremos
#que esté, pero no reemplaza, sino que se agrega.
colors.insert(1, "124 IQ")

#este comando hace que se quite un elemento de la lista
#un elemento que nosotros elegimos.
colors.remove("celeste")

#este comando hace que se elimine todos los elementos
#de la variable "colors"
#colors.clear()

#este comando ordena los elementos alfabeticamente
#colors.sort()

#este comando ordena los elementos alfabeticamente pero al revés.
#recuerda poner True con mayúscula la "T"
#colors.sort(reverse=True)

print(colors)