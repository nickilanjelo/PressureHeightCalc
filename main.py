from math import exp
from decimal import Decimal

PRESSURE = 760
G_BOOST = 9.81
AIR_MASS = 0.029
GAS_CONST = 8.31
PRESSURE_CONST = 133.33


def calc_height_internal(h, t):
    x = (- AIR_MASS * G_BOOST * h) / (GAS_CONST * to_kelvin(t))
    calculated = Decimal(to_pascal(PRESSURE)) * Decimal(exp(x))
    return from_pascal(calculated)


def to_pascal(pressure_mm):
    return pressure_mm * PRESSURE_CONST


def from_pascal(pascal):
    return Decimal(pascal) / Decimal(PRESSURE_CONST)


def to_kelvin(celsius):
    return 273 + celsius


height = int(input('Введите высоту: '))
temp = int(input('Введите температуру: '))
print(calc_height_internal(height, temp))
