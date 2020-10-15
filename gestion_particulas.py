from particula import Particula
class Gestor_Particulas:
    def __init__ (self):
        self.__particulas =[]
    def agregar_final(self, particula_x: Particula):
        self.__particulas.append(particula_x)
    def agregar_inicio(self, particula_x:Particula):
        self.__particulas.insert(0, particula_x)
    def mostrar(self):
        for Particula in self.__particulas:
            print(Particula)

p01 = Particula(12345, 0, 0, 120, 240, 35, 190, 150, 160)
p02 = Particula(12444, 12, 23, 15, 16, 9, 234, 34, 54)

gestor = Gestor_Particulas()
gestor.agregar_final(Particula(123222, 9, 9, 9, 9, 0, 32, 43, 45))
gestor.agregar_inicio(p02)
gestor.agregar_final(p01)
gestor.mostrar()
