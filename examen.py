productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],

}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}


def stock_marca(marca):
    total_stock = sum(stock[modelo][1] for modelo in productos if productos[modelo][0].lower() == marca)
    print(f"El stock es de {total_stock}")


def búsqueda_precio(precio_minimo, precio_maximo):
    try:
        precio_minimo, precio_maximo = int(precio_minimo), int(precio_maximo)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return

    resultados = []
    for modelo, datos in stock.items():
        if precio_minimo <= datos[0] <= precio_maximo and datos[1] > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")

    if resultados:
        print("Los notebooks entre los precios consultados son:", sorted(resultados))
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, precio):
    if modelo not in stock:
        return False
    stock[modelo][0] = precio
    return True

def menu():
    print("-"*60)
    print("\t\t MENU PRINCIPAL")
    print("-"*60)
    print("1. Stock marca.")
    print("2. Busqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

def main():
    while True:

        menu()

        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                marca = input("Ingrese la marca a consultar: ").lower()
                stock_marca(marca)
            case "2":
                precio_minimo = input("Ingrese precio minimo: ")
                precio_maximo = input("Ingrese precio máximo: ")
                búsqueda_precio(precio_minimo,precio_maximo)
            case "3":
                while continuar != "SI":
                    continuar = "SI"
                    modelo = input("Ingrese el modelo a actualizar: ")
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    except ValueError:
                        print("Debe ingresar un precio valido.")
                        continue
                    if actualizar_precio(modelo,nuevo_precio):
                        print("precio actualizado.")
                    else:
                        print("El modelo no existe.")

                    continuar = input("Desea actualizar otro precio? (SI/NO)?: ").upper()
                    if continuar == "NO":
                        continuar = "NO"
            case "4":
                print("cerrando programa...")
                break
            case _:
                print("Debe seleccionar una opcion valida.")
                

main()
