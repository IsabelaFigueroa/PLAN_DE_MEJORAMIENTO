# ------------------------------
# Clase Estudiante
# ------------------------------
class Estudiante:
    def __init__(self, nombre, edad, nota):
        # Atributos de la clase Estudiante
        self.nombre = nombre.title()  # Corrige el formato (Mayúscula inicial)
        self.edad = edad
        self.nota = nota

    def mostrar_info(self):
        """Muestra la información básica del estudiante"""
        print(f" Nombre: {self.nombre} | Edad: {self.edad} | Nota: {self.nota}")

    def aprobo(self):
        """Indica si el estudiante aprobó o no"""
        if self.nota >= 3.0:
            print(f" {self.nombre} ha aprobado.")
        else:
            print(f" {self.nombre} no ha aprobado.")


# ------------------------------
# Clase SistemaRegistro
# ------------------------------
class SistemaRegistro:
    def __init__(self):
        # Lista que almacenará los estudiantes
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        """Agrega un estudiante ya creado al sistema"""
        self.estudiantes.append(estudiante)
        print(f" {estudiante.nombre} fue agregado al sistema.")

    def listar_estudiantes(self):
        """Muestra todos los estudiantes registrados"""
        if not self.estudiantes:
            print(" No hay estudiantes registrados.")
        else:
            print("\n Lista de estudiantes:")
            for est in self.estudiantes:
                est.mostrar_info()
                est.aprobo()

    def buscar_estudiante(self, nombre):
        """Busca un estudiante por nombre"""
        nombre = nombre.title()
        for est in self.estudiantes:
            if est.nombre == nombre:
                print("\n Estudiante encontrado:")
                est.mostrar_info()
                est.aprobo()
                return
        print(" Estudiante no encontrado.")


# ------------------------------
# Creación de objetos y uso directo
# ------------------------------

# Creamos objetos Estudiante (como tu ejemplo de noche_estrellada o geraldo)
juan = Estudiante("juan perez", 16, 4.5)
maria = Estudiante("maria lopez", 17, 2.8)

# Creamos el sistema de registro
sistema = SistemaRegistro()

# Agregamos los estudiantes al sistema
sistema.agregar_estudiante(juan)
sistema.agregar_estudiante(maria)

# Llamamos métodos directamente
print("\n--- Probando métodos ---")
juan.mostrar_info()     # Mostrar info de Juan
juan.aprobo()           # Verificar si aprobó

print()
maria.mostrar_info()    # Mostrar info de María
maria.aprobo()          # Verificar si aprobó

print("\n--- Sistema De Registro ---")
sistema.listar_estudiantes()              # Listar todos
sistema.buscar_estudiante("maria lopez")  # Buscar a María