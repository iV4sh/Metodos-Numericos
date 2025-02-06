import numpy as np
from scipy.optimize import bisect

def funcion(x):
    return x**5 - 6 * x**4 + 2 * x**3 + 20 * x**2 - 27 * x + 10

intervalos = [
    (-3, -2), (-3, 1), (4, 6)
]

for a, b in intervalos:
    print(bisect(funcion, a, b))

##############################################################

# COMENTARIO:
# SOLO ENCONTRE 3 SOLUCIONES