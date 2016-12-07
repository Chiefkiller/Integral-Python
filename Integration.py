import scipy.integrate
import numpy


def f(x, a, b):
    return (1 / numpy.sqrt(2 * numpy.pi * (a ** 2))) * numpy.exp(-((x - b) ** 2 / (2 * a ** 2)))


a = input('Standardabweichung: ')
b = input('Erwartungswert: ')
ug = input('Untere Integrationsgrenze: ')
og = input('Obere Integrationsgrenze: ')

print scipy.integrate.quadrature(f, ug, og, args=(a, b))