import math

def area(r):
    """
    Вычисляет площадь круга.

    Параметры:
    r (float): Радиус круга.

    Возвращает:
    float: Площадь круга.
    """
    return math.pi * r * r

def perimeter(r):
    """
    Вычисляет периметр круга.

    Параметры:
    r (float): Радиус круга.

    Возвращает:
    float: Периметр круга.
    """
    return 2 * math.pi * r
