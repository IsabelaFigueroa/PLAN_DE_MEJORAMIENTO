# ------------------------------
# Definición de la clase Estudiante
# ------------------------------
class Estudiante:
    # Constructor: inicializa los atributos del estudiante
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre   # Atributo nombre
        self.edad = edad       # Atributo edad
        self.nota = nota       # Atributo nota

    # Método para mostrar la información del estudiante
    def mostrar_info(self):
        print(f"\n Nombre: {self.nombre} | Edad: {self.edad} | Nota: {self.nota}")

    # Método para comprobar si el estudiante aprobó
    def aprobo(self):
        if self.nota >= 3.0:   # Condicional: nota mayor o igual a 3
            print(f" {self.nombre} ha aprobado.")
        else:
            print(f" {self.nombre} no ha aprobado.")


# ------------------------------
# Programa principal
# ------------------------------

# Lista donde se almacenarán los objetos de tipo Estudiante
lista_estudiantes = []

# Bucle infinito para el menú (solo se detiene con "break")
while True:
    # Mostrar menú de opciones
    print("\n--- MENÚ ---")
    print("1. Agregar estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Salir")

    # Entrada de usuario
    opcion = input("Elige una opción: ")

    # ------------------------------
    # Opción 1: Agregar estudiante
    # ------------------------------
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ").title()  # .title() → primera letra en mayúscula
        edad = int(input("Ingrese la edad: "))      # Se convierte a entero
        nota = float(input("Ingrese la nota: "))    # Se convierte a decimal

        # Crear un objeto Estudiante con los datos ingresados
        estudiante = Estudiante(nombre, edad, nota)

        # Guardar el objeto en la lista
        lista_estudiantes.append(estudiante)

        print(" El estudiante fue agregado con éxito.")

    # ------------------------------
    # Opción 2: Mostrar lista de estudiantes
    # ------------------------------
    elif opcion == "2":
        if not lista_estudiantes:  # Verificar si la lista está vacía
            print(" No hay estudiantes registrados.")
        else:
            print("\n Lista de estudiantes:")
            # Recorrer la lista y mostrar info de cada objeto
            for est in lista_estudiantes:
                est.mostrar_info()
                est.aprobo()

    # ------------------------------
    # Opción 3: Salir del programa
    # ------------------------------
    elif opcion == "3":
        print(" Saliendo del programa...")
        break  # Rompe el bucle y finaliza el programa

    # ------------------------------
    # Opción no válida
    # ------------------------------
    else:
        print(" Opción no válida, intenta de nuevo.")