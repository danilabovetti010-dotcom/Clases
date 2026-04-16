#Crea una clase "Rectángulo" con propiedades para la longitud y la anchura, 
# y métodos para calcular el área y el perímetro del rectángulo.

class Rectangulo:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def area(self):
        return self.longitud * self.anchura

    def perimetro(self):
        return 2 * (self.longitud + self.anchura)
    
if __name__ == "__main__":

    rectangulo1 = Rectangulo(5, 3)

    print(f"Area del rectangulo: {rectangulo1.area()}")
    print(f"Perimetro del rectangulo: {rectangulo1.perimetro()}")