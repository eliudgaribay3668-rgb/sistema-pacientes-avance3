class ExpedienteMedico:
    def __init__(self, numero, diagnostico):
        self.numero = numero
        self.actualizar_diagnostico(diagnostico)

    def actualizar_diagnostico(self, diagnostico):
        if not diagnostico.strip():
            raise ValueError("El diagnóstico no puede estar vacío.")
        self.diagnostico = diagnostico

    def mostrar_informacion(self):
        print(f"Diagnóstico: {self.diagnostico}")
        print(f"Número de expediente: {self.numero}")


class Paciente:
    def __init__(self, nombre, edad, diagnostico, numero_expediente):
        self.nombre = nombre
        self.set_edad(edad)
        self.__expediente = ExpedienteMedico(numero_expediente, diagnostico)
        self.hospitalizado = False

    @property
    def diagnostico(self):
        return self.__expediente.diagnostico

    @diagnostico.setter
    def diagnostico(self, valor):
        self.__expediente.actualizar_diagnostico(valor)

    @property
    def numero_expediente(self):
        return self.__expediente.numero

    @numero_expediente.setter
    def numero_expediente(self, valor):
        self.__expediente.numero = valor

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if type(edad) is not int or edad < 0:
            raise ValueError("La edad debe ser un entero no negativo.")
        self.__edad = edad

    def mostrar_informacion(self):
        print(f"Paciente: {self.nombre}")
        print(f"Edad: {self.get_edad()} años")
        self.__expediente.mostrar_informacion()
        print(f"Hospitalizado: {'Sí' if self.hospitalizado else 'No'}")

    def actualizar_diagnostico(self, nuevo_diagnostico):
        self.diagnostico = nuevo_diagnostico
        print(f"Diagnóstico actualizado: {self.diagnostico}")

    def hospitalizar(self):
        self.hospitalizado = True
        print(f"{self.nombre} ha sido hospitalizado.")

    def dar_alta(self):
        self.hospitalizado = False
        print(f"{self.nombre} ha recibido el alta médica.")


class PacienteHospitalizado(Paciente):
    def __init__(self, nombre, edad, diagnostico, numero_expediente,
                 habitacion, medico_responsable):
        super().__init__(nombre, edad, diagnostico, numero_expediente)
        self.cambiar_habitacion(habitacion)
        self.medico_responsable = medico_responsable
        self.hospitalizado = True

    def cambiar_habitacion(self, nueva_habitacion):
        if not str(nueva_habitacion).strip():
            raise ValueError("La habitación no puede estar vacía.")
        self.habitacion = nueva_habitacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Habitación: {self.habitacion}")
        print(f"Médico responsable: {self.medico_responsable}")
