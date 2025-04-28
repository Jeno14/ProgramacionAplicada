class calculadora:
    def __init__(self, a, b):
        self.a = int (a)
        self.b = int (b)

    def sumar(self):
        suma = self.a + self.b
        print("La suma es: ", suma)

    def restar(self):
        resta = self.a - self.b 
        print("La resta es: ", resta)

    def multiplicar(self):
        multiplicacion = self.a* self.b
        print("La multiplicación es: ", multiplicacion)

    def dividir(self):
        division = self.a / self.b
        print("La división es: ", division)


a = input("ingrese un numero: ")
b = input("ingrese un numero: ")

calculadora = calculadora(a,b)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()
