#Crea una clase "Producto" con propiedades para el nombre, el precio y el 
# stock disponible, y métodos para aumentar o disminuir el stock.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aumentar_stock(self, cantidad):
        self.stock += cantidad

    def disminuir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("No hay stock disponible")

if __name__ == "__main__":
    producto1 = Producto("Taza oro", 1500, 10)
    
    print(f"Producto: {producto1.nombre}")
    print(f"Precio: ${producto1.precio}")
    print(f"Stock disponible: {producto1.stock}")

    producto1.aumentar_stock(5)
    print(f"Stock despues de aumentar: {producto1.stock}")

    producto1.disminuir_stock(3)
    print(f"Stock despues de disminuir: {producto1.stock}")

    producto1.disminuir_stock(15)
