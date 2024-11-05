# -*- coding: utf-8 -*-
"""Python_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OcsXAHOn9YRW8FEJGKvxMxOK_FzdWIAx
"""

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

df_bestsellers=pd.read_excel('/content/drive/MyDrive/Colab Notebooks/bestsellers+with+categories.xlsx')
df_bestsellers

# Opcional: usa el pd.set_option() para mostrar todas las filas de un dataframe por defecto

"""# Crear un DataFrame"""

# leer el archivo csv "bestsellers with categories" (data sobre los 50 libros más vendidos de Amazon de 2009 a 2019.)
df_bestsellers

# acceder al atributo shape
df_bestsellers.shape

# encontrar el tipo de data de cada columna
df_bestsellers.dtypes

"""# Mostrar un DataFrame"""

# mostrar primeras 5 filas de un dataframe
df_bestsellers.head(5)

# encontrar valores estadisticos de un dataframe (mean, std, min, max)
df_bestsellers.describe()

"""# Agregar una nueva Columna"""

# Tu tarea es crear una columna llamada 'Critic Rating' que deberia tener numeros random enteros entre 1 y 4

# 1.importar numpy y crear 550 numeros random enteros entre 1 y 4
aleatorio=np.random.randint(1,4,size=550)

# 2.agregar nueva columna 'Critic Rating' al dataframe usando los numeros random creados
df_bestsellers['Critic Rating']=aleatorio
df_bestsellers
# Obs: Los numeros aleatorios en la columna 'Critic Rating' seran diferentes entre tu solucion y la mia, pero vamos a concetrarnos en el codigo en esta seccion.

# mostrar 5 primeras filas
df_bestsellers.head(5)

"""# Atributos, Metodos y Funciones Basicas"""

# acceder al atributo "columns"
df_bestsellers.columns

"""# Seleccionar 2 o Mas Columnas de un Dataframe"""

# mover la columna 'Critic Rating' entre las columnas "User Rating" y "Reviews" Luego actualizar el dataframe
nuevo_orden=['Name', 'Author', 'User Rating','Critic Rating', 'Reviews', 'Price', 'Year', 'Genre']
df_bestsellers=df_bestsellers.reindex(columns=nuevo_orden)
df_bestsellers
# Tip: Copiar y pegar los nombres de columna obtenidos con el atributo "columns" y reordenar los elementos usando [[]]

# mostrar 5 primeras filas
df_bestsellers.head(5)

"""# Operaciones en Dataframes"""

# crear una columna llamada "Average Rating" usando la sigueinte formula: Average Rating = (User Rating + Critic Rating)/2
df_bestsellers['Average Rating']=(df_bestsellers['Reviews']+df_bestsellers['Critic Rating'])/2
df_bestsellers

# usar la funcion "round" para redondear los valores del dataframe a 1 decimal y actualizar el dataframe
df_bestsellers.round(1)

"""# Contar Valores"""

# contar elementos en columna "Genre" por categoria y devolver la frecuencia relativa
df_bestsellers['Genre'].value_counts(normalize=True)*100

"""# Renombrar Columnas"""

# renombrar columnas "User Rating," "Critic Rating" y "Average Rating" a "UR," "CR" y "AR" Luego actualizar el dataframe con el parametro "inplace"
df_bestsellers.rename(columns={'User Rating':'UR','Critic Rating':'CR','Average Rating':'AR'}, inplace=True)
df_bestsellers

# mostrar 5 primeras filas
df_bestsellers.head(5)

# seleccionar solo columnas "Name", "Author", "UR", "CR", "AR" y "Year" y actualizar el dataframe
df_bestsellers[['Name', 'Author', 'UR', 'CR', 'AR', 'Year']]
df_bestsellers=df_bestsellers[['Name', 'Author', 'UR', 'CR', 'AR', 'Year']]
df_bestsellers

"""# Ordenar el dataframe"""

# ordenar el dataframe en forma descendente segun las columnas "UR" y "CR"
df_bestsellers.sort_values(['CR','AR'], ascending=False)