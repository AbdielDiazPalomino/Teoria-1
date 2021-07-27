
#así llamamos a un archivo y le ponemos la "r" para reading osea leerlo
el_txt_de_archivos = open("archivos texto.txt","r")


#y para imprimir el comando usamos .read para leerlo y aparesca
#en la pantalla todo el texto del archivo
print(el_txt_de_archivos.read())


#y ponemos readline para que se vea o imprima solo la primera linea
#print(el_txt_de_archivos.readline())


#acá hacemos que las líneas se combiertan en una lista
#y de esa manera podemos seleccionar la línea que queramos
#y el [3] es la línea del texto que queremos imprimir
#print(el_txt_de_archivos.readlines()[3])


#acá con write podemos agrgar cosas a nuestro texto
#pero tenemos que seleccionar "a" en vez de la "r"
#y al escribir ponerle \n para que salte de línea
"""
el_txt_de_archivos = open("archivos texto.txt","a")
print(el_txt_de_archivos.write("\nCarlos el grande = javita"))
"""


#ahora eliminaremos un archivo, pero python no tiene una funcion para eso
#entonces llamaremos a un modulo
"""
import os
os.remove("archivo que queremos eliminar.txt")
"""


el_txt_de_archivos.close() #así cerramos un archivo