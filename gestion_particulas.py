from .particula import Particula
import json

class Gestor_Particulas:
    def __init__ (self):
        self.__particulas =[]
    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration


    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent= 5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0
    

#p01 = Particula(12345, 0, 0, 120, 240, 35, 190, 150, 160)
#p02 = Particula(12444, 12, 23, 15, 16, 9, 234, 34, 54)

#gestor = Gestor_Particulas()
#gestor.agregar_final(Particula(123222, 9, 9, 9, 9, 0, 32, 43, 45))
#gestor.agregar_inicio(p02)
#gestor.agregar_final(p01)
#gestor.mostrar()
