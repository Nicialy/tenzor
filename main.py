import decimal
import math


def first():
    f=input('Введите первое число:')
    
    f2=input('Введите второе число:')
    
    if (f.find('.')!=-1)or(f2.find('.')!=-1):
        ft=float
    else: 
        ft = int 
    if f2=='0':
        fk='Деление на ноль'
        fk2=fk
        delmodul = fk
    else:
        fk= ft(f)/ft(f2)
        fk2=ft(f)//ft(f2)
        delmodul=ft(f)%ft(f2)
    print(f"Складываем: {ft(f)+ft(f2)} \n Вычитаем: {(ft(f))-(ft(f2))} \n Умножаем: {ft(f)*ft(f2)} \n  Делим : {fk}")
    print(f"Возводим в степень: {ft(f)**ft(f2)} \n  Деление по модулю: {delmodul} \n Целочисленное деление: {fk2} ")




def second():
    name= input('Введите ваше имя:')
    print("Привет, "+name+'!')
def third():
    str= input('Введите строку:')
    print(''.join(reversed(str[len(str)-2:len(str)])))
    

def four():
    r=input('Введите радиус круга: ')
    if (r.find('.')!=-1):
        ft=float
    else: 
        ft = int 
    print('S='+str(math.pi*ft(r)*ft(r)))

if __name__ == "__main__":
    first()
    second()
    third()
    four()
