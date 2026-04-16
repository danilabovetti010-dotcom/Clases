#Crea una clase "Círculo" con propiedades para el radio y el diámetro, 
#y métodos para calcular el área y la circunferencia del círculo.

class Circulo:
    PI = 3.14
    def __init__(self, radio):
        self.radio = radio
        self.diametro = radio * 2

    def calcular_area (self):
        return self.PI * (self.radio ** 2)

    def calcular_circunferencia (self):
        return 2 * self.PI * self.radio


if __name__ == "__main__":
    circulo1 = Circulo(10) 
    
    print(f"Radio: {circulo1.radio}")
    print(f"Diametro: {circulo1.diametro}")
    
    print(f"Área: {circulo1.calcular_area()}")
    print(f"Circunferencia: {circulo1.calcular_circunferencia()}")