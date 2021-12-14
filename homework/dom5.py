
def bytecode(a: list):
    """Преобразует список строк, в список байт кодов"""
    byte = []
    for i in a:
        byte.append(i.encode())
    return byte


def decodebyte(a: list):
    """Преобразуетсписок список байт кодов, в список строк."""
    decode = []
    for i in a:
        decode.append(i.decode())
    return decode


def first_problem():
    """Шифрует список строк в байт коды и декодирует"""
    s = ["Как дела?", "Good luck have fun", "Nothing to do", "Что делаешь"]
    s = bytecode(s)
    print(s)
    print(decodebyte(s))


def second_problem():
    """
    Считывает из файла Input.txt, количество С,Н,О
     и выводит максимально возможное число молекул спирта
                в Output.txt 
    """
    try:
        with open('Input.txt', 'r') as f:
            Cnum = int(f.readline())
            Hnum = int(f.readline())
            Onum = int(f.readline())
            if Cnum < 0 or Hnum < 0 or Onum < 0:
                print("Отрицательными не могут быть молекулы")
                return -1
            Cnum //= 2
            Hnum //= 6
            otvet = min(Cnum, min(Hnum, Onum))
            with open("Output.txt", "w") as g:
                g.write(str(otvet))

    except (FileNotFoundError, ValueError):
        print("Проверьте файл")


def third_problem():
    pass
