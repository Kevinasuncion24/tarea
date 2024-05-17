from empleado import Empleado

class Cliente(Empleado):
    def __init__(self, numero_cliente, fecha_registro, vip=False):
        self._numero_cliente = numero_cliente
        self._fecha_registro = fecha_registro
        self._vip = vip

    @property
    def numero_cliente(self):
        return self._numero_cliente

    @numero_cliente.setter
    def numero_cliente(self, nuevo_numero):
        self._numero_cliente = nuevo_numero

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, nueva_fecha):
        self._fecha_registro = nueva_fecha

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, es_vip):
        self._vip = es_vip

    def __str__(self):
        return f"Cliente {self.numero_cliente} registrado el {self.fecha_registro}. VIP: {self.vip}"

# Ejemplo de uso
cliente1 = Cliente(numero_cliente=777889, fecha_registro="2024-05-17", vip=True)
print(str(cliente1))
