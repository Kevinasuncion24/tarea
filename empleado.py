from persona import Persona

class Empleado(Persona):
    def __init__(self, num_empleado, salario):
        self._num_empleado = num_empleado
        self._salario = salario

    @property
    def num_empleado(self):
        return self._num_empleado

    @property
    def salario(self):
        return self._salario

    @num_empleado.setter
    def num_empleado(self, nuevo_num_empleado):
        self._num_empleado = nuevo_num_empleado

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario >= 0:
            self._salario = nuevo_salario
        else:
            print("El salario no puede ser negativo.")

    def __str__(self):
        return f"Número de Empleado: {self.num_empleado}, Salario: ${self.salario:.2f}"

# Ejemplo de uso:
empleado1 = Empleado(num_empleado=333445, salario=480)
print(empleado1)
