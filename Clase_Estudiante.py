#Crea una clase "Estudiante" con propiedades para el nombre, la edad y la carrera, y métodos para obtener 
#y establecer estas propiedades, así como un método para calcular la nota media de un conjunto de exámenes.

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_carrera(self):
        return self.carrera

    def establecer_carrera(self, carrera):
        self.carrera = carrera

    def calcular_nota (self, notas):
        return sum(notas) / len(notas)

if __name__ == "__main__":
    estudiante1 = Estudiante("Pepito", 21, "Contador")

    print(f"Nombre: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")

    estudiante1.establecer_nombre("Pepita")
    estudiante1.establecer_edad(22)
    estudiante1.establecer_carrera("Administracion")

    print("\nDespués de actualizar:")
    print(f"Nombre: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")

    Promedio = estudiante1.calcular_nota ({10, 9, 6})
    print(f"\nPromedio de notas: {Promedio}")