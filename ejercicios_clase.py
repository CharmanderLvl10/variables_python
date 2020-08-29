#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: Ejercicio 1 de la Clase Numero 2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Alejandro Villaboa"
__email__ = "Alejandrocesarv@gmail.com"
__version__ = "Clase Numero 2"


def ej1():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 3.50 y 6.50 es 10.00

    # Suma
    suma = numero_1 + numero_2
    print('El resultado de la suma es', suma)

    # Resta
    resta = numero_1 - numero_2
    print('El resultado de la resta es ', resta)

    # División
    division = numero_1 / numero_2
    print('El resultado de la division es', division)

    # Multiplicación
    Multiplicación = numero_1 * numero_2
    print('El resultado de la Multiplicación es', Multiplicación)


def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('Ingrese el primer número real a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_4 = float(input())

    # Alumno: Imprima en pantalla los dos números reales solicitados
    # print(....)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma = numero_3 + numero_4
    print('El resultado de la suma es', suma)

    # Resta
    resta = numero_3 - numero_4
    print('El resultado de la resta es ', resta)

    # División
    division = numero_3 / numero_4
    print('El resultado de la division es', division)

    # Multiplicación
    Multiplicación = numero_3 * numero_4
    print('El resultado de la Multiplicación es', Multiplicación)


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo

    print('Su nombre completo es', nombre, apellido)
   
    nombre_completo = 'Alejandro Villaboa'
    cantidad_letras = len(nombre_completo)
    
    print('El nombre completo de', nombre_completo, 'y tiene', cantidad_letras, 'letras')

def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras

    # Mis palabra elegidas van a ser "Digital Video Disc" (DVD)
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

    acrónimo_1 = palabra_1 [0]
    acrónimo_2 = palabra_2 [0] 
    acrónimo_3 = palabra_3 [0]

    suma = acrónimo_1 + acrónimo_2 + acrónimo_3

    print('El acronimo de', palabra_1, palabra_2, palabra_3, 'es', suma)


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella

    # Mis palabras elegidas van a ser "Carrion y Bombon" (Carbon)
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados

    anagrama_1 = palabra_1 [0:3]
    anagrama_2 = palabra_2 [3:6] 

    suma = anagrama_1 + anagrama_2

    print('La primer palabra es', palabra_1, 'y tomamos', anagrama_1)
    print('La segunda palabra es', palabra_2, 'y tomamos', anagrama_2)
   
    print('El anagrama que formamos es', suma)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
