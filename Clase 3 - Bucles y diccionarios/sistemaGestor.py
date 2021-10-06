####### Declaramos nuestro diccionario de productos ######
codigos = [143,568,991,321]
#Almacenamos los códigos de los productos presentes en el almacén
#A continuación, construimos una lista de tuplas para almacenar dos datos en cada una de sus posiciones
# el nombre y el precio de producto.
# Hay que prestar especial atención al hecho de que DENTRO de la lista "nombresPrecios" hay otras tuplas, cada unas de las cuales
#contiene la información requerida
nombresPrecios = [("Disco rígido SSD",5000), ("Mouse inalámbrico",800), ("Teclado bluetooth",1000), ("Memoria 8GB",5000)]
#Cuando vemos datos entre paréntesis, separados por comas, son TUPLAS
#Luego, vamos a crear un diccionario que guarde pares "clave valor"
#Como nos interesa asociar una correspondencia entre el CÓDIGO de cada producto, su NOMBRE y su PRECIO
#necesitamos que nuestro diccionario se genere a partir de la lista "códigos" y la lista "nombresPrecios"
#Utilizaremos para este fin la función "zip" combinada con "dic"
datos = dict(zip(codigos, nombresPrecios))
# datos {143: ("Disco rígido SSD",5000), 568: ("Mouse inalámbrico",800)}
#Esto nos ha generado un diccionario que tiene, como claves, todos los elementos de la lista "códios"
# y como valores asociados, las tuplas (descripción, valor)

pedido = [] 
#Esta lista vacía será  utilizada para almacenar los diferentes artículos
#que el usuario quiera pedir
print(" ---- Programa gestor de pedidos ---- ")
nombre = input("Por favor, ingrese su nombre...")
print("Estimado " , nombre , " a continuación confeccionaremos su lista de pedidos.")

#Vamos a imprimir los productos de los que disponemos para que el usuario pueda elegir cuáles
# quiere agregar a la lista de pedidos
# Para controlar el ingreso de productos, le solicitaremos al usuario que ingrese el código del producto
# que desea agregar al pedido o, si ya no quiere aregar más artículos, el valor -1
#Recuperamos las claves del diccionario, mostrando los codigos. De éstos deberá elegir el usuario.
cods = list(datos.keys()) 
#Advertir que los convertimos a listaK

# Para comenzar la repetición correctamente, inicializaremos la variable "codigo" en un valor DIFERENTE a -1
# Esto servrirá para que el bucle WHILE comience su ejecución la primera vez.
codigo = -2

#while(True):
#    codigo = int(input("¿Qué código desea agregar al pedido? (Ingrese -1 para finalizar)"))
#    if(codigo == -1):
#        break


while(codigo!=-1) :
    print("Lista de códigos disponibles para agregar:")

    #Imprimimos ahora la lista de códigos de los cuales puede el usuario elegir los que desee agregar
    # utilizando un bucle
    for i in range(len(cods)) :
        print(cods[i])
    codigo = int(input("¿Qué código desea agregar al pedido? (Ingrese -1 para finalizar)"))
    #Si el codigo ingresado es "-1", no debemos considerar el producto dado que significa que el usuario
    #quiere terminar con el programa
    #Caso contrario, hay que agregar el precio y el nombre del producto que tenga el codigo elegido
    # a la lista de pedidos
    # Para hacerlo, vamos a recuperar el valor asociado a la clave elegida del diccionario
    if(codigo!=-1):
        datosAInsertar = datos.get(codigo)
        pedido.append(datosAInsertar)
        print("Producto cargado con éxito")
    #Recordar que este código se repitea una y otra vez hasta que el usuario ingresa "-1"
    print("----------------------------------------")

#Finalmente, vamos a imprimir por pantalla los productos que incluyó en el pedido

print("Tu pedido consiste de: ")
for elemento in pedido:
    #pedido = [('Disco rígido SSD',5000),('Teclado bluetooth',3000)]
    #elemento[0] es nombre
    #elemento[1] es precio
    #Esto sucede porque en la lista "pedido" nosotros cargamos TUPLAS (nombre, precio)
    print("Nombre del producto: ", elemento[0], " | Precio: ", elemento[1])


#Recuperamos las claves del diccionario, mostrando los codigos. De éstos deberá elegir el usuario.
cods = list(datos.keys()) 
#Advertir que los convertimos a listaK

# Para comenzar la repetición correctamente, inicializaremos la variable "codigo" en un valor DIFERENTE a -1
# Esto servrirá para que el bucle WHILE comience su ejecución la primera vez.
