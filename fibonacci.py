# En este ejemplo calculamos y mostramos los números de fibonacci hasta el 100
# iniciamos la secuencia de fibonacci con los dos primeros números.
F0 = 0
F1 = 1
#calculamos el número que sigue.
Fn = F0+F1

print("La secuencia de fibonacci hasta antes del 100 es:")
print(F0)
print(F1)
while Fn < 100000:
    print(Fn)
    F0 = F1
    F1 = Fn
    Fn = F0+F1
