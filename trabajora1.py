import shutil
from multiprocessing import Process
import multiprocessing
from multiprocessing import Value
resultado_compartido = Value('i', 0)

def sumar(x,y,resultado):
    resultado.value = x + y

def restar(x,y, resultado):
    resultado.value = x - y

def mul(x,y, resultado):
    resultado.value = x * y

def div(x,y, resultado ):
    resultado.value= x//y

def is_par(x):
    if x/2==0:
        return True
    else: 
        return False

def mostrar_menu():
    print("1) Operaciones Básicas (+,-,x,/) | esPar? | esPrimo?")
    print("4) Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            p1 = Process(target=sumar, args=(numero1,numero2, resultado_compartido))
            p2 = Process(target=restar, args=(numero1,numero2, resultado_compartido))
            p3 = Process(target=mul, args=(numero1,numero2, resultado_compartido))
            p4 = Process(target=div, args=(numero1,numero2, resultado_compartido))
            p1.start()
            p1.join()
            resultado = resultado_compartido.value
            p2.start()
            p2.join()
            resultado2 = resultado_compartido.value
            p3.start()
            p3.join()
            resultado3 = resultado_compartido.value
            p4.start()
            p4.join()
            resultado4 = resultado_compartido.value 
            data = [
                ["Operación", "Edad", "Ciudad"],
                ["Suma: "+str(resultado), 30, "Londres"],
                ["Resta: "+str(resultado2), 25, "Nueva York"],
                ["Mult.: "+str(resultado3), 30, "Los Ángeles"],
                ["División: "+str(resultado4), 22, "Chicago"]
            ]
            # Encabezados
            print(data[0][0], data[0][1], data[0][2])

            # Línea separadora
            print("-" * 30)

            # Filas de datos
            for row in data[1:]:
                print(row[0], row[1], row[2])
                    
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
    numero1=int(input("Introduce un número: "))
    numero2=int(input("Introduce un número: "))
    main()