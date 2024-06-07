print('BIENVENIDO AL EXPLORADOR DE TAREAS')
cantidad_de_tareas = 0

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

        if opc == 1 and cantidad_de_tareas < 8:
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
            cantidad_de_tareas += 1

        elif opc == 2:
            tareas = leer_tareas()
            if len(tareas) == 0:
                print("NO HAY TAREAS")
            else:
                print("------------------")
                print(f"TIENES {len(tareas)} TAREAS:\n")
                for i, tarea in enumerate(tareas, start=1):
                    print(f"TAREA {i}:\n{tarea}")

        elif opc == 3:
            tareas = leer_tareas()
            if len(tareas) == 0:
                print("NO HAY TAREAS")
                print("------------------")
            else:
                print("------------------")
                print(f"TIENES {len(tareas)} TAREAS:\n")
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
            print("CERRANDO PROGRAMA...")
            break
        
    except ValueError:
        print("OPCIÓN INVALIDA")
