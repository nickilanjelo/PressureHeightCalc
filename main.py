from math import exp
from decimal import Decimal

PRESSURE = Decimal(760)
G_BOOST = Decimal(9.81)
AIR_MASS = Decimal(0.029)
GAS_CONST = Decimal(8.31)


def calc_height_internal(h, t):
    x = Decimal(- AIR_MASS * G_BOOST * h) / Decimal(GAS_CONST * to_kelvin(t))
    calculated = Decimal(to_pascal(PRESSURE)) * Decimal(exp(x))
    return Decimal(from_pascal(calculated))


def to_pascal(pressure_mm):
    return pressure_mm * Decimal(133.3)


def from_pascal(pascal):
    return pascal / Decimal(133.33)


def to_kelvin(temp):
    return 273 + temp


height = int(input('Введите высоту: '))
temp = int(input('Введите температуру: '))
print(calc_height_internal(Decimal(height), Decimal(temp)))
