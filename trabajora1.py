from multiprocessing import Process, Value, Pool
import multiprocessing
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import os
import errno

resultado_compartido = Value('i', 0)
listimages = ["camaro.jpg", "mclaren.jpg", "MustangDemon.jpg"]

#--------------------------OPCION 1 MENU-----------------------
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

#-------------------------------------------------------------------
#---------------------------OPCION 2  MENU---------------------------

def cuadrado(x):
        print('%s al cuadrado es %s' % (x, int(x)**2))

def raiz (x):
        print('%s su raiz es %s' % (x, int(x)**0.5))
        
def factorial (x):
        resultado = 1 
        for i in range(1, int(x) + 1):
         resultado *= i
        print('%s su factorial es  ' %(x) + str(resultado))
        
#------------------------------------------------------------------
#-----------------------OCPION 3 MENU-----------------------------
def invert_color(pixel):
    r, g, b = pixel #Extraemos de cada pixel  los componentes r, g,b (colores primarios)
    return 255 - r, 255 - g, 255 - b #Aplicamos a cada uno resta de 255 para invertirlos

def process_image(image_path):
    # Cargar la imagen
    image = Image.open(image_path)
    image = np.array(image)
     # Crear un objeto Pool
    pool = Pool()

    # Aplicamos el metodo de inversion de color a cada pixel de la imagen
    result = pool.map(invert_color, [pixel for row in image for pixel in row]) #Hacemos de la matrix un objeto plano, en una lista unidimensional de píxeles
    #Para que realizamos esto simplemente para mejorar el rendimiento y hacerlo mas facil, ademas de esto para hacer el metodo mas compatible ya que por ejemplo
    #esta libreria Pil necesita que le llegue asi los datos para trabajar

    # Reeordenamos todo el array para que salga la imagen igual
    result = np.array(result).reshape(image.shape)

    # Convertimos el resultado a una imagen y guardarla
    result_image = Image.fromarray(result.astype('uint8')) #Aqui convertirmos los valores de los elementos de la matriz (los pixeles con valores de  0 y 2551) a enteros normales
    try:
        os.mkdir('imagenescolorinvertido')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    result_image.save('imagenescolorinvertido/imagen_colorivertido'+ image_path)
    
#--------------------------------------------------------------------
#-----------------------OPCION 4 MENU------------------------------

def EscaladoImagen(imagen):
    img = Image.open(imagen)
    #Reescalamos las imagenes
    img.resize((2160,1440))
    try:
        os.mkdir('imagenesescaladas')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    img.save('imagenesescaladas/Escalado' + imagen)
    
def ImagenNitidez(imagen1):
    img = Image.open(imagen1)
    #Mejoramos la nitidez de la imagen
    imgnitida = img.filter(ImageFilter.SHARPEN)
    try:
        os.mkdir('imagenesnitidas')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    imgnitida.save('imagenesnitidas/Nitidez'+ imagen1)

def ConstrasteImagen(imagen2):
    img = Image.open(imagen2)
    #Aplicamos contraste a la imagen
    imgmejorada =ImageEnhance.Contrast(img)
    #Mejoradas la imagen en 1.4 para que se vea mejor, depues del contraste aplicado antes
    imgmejorada2 =imgmejorada.enhance(1.4)
    try:
        os.mkdir('imagenescontrastadas')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    imgmejorada2.save('imagenescontrastadas/Contraste'+ imagen2)

def ImagenRotacion(imagen3):
    img = Image.open(imagen3)
    #Aplicamos una rotacion a cada imagen
    img = img.rotate(20)
    try:
        os.mkdir('imagenesrotadas')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    img.save('imagenesrotadas/Rotada'+ imagen3)
#------------------------------------------------------------------
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
            #Realizamos calculos un poco mas complejos que antes a los numeros de un array
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
            #En esta opcion cogemos varias imagenes y le realizamos una inversion de color a cada pixel
                p1 = Process(target=process_image, args=(listimages[0],))
                p2 = Process(target=process_image, args=(listimages[1],))
                p3 = Process(target=process_image, args=(listimages[2],))
                
                p1.start()
                p2.start()
                p3.start()
            
                p1.join()
                p2.join()
                p3.join()
                while True:
                    opcion = input("Elige una opción (1. Camaro 2.Mclaren 3.Mustang 4.Salir):")
                    if opcion == "1":
                        Imagen1=Image.open("imagenescolorinvertido/imagen_colorivertidocamaro.jpg")
                        Imagen1.show()
                    elif opcion == "2":
                        Imagen2=Image.open("imagenescolorinvertido/imagen_colorivertidomclaren.jpg")
                        Imagen2.show()
                    elif opcion == "3":
                        Imagen3=Image.open("imagenescolorinvertido/imagen_colorivertidoMustangDemon.jpg")
                        Imagen3.show()
                    elif opcion == "4": 
                        print("VUELTA AL MENÚ")
                        break
                    else:
                        print("Opción no válida. Por favor, elige una opción válida.")

                    
                    
               
        elif opcion == "4":
              #En esta opcion cogemos varias imagenes y aplicamos en cada proceso un filtro o cambio al mismo tiempo
              #una vez terminen se guardaran con el filtro aplicado al nombre del archivo
              for image in listimages:
               p1 = Process(target=EscaladoImagen, args=(image,))
               p2 = Process(target=ImagenNitidez, args=(image,))
               p3 = Process(target=ConstrasteImagen, args=(image,))
               p4 = Process(target=ImagenRotacion, args=(image,))
              

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