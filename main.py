
def bytecode(a:list):
    byte=[]
    for i in a:
        byte.append(i.encode())
    return byte
def decodebyte(a:list):
    decode=[]
    for i in a:
        decode.append(i.decode())
    return decode

def  first_problem():
    s=["Как дела?","Good luck have fun", "Nothing to do","Что делаешь"]
    s = bytecode(s)
    print(s)
    print(decodebyte(s))
def second_problem():
    try:
        with open('Input.txt','r') as f:
            Cnum = int(f.readline())
            Hnum = int(f.readline())
            Onum = int(f.readline())
            if Cnum < 0 or Hnum < 0 or Onum <0:
                print("Отрицательными не могут быть молекулы") 
                return -1
            Cnum //= 2
            Hnum //= 6
            otvet=min(Cnum,min(Hnum,Onum))
            with open("Output.txt","w") as g:
                g.write(str(otvet))
            
    except (FileNotFoundError , ValueError):
                print("Проверьте файл")

def third_problem():
    pass

   

if __name__ == "__main__":
    first_problem()
    second_problem()
    third_problem()
    