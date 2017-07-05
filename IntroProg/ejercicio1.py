#raizX1: num num num -> float
#Calcula la raiz resultante x1 de una ecuacion de segundo grado
#Ejemplo : raizX1(1, 3, -4) debe producir 1.0
def raizx1(a, b, c):
    factor2 = 4 * (a * c)
    raiz = (b ** 2 - factor2) ** 0.5
    numerador = -b + raiz
    denominador = 2 * a
    resultado = numerador / denominador
    return resultado

#Test raizX1
assert raizx1(1, 3, -4) == 1.0

#raizx2 : num num num -> float 
#Calcula la raiz resultante x2 de una ecuacion de segundo grado
#Ejemplo : raizX2(1, 3, -4) debe producir -4.0

def raizx2(a, b, c):
    factor2 = 4 * (a * c)
    raiz = (b ** 2 - factor2) ** 0.5
    numerador = -b - raiz
    denominador = 2 * a
    resultado = numerador / denominador
    return resultado

#Test raizx2
assert raizx2(1, 3, -4) == -4.0

#print(raizx1(1, 3, -4))
#print(raizx2(1, 3, -4))