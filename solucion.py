# Diccionarios iniciales
Productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

'''
ingresarProducto: Incrementa la máxima clave en una unidad y registra el producto con sus respectivos datos
'''
def ingresarProducto(nombreProducto, precioProducto, stockProducto):
    nuevaClave = max(Productos.keys()) + 1 # Incrementado en uno al último valor ingresado 
    Productos[nuevaClave] = nombreProducto
    Precios[nuevaClave] = precioProducto
    Stock[nuevaClave] = stockProducto
    return nuevaClave

'''
eliminarProducto: Elimina el producto por la clave dada
'''
def eliminarProducto(claveProducto):
    Productos.pop(claveProducto)
    Precios.pop(claveProducto)
    Stock.pop(claveProducto)
    # del Productos[claveProducto]
    # del Precios[claveProducto]
    # del Stock[claveProducto]

'''
eliminarProducto: Actualiza el producto, encontrado por la clave ingresada, con los nuevos valores
'''
def actualizarProducto(claveProducto, nombreProducto, precioProductoActualizado, stockProductoActualizado):
    Productos[claveProducto] = nombreProductoActualizado
    Precios[claveProducto] = precioProductoActualizado
    Stock[claveProducto] = stockProductoActualizado

'''
imprimirListaProductos: Resumen de los diccionarios
'''
def imprimirListaProductos() -> 'Resumen de los diccionarios':
    print('====================================================')
    print('Lista de Productos')
    print('====================================================')
    # La clave del producto es la clave 'foranea' que se relaciona en los diccionarios Precios y Stock 
    for claveProducto in Productos.keys():
        print(f'{claveProducto} \t {Productos[claveProducto]} \t {Precios[claveProducto]} \t {Stock[claveProducto]}')
    print('====================================================')

if __name__ == "__main__":
    imprimirListaProductos()
    while(True):
        #Flujo
        print('[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir')

        try:
            opcion = int(input('Elija una opción: '))
            
            if opcion == 1:
                nombreProducto = str(input('Ingrese el nombre del producto: '))
                precioProducto = float(input('Ingrese el precio del producto: '))
                stockProducto = int(input('Ingrese el stock del producto: '))
                nuevaClave = ingresarProducto(nombreProducto, precioProducto, stockProducto)
                print(f"Producto registrado exitosamente con la clave {nuevaClave}")
                imprimirListaProductos()
            elif opcion == 2:
                claveProducto = int(input('Ingrese la clave del producto a eliminar: '))
                if(claveProducto in Productos.keys()):
                # if (claveProducto in Productos): # Recorre las claves por defecto
                    eliminarProducto(claveProducto)
                    print(f"Producto {claveProducto} eliminado exitosamente")
                    imprimirListaProductos()
                else:
                    print("Producto no encontrado")
            elif opcion == 3:
                claveProducto = int(input('Ingrese la clave del producto a actualizar: '))
                if(claveProducto in Productos.keys()):
                # if (claveProducto in Productos): # Recorre las claves por defecto
                    nombreProductoActualizado = str(input('Ingrese el nuevo nombre del producto: '))
                    precioProductoActualizado = float(input('Ingrese el nuevo precio del producto: '))
                    stockProductoActualizado = int(input('Ingrese el nuevo stock del producto: '))
                    actualizarProducto(claveProducto, nombreProductoActualizado, precioProductoActualizado, stockProductoActualizado)
                    print(f"Producto {claveProducto} actualizado exitosamente")
                    imprimirListaProductos()
                else:
                    print("Producto no encontrado")
            elif opcion == 4:
                print("Muchas gracias por usar el programa, hasta la próxima")
                break
                # quit()
            else:
                print("Opción no valida")

        except ValueError:
            print("No es un valor válido para la entrada")
