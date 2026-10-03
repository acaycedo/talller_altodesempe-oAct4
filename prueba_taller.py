#Variable declarada como entero que sera el numero de registros que tendra la base de datos.
print("Ingrese la cantidad de registros que va almacenar:")
N = int(input())

#Se crea una lista que almacenara los registros.
db = []

#Un bucle que repite N veces el proceso. Una vez por registro
for i in range(N):
    #c con cada repetición recibira un input del usuario separados por espacios que representan las diferentes características de las ruedas
    print("Ingrese los parametros de los patines: ")
    c=input() 
    #Por cada " " que encuentre separa esa linea, para hacer una cadena de Strings
    db.append(c.split(' ')) #Luego añade esa cadena en el orden que ingresaron a la base de datos "db"

# Parámetros descriptivos establecidos por el reglamento.
diam_min = 100       # Diámetro mínimo.
diam_max = 120       # Diámetro máximo.
grosor_min = 70      # Grosor mínimo.
grosor_max = 80      # Grosor máximo.
ancho_min = 90       # Ancho mínimo.
ancho_max = 110      # Ancho máximo.

#Establece la disponibilidad como ningún registro cumple las condiciones
disponibilidad=False 

# Lista encargada de almacenar los precios de los diseños
exito=[]


# Bucle que recorre cada uno de los registros en la "db"
for i in range(N):

    # Variables que almacenan el dato correspondiente que ingreso el usuario.
    # De esta manera hacer condicionales resulta ser mas facil de leer por si en un futuro hay que actualizar los parámetros
    # y el programador no tenga problemas para entender la lógica.
    diametro = int(db[i][0])
    grosor = int(db[i][1])
    ancho = int(db[i][2])
    precio = int(db[i][3])

    # Condicional que evalua si cada registro del usuario esta dentro de los parámetros del reglamento.
    if (
        # Evalua si el diametro es mayor o igual al minimo
        diametro >= diam_min
        # Evalua si el diametro es menor o igual al maximo
        and diametro <= diam_max
        # Evalua si el grosor es mayor o igual al minimo
        and grosor >= grosor_min
        # Evalua si el grosor es menor o igual al maximo
        and grosor <= grosor_max
        # Evalua si el ancho es mayor o igual al minimo
        and ancho >= ancho_min
        # Evalua si el ancho es menor o igual al maximo
        and ancho <= ancho_max
    ):
        # Procede almacenar el precio una vez comparo los registros
        exito.append(precio)
        # y una vez se completo la validación, cambia la disponibilidad.
        disponibilidad = True

#Compara si ningún diseño cumplio los requerimientos
if not disponibilidad: 
    print ("NO DISPONIBLE") # Muestra el mensaje
    # Si existe al menos un diseño que cumpla
else:
    # Recorre la lista con el bucle
    for precio in exito: 
        print(precio) # e imprime el resultado



    #CODIGO ORIGINAL
    # primero establece como entero el registro, compara la posicion en la lista con el parametro deseado, y determina si esta en el rango.
    # Es entendible pero quise hacerlo de otra manera ya que me parecia poco entendible para alguien que no conociera el contexto o entrara a revisar el codigo sin una buena documentacion
    # if (
    #     (int(db[i+1][0]) >= parametros[0])
    #     and (int(db[i+1][0]) <= parametros[1])
    #     and (int(db[i+1][1]) >= parametros[2])
    #     and (int(db[i+1][1]) <= parametros[3])
    #     and (int(db[i+1][2]) >= parametros[4])
    #     and (int(db[i+1][2]) <= parametros[5])):
        
        # exito.append(int(db[i+1][3])) 
        # disponibilidad = True 