#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    y3 = [i**4 for i in x]

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    fig = plt.figure()
    fig.suptitle("1° Ejercicio Profundización")

    ax1 = fig.add_subplot(3,1,1)
    ax1.plot(x,y1, color='red', label = "X**2")
    ax1.legend()
    ax1.set_facecolor("blue")

    ax2= fig.add_subplot(3,1,2)
    ax2.plot(x,y2,color='red',label = "X**3")
    ax2.legend()
    ax2.set_facecolor('whitesmoke')
    #ax2.set_xticklabels(" Probando")

    ax3 = fig.add_subplot(3,1,3)
    ax3.plot(x,y3,color='green',label= "X**4")
    ax3.legend()
    plt.show()

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = np.arange(0, 4*np.pi, 0.1)

    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x
    y1 =  [i for i in np.sin(x)]
    y2 = [i for i in np.cos(x)]
    
    fig = plt.figure()
    fig.suptitle("GRAPHIC DESIGN IS MY PASSION", color='white' , fontsize=22)
    fig.set_facecolor("brown")
    
    ax1 = fig.add_subplot(1,2,1)
    ax1.scatter(x,y1,color='blue', label='y1=Sen(X)')
    ax1.legend()
    ax1.set_facecolor('grey')
    ax1.grid(ls='dashed')
    ax1.set_title("Función Seno")
    ax1.set_xlabel('Valores de X')
    ax1.set_ylabel('Valores de Y')
    

    ax2 = fig.add_subplot(1,2,2)
    ax2.scatter(x , y2 , color='lightblue' , label='y2=Cos(X)' )
    ax2.legend()
    ax2.set_facecolor('whitesmoke')
    ax2.grid(ls='dotted')
    ax2.set_title("Función Coseno")
    ax2.set_xlabel("Valores de X")
    ax2.set_ylabel("Valores de Y")

    plt.show()


    
    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.


def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.
    
    fig = plt.figure() 

    fig.suptitle("Ejercicio 5", fontsize=25)
    
    ax = fig.add_subplot()
    ax.set_facecolor("turquoise")
    ax.bar(lenguajes, performance, width=0.5, color='white')
    ax.grid(ls='dotted',ms=100)

        
    plt.show()


def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico

    fig = plt.figure()
    fig.suptitle("Ejercicio 4")

    ax = fig.add_subplot()
    ax.pie()

def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    # signal_x = [....]
    # signal_y = [....]

    # plot(signal_x, signal_y)

    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    # filter_signal_x = [....]
    # filter_signal_y = [....]

    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    # ej5()
