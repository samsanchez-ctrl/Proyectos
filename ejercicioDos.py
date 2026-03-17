# Simulacion de tienda
# 1. El "Almacen": Una lista vacia donde guardare diccionarios
inventario = []

while True:
    print("\n--- SISTEMA DE GESTION DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4: Salir")

    opcion = input("\nSelecciona una opcion (1-4): ")

    if opcion == "1":
        # --- AÑADIR PRODUCTO ---
        nombre = input("Nombre del producto: ")
        # Convertir a float e int porque input() siempre devuelve texto
        precio = float(input("Precio: "))
        stock = int(input("Cantidad inicial en stock: "))

        # Crear un "paquete" (diccionario) para el producto
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }

        # Se guarda en la lista maestra
        inventario.append(nuevo_producto)
        print(f" ¡{nombre} añadido con exito!")

    elif opcion == "2":
        # --- MOSTRAR INVENTARIO ---
        if len(inventario) == 0:
            print(" El inventario esta vacio. ")
        else:
            print("\n--- LISTA DE PRODUCTOS ---")
            for p in inventario:
                print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}")

    elif opcion == "3":
        # --- VENDER (Restar Stock) ---
        nombre_venta = input(" ¿Que producto quieres vender?: ")
        encontrado = False

        for p in inventario:
            # Se busca si el nombre coincide (ignora mayusculas/minusculas)
            if p["nombre"].lower() == nombre_venta.lower():
                encontrado = True
                if p["stock"] > 0:
                    p["stock"] = p["stock"] - 1 # Se le resta uno al stock
                    print(f" Venta realizada. Nuevo stock de {p['nombre']}: {p['stock']} ")
                else:
                    print(f" No hay stock suficiente de {p['nombre']}.")
                break # Se sale del bucle for porque ya encontro el producto

        if not encontrado:
            print(" Producto no encontrado. ")

    elif opcion == "4":
        print(" Saliendo del sistema... ")
        break
    
    else:
        print( "Opción no válida, intenta de nuevo." )
