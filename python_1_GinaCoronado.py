# -*- coding: utf-8 -*-
"""Python_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ISRDh-JBV_ZG8KiMjL5I2YM0SdU2l7Md

**Buenos días** estoy aprendiendo ptyhon, pero a esta es super duro.
"""

#Esto es una broma yo no quiero ser millonario
print('Diosito no me abandone quiero ser millonario')

#Este soy yo
print("Hola soy Michael Rodriguez, tengo 31 años me gusta el futbol")

"Sali con tu mujer ¿Que?, sali con tu mujer ¿que? SALI CON TU MUJER"

"""**TIPOS DE DATOS**"""

#Tipo de dato entero, en ingles integer y la abreviatura para python es int
type(24)

#Tipo de dato flotante que en español, lo conocemos como decimal su abreviatura es float
type(9.8)

#Boleanos son tipos de datos que solo pueden tener dos valores el true (verdadero) o el false (Falso) su abreviatura es bool
type(True)

#Tipos de datos cadena, en ingles strings, siempre deben tener comillas su abreviatura es str
type("en algun lugar de la mancha cuyo nombre no puedo acordarme...")

"""Metodos de las cadenas, las cadenas tienen funciones pequeñas que me ayudan a formatearlas"""

print("Hola estoy aprendiendo python".upper())#Este metodo me sirve para poner mayusculas
print("con pythOn pueDo pediR Un aumENto".lower())#Este metodo me sirve para poner en minusculas
print("Cien años de soledad".title())#Este metodo me sirve para poner en mayuscula cada inicio de palabra

#Para contar las letras de una cadena puedo usar el metodo count
print("Que hay que poder hacer para aprender python".count('a'))

print("""Mi edad es 31 años
mi genero es masculino""")

#como reemplazar un valor dentro de uuna cadena utilizando replace
print("Hola soy michael rodriguez".replace('m','M'))

print("michael RodRiguez camaRgo".replace('R',"r"))

"""**Variables**
Son espacios de memoria que nos sirven para guardar información particular, deben tener un nombre que nos ayude a identificar su contenido
"""

#Para declarar una variable se usa nombre de la variable, el signo igual y el valor
#ejemplo: edad=13
nombre="Michael Steve"
apellido="Rodriguez Camargo"
edad=31
estado_civil="union libre"

nombre

apellido

edad

estado_civil

#nombre de mi hijo que no tengo
hijo_nombre="pachito"
hijo_apellido="mentiras"

hijo_apellido="verdades"

hijo_nombre

hijo_apellido

nombre='Michael'
apellido='Rodriguez'
edad=31
estado_civil='union libre'
estatura_cm=160
datos_personales=[nombre,apellido,edad,estado_civil,estatura_cm]

datos_personales

familiares=[]

familiares.append('viviana')#incluir en una lista vacia ej en familiares

familiares.append('maria')
familiares.append('alvaro')
familiares.append('juliana')
familiares

familiares.insert(1,33)# al insertar se debe hacer de manera independiente no en un solo bloque

nombre_2=input("ingresa tu nombre:") #input sirve para tomar datos de usuarios
print ("la verdad hoy estas terrible,",nombre_2)

#Para remover datos de las listas utilizo el metodo remove

paises=['Venezuela','Colombia','Rusia','Peru','Brasil']

paises.remove("Rusia")
paises

# para eliminar por posicion utilizo pop
paises.pop(1)
paises

#para eliminar definitivamente se utiliza del
del paises [0]

paises



#ordenar las listas, las puedo ordenar de mayor a menor o alfabeticamente con el metodo sort
paises.sort()
paises

digitos=[2,4,8,6,1,9]
digitos.sort()
digitos

digitos.sort(reverse=True)
digitos

paises.sort(reverse=True)
paises

paises_copia_verdadera=paises.copy()
paises_copia_verdadera

paises_copia_verdadera_2=paises[:]
paises_copia_verdadera_2

"""Diccionarios: son tipos de datos que tienen una llave y un valor, a la combinación de llave con valor, se le conoce como item en los diccionarios puedo usar metodos parecidos a los de las listas"""

diccionario_ing_esp={"casa":"house","entender":"understand","sediento":"thirty","rojo":"red","ocupado":"bussy"}
diccionario_ing_esp

#para ver un valor de una llave determinada lo hago de la siguiente manera
diccionario_ing_esp['casa']

#para traer todas las llaves de un diccionario, puedo utilizar el metodo keys
diccionario_ing_esp.keys()

#para traer los valores de un diccionario, puedo utilizar el metodo values
diccionario_ing_esp.values()

#para traer todo el diccionario
diccionario_ing_esp

diccionario_ing_esp.items()

type(diccionario_ing_esp)

#para agregar un nuevo elemento a un diccionario
diccionario_ing_esp["azul"]="blue"
diccionario_ing_esp

#para actualizar el diccionario, o añadir de otra forma
diccionario_ing_esp.update({"negro":"black"})
diccionario_ing_esp

#tambien puedo agregar una lista dentro de un diccionario
diccionario_ing_esp.update({"gris":"grey","pronombres":["he","she","it"]})
diccionario_ing_esp

diccionario_ing_esp.values()

#para borrar vamos a utilizar el metodo pop
diccionario_ing_esp.pop("gris")
diccionario_ing_esp

# metodo del
del diccionario_ing_esp ["pronombres"]
diccionario_ing_esp



"""operadores logicos se usan para comprobar condiciones y devolver true o false, dependiendo cual sea el caso, son esenciales para la toma de decisiones y para la creacion de la logica de programacion

"""

