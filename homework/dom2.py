import math


def first():
    """
    Cкрипт для движения персонажа влево, вправо,
    вверх и вниз по координатам x и y по координатной оси,
    начальная позиция персонажа (0;0)
    """
    x = 0
    y = 0
    dvig = input("Введите куда сдвинуться и насколько?\n")
    if dvig.find('Вправо') != -1:
        x += int(dvig[dvig.find('Вправо')+6:])
    if dvig.find('Влево') != -1:
        x -= int(dvig[dvig.find('Влево')+5:])
    if dvig.find('Вниз') != -1:
        y -= int(dvig[dvig.find('Вниз')+4:])
    if dvig.find('Вверх') != -1:
        y += int(dvig[dvig.find('Вверх')+5:])
    print(f"Вы в позиции ({x},{y})")


def second():
    """
    Cкрипт для движения персонажа влево, вправо,
    вверх и вниз по координатам x и y по координатной оси,
    начальная позиция персонажа (0;0)
    q - стоп  слово для выхода из цикла.
    """
    x = 0
    y = 0
    while True:

        dvig = input(
            "Введите куда сдвинуться и насколько? Чтобы выйти введит q \n")
        if dvig.find('q') != -1:
            break
        if dvig.find('Вправо') != -1:
            x += int(dvig[dvig.find('Вправо')+6:])
        if dvig.find('Влево') != -1:
            x -= int(dvig[dvig.find('Влево')+5:])
        if dvig.find('Вниз') != -1:
            y -= int(dvig[dvig.find('Вниз')+4:])
        if dvig.find('Вверх') != -1:
            y += int(dvig[dvig.find('Вверх')+5:])
        print(f"Вы в позиции ({x},{y})")
    print(f"Вы в позиции ({x},{y})")


def third():
    """Скрипт решения квадратного уравнения,
        c обработкой отрицательного дискриминанта"""
    print("Введите коэффициенты для уравнения, a не равно 0")
    print("ax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(f"Вы ввели уравнение {a}x^2+{b}x+{c}=0:")
    d = b ** 2 - 4 * a * c
    print(f"Дискриминант : {d}")
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"x1={x1} \n x2={x2}")
    elif d == 0:
        x = -b/(2*a)
        print(f"x={x}")
    else:
        x1 = complex(-b, math.sqrt(-d)) / (2*a)
        x2 = complex(-b, -math.sqrt(-d)) / (2*a)
        print(f"x1 = {x1} \n x2 = {x2}")
