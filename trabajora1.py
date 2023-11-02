import shutil
from multiprocessing import Process, Value, Pool
import multiprocessing
from PIL import Image, ImageEnhance, ImageFilter
import time
import numpy as np


resultado_compartido = Value('i', 0)
listEscalado = ["imagem_2023_04_30_22184991439.jpg"]
listNitidez = ['']
listConstraste = ['']
listRotacion = ['']

def sumar(x,y,resultado):
    resultado.value = x + y

def restar(x,y, resultado):
    resultado.value = x - y

def mul(x,y, resultado):
    resultado.value = x * y

def div(x,y, resultado ):
    resultado.value= x//y
    
def is_par(x):
    if x % 2 ==0:
        print(f'{x} es PAR')
    else: 
        print(f'{x} es IMPAR')

def es_primo(x):
    for n in range(2, x):
        if x % n == 0:
            print(f'{x} NO es primo')
            return False
    print(f'{x} SI es primo')
    return True
def invert_color(pixel):
    r, g, b = pixel
    return 255 - r, 255 - g, 255 - b

def process_image(image_path):
    # Cargar la imagen
    image = Image.open("camaro.jpg")
    image = np.array(image)

    # Crear un objeto Pool
    pool = Pool()

    # Aplicar el filtro de inversión de color a cada pixel de la imagen
    result = pool.map(invert_color, [pixel for row in image for pixel in row])

    # Reshape del resultado para que tenga la misma estructura que la imagen original
    result = np.array(result).reshape(image.shape)

    # Convertir el resultado a una imagen y guardarla
    result_image = Image.fromarray(result.astype('uint8'))
    result_image.save('imagen_mejorada.jpg')


def cuadrado(x):
        print('%s al cuadrado es %s' % (x, int(x)**2))

def raiz (x):
        print('%s su raiz es %s' % (x, int(x)**0.5))
        
def factorial (x):
        resultado = 1 
        for i in range(1, int(x) + 1):
         resultado *= i
        print('%s su factorial es  ' %(x) + str(resultado))
        
def EscaladoImagen(imagen):
    img = Image.open(imagen)
    img.resize((2160,1440))
    img.save('Escalado' + imagen)
    listNitidez.append(img)
    
def ImagenNitidez(imagen1):
    img = Image.open(imagen1)
    imgnitida = img.filter(ImageFilter.SHARPEN)
    imgnitida.save('Nitidez'+ imagen1)
    listConstraste.append(imgnitida)

def ConstrasteImagen(imagen2):
    img = Image.open(imagen2)
    imgmejorada =ImageEnhance.Contrast(img)
    imgmejorada2 =imgmejorada.enhance(1.4)
    imgmejorada2.save('Contraste'+ imagen2)
    listRotacion.append(imgmejorada2)

def ImagenRotacion(imagen3):
    img = Image.open(imagen3)
    img = img.rotate(20)
    img.save('Final'+ imagen3)
    img.show()

def mostrar_menu():
    print("OPERACIONES NUMÉRICAS")
    print("1) Operaciones Básicas (+,-,x,/) | esPar? | esPrimo?")
    print("2) Potencia, Raiz, Factorial de una lista de Numeros")
    print("OPERACIONES CON IMAGEN")
    print("3) Invertir color pixel de Imagen")
    print("4) Procesos en Imagenes")
    print("5) Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            numero1=int(input("Introduce un número: "))
            numero2=int(input("Introduce un número: "))
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
            resultados = [resultado, resultado2, resultado3, resultado4]
            data = [
                ["Operaciones Básicas (+,-,*,/)"],
                ["Suma: "+str(resultado)],
                ["Resta: "+str(resultado2)],
                ["Mult.: "+str(resultado3), ],
                ["División: "+str(resultado4)]
            ]
            # Encabezados
            print(data[0][0])

            # Línea separadora
            print("-" * 30)

            # Filas de datos
            for row in data[1:]:
                print(row[0])
            
            
            print("¿Es el resultado par?")   
            for x in resultados:               
                p5 = Process(target=is_par, args=(x,))
                p5.start()
                p5.join()
                
            print("¿Es el resultado primo?")   
            for x in resultados:               
                p6 = Process(target=es_primo, args=(x,))
                p6.start()
                p6.join()
        elif opcion == "2":
            numeros = [3, 8, 5, 8, 4, 2]
            for x in numeros:
             print('Potencia y Raiz de ', x)
             p1 = Process(target=cuadrado, args=(x,))
             p2 = Process(target=raiz, args=(x,))
             p3 = Process(target=factorial, args=(x,))

             p1.start()
             p2.start()
             p3.start()

             p1.join()
             p2.join()
             p3.join()
             
             print('-------------------------------------------')
        elif opcion == "3":
            process_image("camaro.jpg")
        elif opcion == "4":
              #Array de varias Imagenes
              p1 = Process(target=EscaladoImagen, args=("camaro.jpg",))
              time.sleep(2)
              p2 = Process(target=ImagenNitidez, args=("camaro.jpg",))
              time.sleep(2)
              p3 = Process(target=ConstrasteImagen, args=("camaro.jpg",))
              time.sleep(2)
              p4 = Process(target=ImagenRotacion, args=("camaro.jpg",))
              

              p1.start()
              p2.start()
              p3.start()
              p4.start()

              p1.join()
              p2.join()
              p3.join()
              p4.join()
         
        elif opcion == "5": 
            print("FIN DEL PROGRAMA")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()