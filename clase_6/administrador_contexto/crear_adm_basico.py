class MiAdministradorDeContexto:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        print(f"El mensaje es: {mensaje}")

    def __enter__(self):
        print("Entro al administrador de contexto")
        # Esto es lo que devuelve el administador de contexto
        return self

    def __exit__(self, type, value, traceback):
        print("Salio del administrador de contexto")


with MiAdministradorDeContexto("Este es el mensaje") as administrador:
    print(
        f"Estamos dentro del administrador de contexto el mensaje es: {administrador.mensaje}"
    )

print(__file__)
