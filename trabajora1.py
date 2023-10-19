import shutil

def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Has seleccionado la Opción 1")
            # Aquí puedes poner el código relacionado con la Opción 1
        elif opcion == "2":
            print("Has seleccionado la Opción 2")
            # Aquí puedes poner el código relacionado con la Opción 2
        elif opcion == "3":
            print("Has seleccionado la Opción 3")
            # Aquí puedes poner el código relacionado con la Opción 3
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()