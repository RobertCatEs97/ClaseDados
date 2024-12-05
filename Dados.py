import random

class Dados:
    def __init__(self):
        self.valor = 0

    def lanzar(self):
        """Genera un valor aleatorio entre 1 y 6 para el dado."""
        self.valor = random.randint(1, 6)

    def obtener_valor(self):
        """Devuelve el valor del dado."""
        return self.valor

class Dados:
    def __int__(self):
        self.dado1 = Dados()
        self.dado2 = Dados()

    def pedir_valor(self, dado_numero):
        """Método para pedir un valor válido entre 1 y 6."""
        while True:
            try:
                valor = int(input(f"Ingrese el valor del dado {dado_numero} (1-6): "))
                if 1 <= valor <= 6:
                    return valor
                else:
                    print("El valor debe ser un número entre 1 y 6.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    def jugar(self):
        """Método para ingresar valores de los dados y calcular la suma."""
        # Pedir valores válidos para ambos dados
        valor_dado1 = self.pedir_valor(1)
        valor_dado2 = self.pedir_valor(2)
        
        # Lanzamos los dados con los valores ingresados
        self.dado1.lanzar()
        self.dado2.lanzar()

        # Calculamos la suma de los valores
        suma = self.dado1.obtener_valor() + self.dado2.obtener_valor()
        print(f"La suma de los valores de los dos dados es: {suma}")

    def simular_tiros(self, num_tiros=100):
        """Simula 100 tiros de dados y calcula la frecuencia de cada suma entre 2 y 12."""
        frecuencias = {i: 0 for i in range(2, 13)}  # Diccionario para contar la frecuencia de las sumas de 2 a 12

        for _ in range(num_tiros):
            # Lanzar ambos dados aleatoriamente
            self.dado1.lanzar()
            self.dado2.lanzar()
            suma = self.dado1.obtener_valor() + self.dado2.obtener_valor()
            frecuencias[suma] += 1

        # Imprimir la frecuencia de cada suma
        print("\nFrecuencia de las sumas en 100 tiros:")
        for suma in range(2, 13):
            print(f"Suma {suma}: {frecuencias[suma]} veces")

# Crear una instancia de JuegoDados y ejecutar el juego
juego = Dados()