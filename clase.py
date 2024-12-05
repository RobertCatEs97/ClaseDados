class Dados:
    # atributos y postcondiciones de los caso de uso
    # encapsulamiento
    __dado1 = 0
    __dado2 = 0
    __calcularSumaDados = 0

    # Metodos: metodo por caso de uso
    # def nombreCasoUso(self, parametros (precondiciones separadas con ","))
    def calcularSumaDados(self,dado1, dado2):
        self.__dado1 = dado1
        self.__dado2 = dado2
        self.__calcularSumaDados = self.____calcularSumaDados(dado1+dado2)
        return self.__calcularSumaDados 
