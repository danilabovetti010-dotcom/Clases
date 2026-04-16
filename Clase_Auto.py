class Auto:
    def __init__(self, marca, modelo, fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.fabricacion = fabricacion

    def obtener_marca(self):
        return self.marca

    def establecer_marca(self, marca):
        self.marca = marca

    def obtener_modelo(self):
        return self.modelo

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def obtener_fabricacion(self):
        return self.fabricacion

    def establecer_fabricacion(self, fabricacion):
        self.fabricacion = fabricacion

if __name__ == "__main__":
    auto1 = Auto("Ford", 206, 2010)

    print(f"Marca: {auto1.obtener_marca()}")
    print(f"Modelo: {auto1.obtener_modelo()}")
    print(f"Fabricacion: {auto1.obtener_fabricacion()}")

    auto1.establecer_marca("Chevrolet")
    auto1.establecer_modelo(208)
    auto1.establecer_fabricacion(2012)

    print("\nDespués de actualizar:")
    print(f"Marca: {auto1.obtener_marca()}")
    print(f"Modelo: {auto1.obtener_modelo()}")
    print(f"Fabricacion: {auto1.obtener_fabricacion()}")