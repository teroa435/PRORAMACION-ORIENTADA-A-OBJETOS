class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def mostrar_atributos(self):
        print(f"--- {self.nombre} ---")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")

    def subir_nivel(self, fuerza=0, inteligencia=0, defensa=0, vida_extra=0):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.vida += vida_extra
        print(f"{self.nombre} ha subido de nivel. Nuevos atributos:")
        self.mostrar_atributos()

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, daño):
        daño_real = max(0, daño - self.defensa)
        self.vida -= daño_real
        print(f"{self.nombre} ha recibido {daño_real} puntos de daño.")
        if not self.esta_vivo():
            self.morir()

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto.")

    def atacar(self, enemigo):
        daño = self.fuerza
        print(f"{self.nombre} ataca a {enemigo.nombre}.")
        enemigo.recibir_daño(daño)


class Hechizo:
    def __init__(self, nombre, daño, costo_mana):
        self.nombre = nombre
        self.daño = daño
        self.costo_mana = costo_mana

    def lanzar(self, lanzador, objetivo):
        print(f"{lanzador.nombre} lanza {self.nombre} a {objetivo.nombre}.")
        objetivo.recibir_daño(self.daño)


# Ejemplo de uso
jugador = Personaje("Héroe", fuerza=10, inteligencia=8, defensa=5, vida=50)
enemigo = Personaje("Goblin", fuerza=6, inteligencia=2, defensa=3, vida=30)

hechizo_fuego = Hechizo("Bola de Fuego", daño=15, costo_mana=5)

jugador.mostrar_atributos()
enemigo.mostrar_atributos()

jugador.atacar(enemigo)
hechizo_fuego.lanzar(jugador, enemigo)

enemigo.atacar(jugador)
jugador.subir_nivel(fuerza=2, inteligencia=1, defensa=1, vida_extra=10)
