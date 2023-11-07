import pandas as pd 
from math import factorial

s = pd.Series([2,4,6,8])
s2 = pd.Series(['2','4','6','8'])

#suma
print(s+1)

#multiplicacion
print(s2*2)

#total de elementos
print(s.count())

#suma total
print(s2.sum())

#desviacion estandar
print(s.std())

"""Regresa una estructura Serie que contiene elementos que describen a la serie original.

Contiene, en ese orden, la siguiente información:

La cantidad total de elementos

La suma

La media

La desviación estándar

El mínimo

Los cuartiles

El máximo """

print(s.describe())

"""Función apply(f)
Regresa una estructura Serie que contiene los elementos resultantes de ejecutar una función a cada uno de los
elementos de la serie original. La función puede ser, o bien una función definida y creada por nosotros mismos 
o una función importada de alguna librería."""

print(s.apply(factorial))
