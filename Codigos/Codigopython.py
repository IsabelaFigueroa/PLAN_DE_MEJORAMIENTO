estudiantes = []
while True: 
    print("\n--- MENÚ PRINCIPAL ---") 
    print("1. Agregar estudiante") 
    print("2. Listar estudiantes") 
    print("3. Buscar estudiante") 
    print("4. Salir")
# El usuario elige una opción
    opcion = input("Elige una opción (1-4): ")
# ---------------- Opción 1: Agregar estudiante ----------------
    if opcion == "1":
        # Pedimos los datos básicos
        nombre = input("Ingrese el nombre del estudiante: ").title()  
        # .title() convierte a mayúscula la primera letra de cada palabra
        edad = int(input("Ingrese la edad: "))      
        nota = float(input("Ingrese la nota final: "))  
        # Creamos una tupla con los datos (edad, nota) porque no cambiarán
        datos = (edad, nota)
        # Creamos un diccionario con nombre y datos
        estudiante = {
            "nombre": nombre,
            "datos": datos
        }
        # Agregamos el diccionario a la lista de estudiantes
        estudiantes.append(estudiante)
        print(f" El estudiante {nombre}  fue agregado con éxito.")
    # ---------------- Opción 2: Listar estudiantes ----------------
    elif opcion == "2":
        if len(estudiantes) == 0:
            print(" No hay estudiantes registrados.")
        else:
            print("\n LISTA DE ESTUDIANTES:")
            for est in estudiantes:
                print(f" {est['nombre']} | Edad: {est['datos'][0]} | Nota: {est['datos'][1]}")
    # ---------------- Opción 3: Buscar estudiante ----------------
    elif opcion == "3":
        buscar = input("Ingrese el nombre a buscar: ").title()
        # También aplicamos .title() aquí para que coincida con el formato almacenado
        encontrado = False  
        for est in estudiantes:
            if est["nombre"] == buscar:  # Ya no hace falta .lower()
                print(f"Encontrado: {est['nombre']} | Edad: {est['datos'][0]} | Nota: {est['datos'][1]}")
                encontrado = True
                break  
        if not encontrado:
            print(" Estudiante no encontrado.")
    # ---------------- Opción 4: Salir ----------------
    elif opcion == "4":
        print("Saliendo del programa...")
        break  
    # ---------------- Opción inválida ----------------
    else:
        print("Opcion invalida, elige entre 1 y 4")
