

class Animals:

    def __init__(self, name_animal, age=0) -> None:
        self.name_animal = name_animal
        self.age = age


class Mammals(Animals):

    def __init__(self, name_animal, age, gender) -> None:
        super().__init__(name_animal, age)
        self.gender = gender

    def hello_iam_mammals(self)-> None:
        print(f"Я животное - млекопитающие,{self.name_animal} , мне {self.age} лет!")


class Human(Mammals):

    def __init__(self, name_animal, age, gender, name) -> None:
        super().__init__(name_animal, age, gender)
        self.name = name
        self.prava = 'Net y teb9 prav'

    def say_hello(self) -> None:
        print(f"Привет, я {self.name_animal},меня зовут {self.name} ,у меня есть права!")
        print(f"-{self.prava}")


class Cat(Mammals):
    def __init__(self, name_animal, age, gender, name) -> None:
        super().__init__(name_animal, age, gender)
        self.name = name

    def info(self) -> None:
        print(f'My name {self.name}, age - {self.age}')

    def make_sound(self) -> None:
        print('Meow')


class Dog(Mammals):
    def __init__(self, name_animal, age, gender, name) -> None:
        super().__init__(name_animal, age, gender)
        self.name = name

    def info(self) -> None:
        print(f'My name {self.name}, age - {self.age}')

    def make_sound(self) -> None:
        print('Gav')


class Student(Human):

    def __init__(self, name_animal, age, gender, name, homework_complete=0) -> None:
        super().__init__(name_animal, age, gender, name)
        self.homework_complete = homework_complete

    def say_student(self) -> None:
        print(f'Я студент , звать меня {self.name}')

    def __eq__(self, other) -> str:
        if self.homework_complete == other.homework_complete:
            return 'Коливчество выполненых домашних заданий равны'
        return 'Коливчество выполненых домашних заданий не равны'

    def __lt__(self, other)-> str:
         if self.homework_complete < other.homework_complete:
              return f'Коливчество выполненых домашних заданий больше у {other.name}'
         return f'Коливчество выполненых домашних заданий больше у {self.name}'

    def __gt__(self, other) -> str:
         if self.homework_complete > other.homework_complete:
               return f'Коливчество выполненых домашних заданий больше у {self.name}'
         return f'Коливчество выполненых домашних заданий больше у {other.name}'
         
    def __le__(self, other) -> str:
        if self.homework_complete >= other.homework_complete:
            return 'У кого-то больше , а может и равны'
        return f'У {other.name} больше выолненых дз'

    def __ge__(self, other) -> str:
          if self.homework_complete <= other.homework_complete:
            return 'У кого-то больше , а может и равны'
          return f'У {self.name} больше выолненых дз'  