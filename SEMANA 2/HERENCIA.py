class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return max(self.fuerza - enemigo.defensa, 0)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


# Clase derivada Guerrero
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, resistencia):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.resistencia = resistencia

    def atributos(self):
        super().atributos()
        print("·Resistencia:", self.resistencia)

    def atacar_poderoso(self, enemigo):
        daño = self.fuerza * 1.5 - enemigo.defensa
        enemigo.vida -= max(daño, 0)
        print(self.nombre, "ha usado un ataque poderoso y realizado", round(daño), "puntos de daño")
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


# Clase derivada Mago
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, mana):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.mana = mana

    def atributos(self):
        super().atributos()
        print("·Maná:", self.mana)

    def lanzar_hechizo(self, enemigo):
        if self.mana >= 10:
            daño = self.inteligencia * 2
            enemigo.vida -= daño
            self.mana -= 10
            print(self.nombre, "ha lanzado un hechizo y realizado", daño, "puntos de daño")
            if enemigo.esta_vivo():
                print("Vida de", enemigo.nombre, "es", enemigo.vida)
            else:
                enemigo.morir()
        else:
            print(self.nombre, "no tiene suficiente maná para lanzar un hechizo")


# Ejemplo de uso
guerrero = Guerrero("Aragorn", 15, 8, 12, 100, 20)
mago = Mago("Gandalf", 5, 20, 8, 80, 50)

guerrero.atributos()
mago.atributos()

guerrero.atacar(mago)
mago.lanzar_hechizo(guerrero)
guerrero.atacar_poderoso(mago)
