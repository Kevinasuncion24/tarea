class Persona:
    def __init__(self, nombre, direccion, edad, genero):
        self._nombre = nombre
        self._direccion = direccion
        self._edad = edad
        self._genero = genero

    @property
    def nombre(self):
        return self._nombre

    @property
    def direccion(self):
        return self._direccion

    @property
    def edad(self):
        return self._edad

    @property
    def genero(self):
        return self._genero

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @direccion.setter
    def direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

    @genero.setter
    def genero(self, nuevo_genero):
        self._genero = nuevo_genero

    def __str__(self):
        return f"Nombre: {self._nombre}, Dirección: {self._direccion}, Edad: {self._edad} años, Género: {self._genero}"

# Ejemplo de uso:
persona1 = Persona(nombre="Maria", direccion="Rumichaca y Cordoba 1045", edad=180, genero="Femenino")
print(persona1)
