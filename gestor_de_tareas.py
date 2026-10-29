# 09-05 (Principio del Proyecto - Python)
# 20-10 (Avances y Actualizaciones Proyecto - Python)
# Main
print("================================")
print("     GESTOR DE TAREAS - v1.0")
print("================================")

nombre_usuario = input("Ingresa tu nombre: ")

print(f"Bienvenido, {nombre_usuario}.")

opcion: int = 0
tareas: list[str] = []

# Cambios realizados el 20-10:
# Se agregaron type hints a las variables para mejorar la verificación estática de tipos. 


def crear_tarea(lista: list[str]):
    nombre_tarea = input("Ingrese una tarea: ")

    if nombre_tarea.strip() == "":
        print("No se ha ingresado ninguna tarea.")
    else:
        tarea = {
            "nombre": nombre_tarea,
            "completada": False
        }
        lista.append(tarea)
        print("Tarea agregada correctamente.")


def ver_tareas(lista: list[str]):
    if not lista:
        print("No hay tareas cargadas.")
    else:
        print("\n=== LISTA DE TAREAS ===")
        for i, tarea in enumerate(lista, 1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['nombre']} [{estado}]")
        print("=======================")
        completadas = 0
        pendientes = 0

        for tarea in lista:
            if tarea["completada"]:
                completadas += 1
            else:
                pendientes += 1

        print(f"Tareas completadas: {completadas}")
        print(f"Tareas pendientes: {pendientes}")


def mostrar_configuracion():
    print("""
    | \t Configuración:
    |
    | 1. Cambiar nombre de usuario
    | 2. Cambiar tema
    | 3. Volver al menú principal
    """)


while opcion != 7:

    print("""
| 1 - Ver Tareas
| 2 - Crear Tarea
| 3 - Completar Tarea
| 4 - Marcar Tarea Pendiente
| 5 - Eliminar Tarea
| 6 - Configuración
| 7 - Salir                
""")
    try:

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ver_tareas(tareas)

        elif opcion == 2:
            crear_tarea(tareas)

        elif opcion == 3:
            if not tareas:
                print("No hay tareas para completar.")
            else:
                print("Seleccione el número de tarea que desea completar: ")
                ver_tareas(tareas)

                try:
                    num_tarea = int(input("Número de tarea: "))
                    if 1 <= num_tarea <= len(tareas):
                        indice = num_tarea - 1
                        if tareas[indice]["completada"]:
                            print("La tarea ya está marcada como completada.")
                            continue
                        else:
                            tareas[indice]["completada"] = True
                            print(
                                f"Tarea {tareas[indice]['nombre']} marcada como completada."
                            )
                    else:
                        print("Número de tarea inválido.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

        elif opcion == 4:
            if not tareas:
                print("No hay tareas para marcar como pendientes.")
            else:
                print("Seleccione el número de tarea que desea marcar como pendiente: ")
                ver_tareas(tareas)

                try:
                    num_tarea = int(input("Número de tarea: "))
                    if 1 <= num_tarea <= len(tareas):
                        indice = num_tarea - 1
                        tareas[indice]["completada"] = False
                        print(
                            f"Tarea {tareas[indice]['nombre']} marcada como pendiente."
                        )
                    else:
                        print("Número de tarea inválido.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

        elif opcion == 5:
            if not tareas:
                print("No hay tareas para eliminar.")
            else:
                print("Seleccione el número de tarea que desea eliminar: ")
                ver_tareas(tareas)

                try:
                    num_tarea = int(input("Número de tarea: "))
                    if 1 <= num_tarea <= len(tareas):
                        indice = num_tarea - 1
                        tareas.pop(indice)
                        print(
                            "Tarea eliminada."
                        )
                    else:
                        print("Número de tarea inválido.")
                except ValueError:
                    print("Por favor, ingrese un número de tarea valido válido.")

        elif opcion == 6:
            mostrar_configuracion()

        elif opcion == 7:
            print("Saliendo del programa...")

        else:
            print("Opción inválida.")

    except ValueError:
        print("Ingrese un número de opción válido.")


# Fin Main
