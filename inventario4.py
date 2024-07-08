class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre:<20} {self.cantidad:>10} {self.precio:>10.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def ingresar_producto(self):
        nombre = input("Ingresar Nombre del Producto: ")
        cantidad = int(input("Ingresar Cantidad: "))
        precio = float(input("Ingresar Precio: "))
        producto = Producto(nombre, cantidad, precio)
        self.productos.append(producto)
        print("Producto ingresado exitosamente.\n")

    def editar_producto(self):
        if not self.productos:
            print("No hay productos en el inventario.\n")
            return

        print("Productos Ingresados:")
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto}")

        try:
            index = int(input("Seleccione el número del producto a editar: ")) - 1
            if 0 <= index < len(self.productos):
                producto = self.productos[index]
                producto.cantidad = int(input(f"Ingresar Nueva Cantidad para {producto.nombre}: "))
                producto.precio = float(input(f"Ingresar Nuevo Precio para {producto.nombre}: "))
                print("Producto editado exitosamente.\n")
            else:
                print("Número de producto no válido.\n")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número.\n")

    def eliminar_producto(self):
        if not self.productos:
            print("No hay productos en el inventario.\n")
            return

        print("Productos Ingresados:")
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto}")

        try:
            index = int(input("Seleccione el número del producto a eliminar: ")) - 1
            if 0 <= index < len(self.productos):
                del self.productos[index]
                print("Producto eliminado exitosamente.\n")
            else:
                print("Número de producto no válido.\n")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número.\n")

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.\n")
            return
        print("Listado de Productos:")
        print(f"{'Nombre':<20} {'Cantidad':>10} {'Precio':>10}")
        print("-" * 40)
        for producto in self.productos:
            print(producto)
        print()


def menu():
    inventario = Inventario()
    while True:
        print("Sistema de Inventarios")
        print("1. Ingresar Producto")
        print("2. Editar Producto")
        print("3. Eliminar Producto")
        print("4. Listar Productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            inventario.ingresar_producto()
        elif opcion == '2':
            inventario.editar_producto()
        elif opcion == '3':
            inventario.eliminar_producto()
        elif opcion == '4':
            inventario.listar_productos()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")


if __name__ == "__main__":
    menu()
