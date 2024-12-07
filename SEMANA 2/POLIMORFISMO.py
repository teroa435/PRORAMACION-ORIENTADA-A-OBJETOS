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
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= max(daño, 0)  # Evitar daño negativo
        print(self.nombre, "ha realizado", max(daño, 0), "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)

    def daño(self, enemigo):
        # El Guerrero inflige daño extra basado en su fuerza
        daño_base = super().daño(enemigo)
        daño_extra = self.fuerza * 0.2
        return daño_base + daño_extra

    def atacar(self, enemigo):
        print(f"{self.nombre} realiza un ataque poderoso.")
        super().atacar(enemigo)


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)

    def daño(self, enemigo):
        # El Mago inflige daño basado en su inteligencia
        return self.inteligencia * 2 - enemigo.defensa

    def atacar(self, enemigo):
        print(f"{self.nombre} lanza un hechizo.")
        super().atacar(enemigo)

    def curar(self):
        # El Mago puede curarse a sí mismo
        curación = self.inteligencia * 1.5
        self.vida += curación
        print(f"{self.nombre} se ha curado {curación} puntos de vida.")
        print("Nueva vida:", self.vida)


# Ejemplo de uso
guerrero = Guerrero("Thor", fuerza=15, inteligencia=5, defensa=10, vida=50)
mago = Mago("Merlín", fuerza=5, inteligencia=20, defensa=8, vida=40)

guerrero.atributos()
mago.atributos()

guerrero.atacar(mago)
mago.curar()
mago.atacar(guerrero)
