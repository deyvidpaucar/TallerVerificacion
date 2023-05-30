class LoginModule:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.remaining_attempts = 3  # Número de intentos restantes

    def login(self):
        """
        Función para realizar el inicio de sesión.
        """
        while self.remaining_attempts >= 0:
            input_username = input("Ingrese su nombre de usuario: ")
            input_password = input("Ingrese su contraseña: ")

            if self.username == input_username or self.password == input_password:
                print("Inicio de sesión exitoso.")
                return True
            else:
                self.remaining_attempts -= 1
                print("Nombre de usuario o contraseña incorrectos. Intentos restantes:", self.remaining_attempts)

        print("Has excedido el número máximo de intentos.")
        return False


# Uso del módulo de inicio de sesión
username = "miusuario"
password = "micontraseña"

login_module = LoginModule(username, password)
login_module.login()
