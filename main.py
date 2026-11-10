from modelos import Paciente, PacienteHospitalizado


if __name__ == "__main__":
    paciente = Paciente("Ana Ruiz", 20, "Migraña", "EXP-001")
    ingresado = PacienteHospitalizado(
        "Luis Vega", 40, "Fractura de brazo", "EXP-002", "102", "Dra. Silva"
    )

    # La misma llamada muestra información distinta según la clase.
    print("=== HERENCIA Y POLIMORFISMO ===")
    for persona in (paciente, ingresado):
        persona.mostrar_informacion()
        print()

    print("=== ENCAPSULAMIENTO ===")
    ingresado.set_edad(41)
    try:
        ingresado.set_edad(-5)
    except ValueError as error:
        print(error)
    assert ingresado.get_edad() == 41
    print(f"Edad conservada: {ingresado.get_edad()} años")

    print("\n=== COMPOSICIÓN ===")
    # Paciente delega el cambio al expediente que contiene.
    ingresado.actualizar_diagnostico("Fractura de brazo en recuperación")
    assert ingresado.diagnostico == "Fractura de brazo en recuperación"
    assert paciente.diagnostico == "Migraña"

    print("\n=== INFORMACIÓN FINAL ===")
    ingresado.cambiar_habitacion("105")
    ingresado.dar_alta()
    ingresado.mostrar_informacion()
