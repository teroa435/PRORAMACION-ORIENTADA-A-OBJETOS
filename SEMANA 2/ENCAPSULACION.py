class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_fuerza(self):
        return self.__fuerza

    def get_inteligencia(self):
        return self.__inteligencia

    def get_defensa(self):
        return self.__defensa

    def get_vida(self):
        return self.__vida

    # Setters
    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza

    def set_inteligencia(self, inteligencia):
        self.__inteligencia = inteligencia

    def set_defensa(self, defensa):
        self.__defensa = defensa

    def set_vida(self, vida):
        self.__vida = vida

    # Métodos de la clase
    def atributos(self):
        print(self.get_nombre(), ":", sep="")
        print("·Fuerza:", self.get_fuerza())
        print("·Inteligencia:", self.get_inteligencia())
        print("·Defensa:", self.get_defensa())
        print("·Vida:", self.get_vida())

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.set_fuerza(self.get_fuerza() + fuerza)
        self.set_inteligencia(self.get_inteligencia() + inteligencia)
        self.set_defensa(self.get_defensa() + defensa)

    def esta_vivo(self):
        return self.get_vida() > 0

    def morir(self):
        self.set_vida(0)
        print(self.get_nombre(), "ha muerto")

    def daño(self, enemigo):
        return self.get_fuerza() - enemigo.get_defensa()

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.set_vida(enemigo.get_vida() - daño)
        print(self.get_nombre(), "ha realizado", daño, "puntos de daño a", enemigo.get_nombre())
        if enemigo.esta_vivo():
            print("Vida de", enemigo.get_nombre(), "es", enemigo.get_vida())
        else:
            enemigo.morir()


# Ejemplo de uso
jugador1 = Personaje("Héroe", 10, 5, 3, 50)
jugador2 = Personaje("Villano", 8, 4, 2, 40)

jugador1.atributos()
jugador2.atributos()

jugador1.atacar(jugador2)
jugador2.atacar(jugador1)
