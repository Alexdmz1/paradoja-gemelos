
#En este tratamos introducción a la relatividad especial
# Paritcularmente queremos conocer la dilatación del tiempo

# Una nave viaja de la tierra en linea recta a una velocidad relativa v hacia otro planeta que esa a x años luz
#de distancia.

#Este programa en python pregunta al usuario la distancia x y la rapidez
# como fracción

from math import sqrt

# definimos la rapidez de la luz

c=3e8 #m/s

# Ecuación


print("Escribe la distancia en años luz hasta el planeta que quieres viajar")
x=float(input())

# antes de hacer cualquier cosa debemos convertir los años luz a metros
x=x*9.461e15 # esta distancia es en metros


print("Escribe la rapidez a la que viaja la nace como factor de c de (0 a 0.9999)")
v=float(input())
while v<0 or v>0.999999:
  print("Escribe la rapidez a la que viaja la nace como factor de c de (0 a 0.9999)")
  v = float(input())

v=v*c
t0=x/v
print(" a)Según el observador que viaja en la nave, el tiempo de viaje es:")
print(t0, "segundos")
print("Esto equivale a:")
print(t0/60, "minutos")
print(t0/3600,"horas")
print(t0/3600/24, "días")
print(t0/3600/24/365*12,"meses")
print(t0/3600/24/365, "años")

print("*******************************")
t=t0/sqrt(1-v**2/c**2)
print("b)Según el observador que se queda en la tierra, el tiempo de viaje es:")
print(t, "segundos")
print("Esto equivale a:")
print(t/60, "minutos")
print(t/3600,"horas")
print(t/3600/24, "días")
print(t/3600/24/365*12,"meses")
print(t/3600/24/365, "años")