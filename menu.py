print('BIENVENIDO AL EXPLORADOR DE TAREAS')

def leer_tareas():
    try:
        with open("guardar_tareas.txt", "r", encoding="UTF-8") as archivo:
            tareas = archivo.read().strip().split("\n")
            return [tarea for tarea in tareas if tarea]
    except FileNotFoundError:
        return []

def escribir_tareas(tareas):
    with open("guardar_tareas.txt", "w", encoding="UTF-8") as archivo:
        archivo.write("\n".join(tareas) + "\n")

def imprimir_tareas(tareas):
    print("------------------")
    print(f"TIENES {len(tareas)} TAREAS:\n")
    for i, tarea in enumerate(tareas, start=1):
        print(f"TAREA {i}:\n{tarea}")

def verificar_tareas():
    tareas = leer_tareas()
    if not tareas:
        print("NO HAY TAREAS")
    else:
        imprimir_tareas(tareas)

def opcion_invalida():
    print("------------------")
    print("OPCIÓN INVÁLIDA")

while True:
    print(
        "------------------\n"
        "Ingrese 1 para crear una nueva tarea\n"
        "Ingrese 2 para ver tus tareas\n"
        "Ingrese 3 para borrar una tarea\n"
        "Ingrese 4 para salir\n"
        "------------------"
    )

    try:
        opc = int(input(""))

        if opc == 1:
            print(
                "------------------\n"
                "INGRESE LA DESCRIPCIÓN DE LA TAREA\n"
                "Cuando termine, presione enter e ingrese '//' para guardar la tarea\n"
                "------------------"
            )
            tarea = ""
            while True:
                linea = input()
                if linea == "//":
                    break
                tarea += linea + "\n"
            tarea = tarea.strip()
            tareas = leer_tareas()
            tareas.append(tarea)
            escribir_tareas(tareas)

        elif opc == 2:
            verificar_tareas()

        elif opc == 3:
            tareas = leer_tareas()
            verificar_tareas()
            if tareas:
                try:
                    print("------------------")
                    num_tarea = int(input("Ingrese el número de la tarea que desea borrar: "))
                    if 1 <= num_tarea <= len(tareas):
                        del tareas[num_tarea - 1]
                        escribir_tareas(tareas)
                        print("TAREA BORRADA")
                    else:
                        opcion_invalida()
                except ValueError:
                    opcion_invalida()

        elif opc == 4:
            print("CERRANDO PROGRAMA...")
            break
        
        else:
            opcion_invalida()
        
    except ValueError:
        opcion_invalida()
