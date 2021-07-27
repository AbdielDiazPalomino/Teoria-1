#acá importamos un modulo que instalamos con pip instal colorama, en la consola cmd
#y ya podemos poner colores a la letra, y 
#podemos enrtar a pypi.org para sacar mas modulos
from colorama import Fore, Style, init 
init(convert=True)
print(Fore.RED + "Abdiel es genial")