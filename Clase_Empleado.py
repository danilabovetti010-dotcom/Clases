#Crea una clase "Empleado" con propiedades para el nombre, la edad, el salario y el cargo, 
#y métodos para obtener y establecer estas propiedades, así como un método para calcular el salario anual.

class Empleado:
    def __init__(self, nombre, edad, cargo, salario):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_cargo(self):
        return self.cargo

    def establecer_cargo(self, cargo):
        self.cargo = cargo
        
    def obtener_salario(self):
        return self.salario
    
    def establecer_salario(self, salario):
        self.salario = salario

    def calcular_salario(self):
        return self.salario * 12

if __name__ == "__main__":
    empleado1 = Empleado("Pepito", 45, "Contador", 1000)

    print(f"Nombre: {empleado1.obtener_nombre()}")
    print(f"Edad: {empleado1.obtener_edad()}")
    print(f"Cargo: {empleado1.obtener_cargo()}")
    print(f"Salario: ${empleado1.obtener_salario()}")

    empleado1.establecer_nombre("Pepita")
    empleado1.establecer_salario(1200)

    print("\nDespués de actualizar:")
    print(f"Nombre: {empleado1.obtener_nombre()}")
    print(f"Salario: ${empleado1.obtener_salario()}")
    
    print(f"\nNuevo Salario: ${empleado1.obtener_salario()}")

    Salario_Anual = empleado1.calcular_salario()
    print(f"Salario Anual Total: ${Salario_Anual}")