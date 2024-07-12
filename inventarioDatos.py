import os
 
def crear_producto(nombre, cantidad, precio):
    return {
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio
    }
 
def producto_a_string(producto):
    return f"{producto['nombre']},{producto['cantidad']},{producto['precio']}"
 
def producto_desde_string(linea):
    nombre, cantidad, precio = linea.strip().split(',')
    return crear_producto(nombre, int(cantidad), float(precio))
 
 
 
def cargar_productos():
    productos = []
    if os.path.exists('inventario.txt'):
        with open('inventario.txt', 'r') as file:
            for line in file:
                productos.append(producto_desde_string(line))
    return productos
 
def guardar_productos(productos):
    with open('inventario.txt', 'w') as file:
        for producto in productos:
            file.write(producto_a_string(producto) + '\n')
 
def ingresar_producto():
    nombre = input("Ingresar Nombre del Producto: ")
    cantidad = int(input("Ingresar Cantidad: "))
    precio = float(input("Ingresar Precio: "))
    producto = crear_producto(nombre, cantidad, precio)
    productos = cargar_productos()
    productos.append(producto)
    guardar_productos(productos)
    print("Producto ingresado exitosamente.\n")
 
def editar_producto():
    productos = cargar_productos()
    if not productos:
        print("No hay productos en el inventario.\n")
        return
 
    print("Productos Ingresados:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']}, {producto['cantidad']}, {producto['precio']}")
 
    try:
        index = int(input("Seleccione el número del producto a editar: ")) - 1
        if 0 <= index < len(productos):
            producto = productos[index]
            producto['cantidad'] = int(input(f"Ingresar Nueva Cantidad para {producto['nombre']}: "))
            producto['precio'] = float(input(f"Ingresar Nuevo Precio para {producto['nombre']}: "))
            guardar_productos(productos)
            print("Producto editado exitosamente.\n")
        else:
            print("Número de producto no válido.\n")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.\n")
 
def eliminar_producto():
    productos = cargar_productos()
    if not productos:
        print("No hay productos en el inventario.\n")
        return
 
    print("Productos Ingresados:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']}, {producto['cantidad']}, {producto['precio']}")
 
    try:
        index = int(input("Seleccione el número del producto a eliminar: ")) - 1
        if 0 <= index < len(productos):
            del productos[index]
            guardar_productos(productos)
            print("Producto eliminado exitosamente.\n")
        else:
            print("Número de producto no válido.\n")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.\n")
 
def listar_productos():
    productos = cargar_productos()
    if not productos:
        print("No hay productos en el inventario.\n")
        return
    print("Listado de Productos:")
    print(f"{'Nombre':<20} {'Cantidad':>10} {'Precio':>10}")
    print("-" * 45)
    for producto in productos:
        print(f"{producto['nombre']:<20} {producto['cantidad']:>10} {producto['precio']:>10.2f}")
    print()
 
 
def menu():
    while True:
        print("Sistema de Inventarios")
        print("1. Ingresar Producto")
        print("2. Editar Producto")
        print("3. Eliminar Producto")
        print("4. Listar Productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
 
        if opcion == '1':
            ingresar_producto()
        elif opcion == '2':
            editar_producto()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            listar_productos()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
 
if __name__ == "__main__":
    menu()