#el primero es AND que traduce y
print("operador AND (que significa y)")
print("para que Y sea verdadero todas las condiciones deben ser verdaderas")
5>3 and 5<10

5<3 and 5<10

# para usar O se usa la palabra reservada or en or por lo menos una de las condiciones debe ser verdadera
5<3 or 5<10

5<3 or 5>10

# existe otro operador logico que es el NOT
print("operador not (negación logica)")
not 5>3

"""operaciones matematicas, en este momento se utilizaran las mas basicas que son el lenguaje para la programcion, suma, resta, multiplicación, division, potenciacion y modulo"""

# suma se representa con el simbolo + y sirve tambien para concatenar
6+5

#resta se representa con el simbolo -
6-5

#Multiplicacion se representa con el simbolo *
2*6

edad_usuario=int(input('Hola para ingresar por favor comprueba tu edad'))
if edad_usuario >= 18:
  print('Bienvenido, puedes apostar tu casa')
elif edad_usuario >=13:
  print('Eres un adolecente,pero no te preocupes TE ESPERAMOS')
else:
  print('Eres pequeño, no puedes apostar')

Mayor_Menor=int(input('Ingresa tu edad'))
if Mayor_Menor >= 18:
  print('Eres mayor de edad')
else:
    print('Eres menor de edad')

numero_1=int(input('ingresa un número'))
numero_2=int(input('ingresa un segundo numero'))
suma=numero_1+numero_2
multiplicación=numero_1*numero_2
resta=numero_1-numero_2
division=numero_1/numero_2
print('resultado de suma: ', suma)
print('resultado multiplicación', multiplicación)
print('resultado resta', resta)
print('resultado division', division)

"""**Ciclos y bucles:** Son estructuras de codigo que me permiten iterar sobre una estructura o un rango, existen dos tipos de ciclos mas usados, los for que significa para o los wait que significa mientras que."""

# de esta maner es la estructura de los ciclos for
#for <variable>int<lista o rango>:
#<ejecutable>
paises=['Rusia','Paraguay','Colombia','Argentina','Brasil']
paises

for i in paises:
 print (i)

for i in paises:
  if i == 'Brasil':
   print("este pais es infiltrado")

for numero, i in enumerate(paises):
  print(numero)
  print(i)

#Funcion len que me da una longitud de una regla
len(paises)

# Funcion "max" me sirve para mostrar el numero mas grande de un arreglo
max(1,5,6,7,4,3,4,5,9)

# funcion "min" me sirve para mostrar el valor mas bajo de un arreglo
min(3,5,7,8,2,5)

#Type nos sirve para saber el tipo de datos de una variable
type(paises)

#round me sirve para redondear decimales
round(3.141624,2)

# range para crear una secuencia de numeros tiene 3 argumentos el inicio, el final, el paso
contar=range(0,200,5)

for i in contar:
  print (i)

# funciones propias me sirve para reutilizar codigo
# la palabra reservada para declarar una funcion es "def"
def suma(a,b):
  resultado=a+b
  return resultado

# llamo la funcion declara anteriormente
suma(2,5)

def pan(pan,precio):
  precio_pan=pan*precio
  return precio_pan

cantidad=int(input("buenos dias cuanto pan necesita"))
valor=int(input("valor pan"))
pan(cantidad,valor)

def division(a,b):
  resultado_division=a/b
  return resultado_division

division(5,2)

"""#Ejercicio: escribe un programa que calcule el total de una compra de supermercado, el usuario debe ingresar el precio de dos productos y las cantidades que desee comprar de cada uno luego el programa debera permitir al usuario: sumar los precios de ambos productos. multiplicar los precios por las cantidades de productos para obtener el precio total restar un descuento del precio total (si el usuario tiene un cupon). Dividir el total entre dos personas por si desean dividir la cuenta.

dividir entre 0 / if b !=0: return a/b else: return print ("no se puede dividir entre 0)
"""

#Ejercicio: escribe un programa que calcule el total de una compra de supermercado, el usuario debe ingresar el precio de dos productos y las cantidades que desee comprar de cada uno luego el programa debera permitir al usuario: sumar los precios de ambos productos. multiplicar los precios por las cantidades de productos para obtener el precio total restar un descuento del precio total (si el usuario tiene un cupon). Dividir el total entre dos personas por si desean dividir la cuenta.
#Multiplicar
#Suma
#resta
#Division

def suma(a,b):
  suma_producto=a+b
  return suma_producto
def multiplicacion(a,b):
  resultado_multiplicacion=a*b
  return resultado_multiplicacion
def division(a,b):
  if b !=0:
    return a/b
  else:
    return print ("No se puede dividir entre 0")
def resta(a,b):
  resultado_resta=a-b
  return resultado_resta

print("Bienvenido a supermarket")
Precio_Producto_A=float(input("ingresa el precio del producto seleccionado"))
Cantidad_producto_A=int(input("ingresa la cantidad del producto seleccionado"))
Precio_Producto_B=float(input("ingresa el precio del producto seleccionado"))
Cantidad_producto_B=int(input("ingresa la cantidad del producto seleccionado"))
Operacion=(input("""Bienvenido como estas cuentame que quieres hacer
1. Sumar los precios de ambos productos
2. calcular el costo total multiplicando Precio * Cantidad
3. Aplicar un descuento al total
4. dividir el total entre dos personas
No olvides que solo puedes seleccionar 1,2,3 ó 4: """))
if Operacion=="1":
  total_precio=suma_producto(Precio_Producto_A,Precio_Producto_B)
  print(total_precio)