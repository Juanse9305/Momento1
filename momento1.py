#Juan Sebastian Alvarez G
#Danny Taborda

Motos = {
    "Honda": {"modelo": "Navi", "precio": 7000000},
    "Yamaha": {"modelo": "N-Max", "precio": 12000000},
    "Kawasaki": {"modelo": "Ninja ZX", "precio": 40000000}
}

while True:
    print("Menu: \n 1. Agregar moto \n 2. Buscar moto \n 3. Actualizar información de una moto \n 4. Eliminar moto \n 5. Salir")

    opcion = input("Digite una opción: ")

    if opcion == "1":
        marca = input("Ingrese la marca de la moto: ")
        modelo = input("Ingrese el modelo de la moto: ")
        precio = float(input("Ingrese el precio de la moto: "))
        Motos[marca] = {"modelo": modelo,
                        "precio": precio}
        print("Moto agregada correctamente.")

    elif opcion == "2":
        marca = input("Ingrese la marca de la moto que desea buscar: ")
        if marca in Motos:
            moto = Motos[marca]
            print(f"Marca: {marca}\n Modelo: {moto['modelo']}\n Precio: {moto['precio']}")
        else:
            print("Moto no encontrada.")

    elif opcion == "3":
        marca = input("Ingrese la marca de la moto que desea actualizar: ")
        if marca in Motos:
            modelo = input("Ingrese el nuevo modelo de la moto: ")
            precio = float(input("Ingrese el nuevo precio de la moto: "))
            Motos[marca] = {"modelo": modelo, 
                            "precio": precio}
            print("Información de la moto actualizada correctamente.")
        else:
            print("Moto no encontrada.")

    elif opcion == "4":
        marca = input("Ingrese la marca de la moto que desea eliminar: ")
        if marca in Motos:
            del Motos[marca]
            print("Moto eliminada correctamente.")
        else:
            print("Moto no encontrada.")

    elif opcion == "5":
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")
