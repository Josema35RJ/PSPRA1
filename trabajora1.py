import shutil
from multiprocessing import Process
import multiprocessing

def is_par(x):
    if x/2==0:
        print('%s es par' %(x))
    else: 
        print('%s es impar' %(x))

def mostrar_menu():
    print("1) SUMA | esPar? | esPrimo?")
    print("2) RESTA | esPar? | esPrimo?")
    print("3) MULTIPLICACIÓN | esPar? | esPrimo?")
    print("4) DIVISIÓN | esPar? | esPrimo?")
    print("5) Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Has seleccionado la Opción 1")
            import time

            def my_process():
                     while True:
                      print("Running...")
                     time.sleep(1)

            if __name__ == '__main__':
                   process = multiprocessing.Process(target=my_process)
                   process.start()
                   time.sleep(5)
                   process.terminate()
            # Aquí puedes poner el código relacionado con la Opción 1
            def print_process_name():
              print(multiprocessing.current_process().name)

            if __name__ == '__main__':
                  processes = []
            for i in range(4):
               process = multiprocessing.Process(target=print_process_name)
               processes.append(process)
               process.start()

            for process in processes:
               process.join()
        elif opcion == "2":
            print("Has seleccionado la Opción 2")
            # Aquí puedes poner el código relacionado con la Opción 2
        elif opcion == "3":
            print('4')
        elif opcion == "4":
            print("Has seleccionado la Opción 4")
            break
        elif opcion == "5": 
            print("Has seleccionado la Opción 5")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()