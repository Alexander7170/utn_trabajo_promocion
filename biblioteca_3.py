def imprimir_menu_opciones(): 
    # Imprimira el menu de opciones con un cierto orden usando el \n
    print("---Menu de opciones---\n 1   Mostrar Productos y ventas \n 2   Ordenar productos por ventas anuales \n 3   Buscar Producto por nombre \n 4   Buscar monto de venta en la matriz \n 5   salir ")

def imprimir_matriz(matriz_a_imprimir:list, Lista_productos:list,Total_suma:list,):
     #Imprimira como encabezado el tipo de dato
    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("Producto", "Trimestre 1", "Trimestre 2", "Trimestre 3", "Total" ))
    # imprimira en primer elemento que hay en la lista productos,
    # Ademas tambien imprimira, de la matriz: el elemento 0,1 y 2 de la lista i
    # Por ultimo imprimira los elementos de la lista Total_suma
    for i in range(len(Lista_productos)):
        print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(Lista_productos[i] , matriz_a_imprimir[i][0], matriz_a_imprimir[i][1], matriz_a_imprimir [i][2], Total_suma[i] ))

def imprimir_segun_posicion(posicion:int,matriz_ventas:list):
    # Si posicion es un numero, imprimira usando como fila, la referencia posicion, en la matriz ventas
    # todos las columnas con la mismo valor de fila. Si posicion no es entero, entonces imprimira que no existe tal producto
    if posicion == None:
        print("No existe ese producto")
    else: 
        print("El primer trimestre tuvo ventas de: ", matriz_ventas[posicion][0], "El segundo trimestre tuvo ventas de ", matriz_ventas[posicion][1],"El tercer trimestre tuvo ventas de ", matriz_ventas[posicion][2])

def imprimir_segun_posicion_trimestre_producto(posiciones:list, lista_productos:list):
    # Si el conteo de elementos de la lista posiciones es 0
    # significa que no habia encontrado la posicion de ese elemento en aquella matriz en la que se busco
    if len(posiciones) == 0:
        print("Ese monto de venta no existe")
    #si se encontro, el primer elemento seria la fila, osea el producto
    # el segundo elemento seria la columna, osea el trimestre
    else:
        print("El producto es: ", lista_productos[posiciones[0]], ", venta del trimestre", posiciones[1] + 1)

def pedir_numero_con_parametros(mensaje:str, desde:int, hasta:int)->int:
    # El mensaje es para informarle al usuario los parametros.
    # obligara a que el numero que el usuario no tire este dentro de los parametros y lo retornara 
    numero = int(input(mensaje))
    while numero < desde or numero > hasta:
        numero = int(input("No puse un numero dentro de lo pedido," + mensaje))
    return numero

def pedir_string(mensaje:str)->str:
    # Pedir una cadena de caracteres, un producto en este caso. Lo que nos tire el usuario lo retornaremos
    producto = input(mensaje)
    return producto

def suma_de_entero_filas(matriz:list)->list:
    # Itero la matrix y cada vez que j itera las listas de la matriz, suma el elemento a la variable Acumulador
    # asi de esa manera tengo la suma de una fila entera, esa suma lo añado a la lista lista_con_las_sumas
    # y antes de que vuelva a iterar i, reinicio la varible acumulador a su valor original.
    acumulador = 0
    lista_con_las_sumas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            acumulador += matriz[i][j]
        lista_con_las_sumas.append(acumulador)
        acumulador = 0
    return lista_con_las_sumas

def buscar_posicion_de_string_en_lista(producto:str, lista_a_buscar:list)->any:
    # Itera lista_a_buscar y si encuentra un elemento que sea igul a la referencia producto
    # Reemplazara la variable posicion por la ubicacion de ese elemento y lo retornara
    posicion = None
    for i in range(len(lista_a_buscar)):
        if producto == lista_a_buscar[i]:
            posicion = i
            break
    return posicion

def buscar_posicion_de_entero_en_matriz(valor_de_venta:int, matriz_a_buscar:list)->list:
    # itera matriz_a_buscar, es una matriz por lo tanto lo que retornara es una lista
    # con su fila y columna del valor_de_venta. Si encuentra un elemento que sea igual a valor_de_venta
    # lo añadira a la variable_posicion su fila y columna, luego se retorna eso
    posicion = []
    for i in range(len(matriz_a_buscar)):
        for j in range(len(matriz_a_buscar[i])):
            if valor_de_venta == matriz_a_buscar[i][j]:
                posicion.append(i)
                posicion.append(j)
                break
    return posicion


def ordenar_descendentemente(lista_ventas_anuales:list, ventas:list, lista_productos:list):
    #itera lista_ventas_anuales y compara sus propios elementos
    # siguiendo un criterio que ordenara de mayor a menor
    # si ese criterio es verdadero, intercambiara las posiciones de dos elementos
    #Asi hasta el ultimo elemento, quedando finalmente el primer elemento como el mas grande,
    # paralelamente tambien intercambiara la lista ventas y la lista_productos siguinedo el criterio dicho antes
    for i in range(len(lista_ventas_anuales)- 1):
        for j in range(i + 1, len(lista_ventas_anuales)):
            if lista_ventas_anuales[i] < lista_ventas_anuales[j]:
                aux = lista_ventas_anuales[i] #swapeo
                lista_ventas_anuales[i] = lista_ventas_anuales[j]
                lista_ventas_anuales[j] = aux
                aux = ventas[i]
                ventas[i] = ventas[j]
                ventas[j] = aux
                aux = lista_productos[i]
                lista_productos[i] = lista_productos[j]
                lista_productos[j] = aux
