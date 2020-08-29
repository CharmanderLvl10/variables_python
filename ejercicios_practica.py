#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: Ejercicio 2 de la Clase Numero 2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Alejandro Villaboa"
__email__ = "alejandrocesarv@gmail.com"
__version__ = "Clase Numero 2"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculo, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    numero_1 = 2.5
    numero_2 = 3.5

    suma = numero_1 + numero_2
    print('El resultado de la suma es', suma)

    resta = numero_1 - numero_2
    print('El resultado de la resta es', resta)

    Multiplicación = numero_1 * numero_2
    print('El resultado de la mulplicacion es', Multiplicación)

    Division = numero_1 / numero_2
    print('El resultado de la division es', Division)

    Exponente = numero_1 ** numero_2
    print('El resultado de la exponente es', Exponente)

    
def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''
    print('Ingrese su Nombre y Apellido:')
    nombre = str(input())
    
    print('Ingrese su DNI:')
    dni = int(input())

    print('Ingrese su edad:')
    edad = int(input())

    print('Ingrese su altura:')
    altura = float(input())
    
    print('Nombre y DNI ingresado:', nombre, dni)
    print('Nombre, Edad y Altura ingresada:', nombre, dni, altura)


def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''

    print('Ingrese el Nombre y Apellido del Padre:')
    nombre_1 = str(input())
    print('El Nombre ingresado del Padre es:', nombre_1)

    print('Ingrese el Nombre y Apellido de la Madre:')
    nombre_2 = str(input())
    print('El Nombre ingresado de la Madre es:', nombre_2)

    print('Ingrese el Nombre del Hijo/a:')
    nombre_3 = str(input())
    print('El Solamente el Nombre del Hijo/a es:', nombre_3)

    nombre_padre, apellido_padre = nombre_1.split(' ')
    nombre_madre, apellido_madre = nombre_2.split(' ')

    print('El Nombre de Familia Completo del Hijo/a es:', nombre_3, apellido_padre, apellido_madre)


def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    # Los nombres que elegi son Pablo Gomez y Ana Gomez
    print('Ingrese el primer nombre y apellido de su familia:')
    nombre_1 = str(input())
    print('El primer nombre ingresado es:', nombre_1)

    print('Ingrese el segundo nombre y apellido de su familia:')
    nombre_2 = str(input())
    print('El segundo nombre ingresado es:', nombre_2)

    nombre_familia_1, apellido_familia_1 = nombre_1.split(' ')
    nombre_familia_2, apellido_familia_2 = nombre_2.split(' ')

    persona = apellido_familia_1 in apellido_familia_2

    print(nombre_familia_1, 'es pariente de', nombre_familia_2, '?:', persona)


def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''

    print('Ingrese su nombre y apellido sin mayusculas:')
    nombre_1 = str(input())
    nombre_01, apellido_01 = nombre_1.split(' ')
    nombre_0 = nombre_01.capitalize()
    apellido_00 = apellido_01.capitalize()
    print('Su nombre correcto se escribe:', nombre_0, apellido_00)

    print('Ingrese su nombre y apellido solo en minuscula:')
    nombre_2 = str(input())
    nombre_mayusculas = nombre_2.upper()
    print('Su nombre en mayusculas es:', nombre_mayusculas)

    print('Ingrese su nombre y apellido solo en mayusculas:')
    nombre_3 = str(input())
    nombre_001, apellido_001 = nombre_3.split(' ')
    nombre_002 = nombre_001.lower()
    apellido_002 = apellido_001.lower()
    print('Su nombre en minusculas es:',nombre_002, apellido_002)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
