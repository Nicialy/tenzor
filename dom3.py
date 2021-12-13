import webbrowser
from webcolors import rgb_to_name
from random import randint


def bubble():
    """ Cортировка списка методом пузырька"""

    s = []

    while True:

        dvig = input(
            "Введите элемент списка.\n Список сразу будет выведен в сортировке пузырька.\nЧтобы выйти введит q \n")
        if dvig.find('q') != -1:
            break
        s.append(dvig)
        if len(s) > 1:
            for i in range(len(s)-1):
                for j in range(len(s)-i-1):
                    if s[j] > s[j+1]:
                        s[j], s[j+1] = s[j+1], s[j]

        # s.sort()
        print(s)


def second():
    """
    Cловарь цветов,
    в котором ключ - название или кодировка цвета;
    значение - кортеж из rgb этого цвета
    """
    rgb1 = (0, 0, 0)
    rgb2 = (192, 192, 192)
    rgb3 = (255, 0, 255)
    rgb4 = (255, 0, 0)
    rgb5 = (0, 0, 128)
    rgb6 = (255, 255, 0)
    # мне было лень писать цвета...

    d = {rgb_to_name(rgb1): rgb1, rgb_to_name(rgb2): rgb2, rgb_to_name(
        rgb3): rgb3, rgb_to_name(rgb4): rgb4, rgb_to_name(rgb5): rgb5, rgb_to_name(rgb6): rgb6}
    print(d)


def third():
    """
    Заполняет два случайных набора чисел
    Указывает какие элементы:
        входят одновременно в оба;
        входят только в первое, но не входят во второе;
        входят только во второе, но не входят в первое;
        входят в первое или во второе, но не в оба из них одновременно.
    """

    s1 = set()
    s2 = set()
    for i in range(7):
        s1.add(randint(0, 10))
        s2.add(randint(0, 5))
    print(f"Первое множество : {s1} , Второе множество: {s2}")
    print(f'Входят одновременно в оба : {s1.intersection(s2) }')
    print(
        f'Входят только в первое, но не входят во второе: {s1.difference(s2)}')
    print(
        f'Входят только во второе, но не входят в первое: { s2.difference(s1)}')
    print(
        f'Входят в первое или во второе, но не в оба из них одновременно {s1.symmetric_difference(s2)}')


def inventory():
    """Игровой инвентарь"""
    maxweight = 150.0
    now = 0
    inventplayer = {}
    lvl = 1
    url = 'https://store.playstation.com/ru-ru/product/EP0001-CUSA05625_00-DLCEXPENSIONS002'
    url2 = 'https://store.playstation.com/ru-ru/product/EP0001-CUSA05625_00-ACEPACKDELUXE000'
    while True:
        dvig = input(f"""
            Ваш уровень инвентаря {lvl}
            Ваш инвентарь заполнен на  {now} из  {maxweight}
            Вы попали в свой инвентарь что вы хотите сделать?
            1. Добавить предмет
            2. Удалить предмет
            3. Вывести весь инвентарь
            4. Как повысить уровень инвентаря?
            q. Выйти из инвентаря
            """)
        if dvig.find('q') != -1:
            break
        if dvig.find('1') != -1:
            addinv = input(" Введите  имя предмета :")
            key = addinv
            addinv = input(" Введите  вес предмета :")
            value = float(addinv)
            if value <= 0:
                print(
                    "Вес предмета не может быть отрицательным, у нас тут нету экзотической материи")
            else:
                if (now+value) > maxweight:
                    print(
                        "Инвентарь будет переполнен!!!!!!!!!11111 \n Чтобы улучшить инвентарь повысьте его урвоень!!")
                else:
                    inventplayer.update({key: value})
                    now += value

        if dvig.find('2') != -1:
            delpredmet = input("Введите предмет который хотите удалить:\n")

            value = inventplayer.get(delpredmet)
            if inventplayer.pop(delpredmet, False):
                print(f" Предмет {delpredmet} удален")
                now -= value
            else:
                print(f"Предмет {delpredmet} не найден")
        if dvig.find('3') != -1:
            print(inventplayer)
        if dvig.find('4') != -1:
            while True:
                buydlc = input("""
                    Чтобы повысить уровень инвентаря убивайте монстров или купите его.
                    1. Почему я не вижу никаких монстров?
                    2. Где купить уровень ?
                    q. Назад
                    """)
                if buydlc.find('q') != -1:
                    break
                if buydlc.find('1') != -1:
                    print("У вас неприобретено DLC, купите его и  новый скайрим тоже")
                    webbrowser.open(url, 0)
                if buydlc.find('2') != -1:
                    webbrowser.open(url2, 0)
