from biblioteca_3 import*
productos = ["A", "B", "C"]
ventas = [[50, 60, 70 ],
          [80, 55, 45],
          [40, 65, 75]]
seguir_usando_menu = True

while seguir_usando_menu:
    imprimir_menu_opciones()
    match pedir_numero_con_parametros("Selecciona una opcion del 1 al 5: ",1,5):
        case 1:
            imprimir_matriz(ventas,productos,suma_de_entero_filas(ventas))
        case 2:
            ordenar_descendentemente(suma_de_entero_filas(ventas),ventas,productos)
        case 3:
            imprimir_segun_posicion(buscar_posicion_de_string_en_lista(pedir_string("Dime cual es el producto: "),productos),ventas)
        case 4:
            imprimir_segun_posicion_trimestre_producto(buscar_posicion_de_entero_en_matriz(pedir_numero_con_parametros("Dime el monto de venta: ",0, 1000),ventas),productos)
        case 5:
            seguir_usando_menu = False