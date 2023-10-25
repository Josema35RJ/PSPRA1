import shutil
from multiprocessing import Process
import multiprocessing

def is_par(x):
    if x/2==0:
        print('%s es par' %(x))
    else: 
        print('%s es impar' %(x))

def mostrar_menu():
    print("1) Operaciones Básicas (+,-,x,/) | esPar? | esPrimo?")
    print("4) Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Has seleccionado la Opción 1")
        elif opcion == "2":
            print("Has seleccionado la Opción 2")
            # Aquí puedes poner el código relacionado con la Opción 2
        elif opcion == "3":
            print('4')
        elif opcion == "4":
            print("Has seleccionado la Opción 4")
        elif opcion == "5": 
            print("FIN DEL PROGRAMA")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()