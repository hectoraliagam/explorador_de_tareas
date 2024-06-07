print('¡Bienvenido al explorador de tareas!')
cantidad_de_tareas = 0

def leer_tareas():
    try:
        with open("guardar_tareas.txt", "r", encoding="UTF-8") as archivo:
            contenido = archivo.read().strip()
            if contenido:
                return contenido.split("-----\n")
            else:
                return []
    except FileNotFoundError:
        return []

def escribir_tareas(tareas):
    with open("guardar_tareas.txt", "w", encoding="UTF-8") as archivo:
        archivo.write("-----\n".join(tareas) + "\n")

while True:
    print('Ingrese 1 para crear una nueva tarea')
    print('Ingrese 2 para ver tus tareas')
    print('Ingrese 3 para borrar una tarea')
    print('Ingrese 4 para salir')
    opc = int(input(""))

    if opc == 1 and cantidad_de_tareas < 8:
        # Crear tarea
        print("Ingrese la descripción de la tarea. Cuando termine, ingrese '//' para guardar la tarea.")
        tarea = ""
        while True:
            linea = input()
            if linea == "//":
                break
            tarea += linea + "\n"

        tarea = tarea.strip()  # Eliminar espacios en blanco alrededor de la tarea
        tareas = leer_tareas()
        tareas.append(tarea)
        escribir_tareas(tareas)
        cantidad_de_tareas += 1
    elif opc == 2:
        # Ver tareas
        tareas = leer_tareas()
        if len(tareas) == 0:
            print("No hay tareas.")
        else:
            print(f"Tienes {len(tareas)} tareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"Tarea {i}:\n{tarea}")
    elif opc == 3:
        # Borrar tarea
        tareas = leer_tareas()
        if len(tareas) == 0:
            print("No hay tareas para borrar.")
        else:
            print(f"Tienes {len(tareas)} tareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"TAREA {i}:\n{tarea}")
            num_tarea = int(input("Ingrese el número de la tarea que desea borrar: "))
            if num_tarea < 1 or num_tarea > len(tareas):
                print("NÚMERO DE TAREA INVÁLIDO")
            else:
                del tareas[num_tarea - 1]
                escribir_tareas(tareas)
                cantidad_de_tareas -= 1
                print("TAREA BORRADA")
    elif opc == 4:
        # Salir
        print("Hasta luego...")
        break
    else:
        print("Opción inválida")
