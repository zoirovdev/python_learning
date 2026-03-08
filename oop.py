class ClassName:
    pass

class Ignore:
    """class example"""
    i = 12453

    def f():
        print('Hello world')


class Toplam:
    "just a sample class"
    def __init__(self):
        self.data = []

    def add(self, new_mem:int):
        self.data.append(new_mem)
        return new_mem
    
    def remove(self, indx: int):
        n = self.data.pop(indx)
        return n
    
    def all(self)->list:
        return self.data




class Car:
    def __init__(self, model, manufacturer, color):
        self.model = model
        self.manufacturer = manufacturer
        self.color = color

    def start(self):
        print(self.model, 'has been ignited!')

    
    def stop(self):
        print(self.model, 'has been stopped!')



class Tesla(Car):
    def __init__(self, model, manufacturer, color):
        super().__init__(model, manufacturer, color)


    def auto_drive(self):
        print('Tesla driving itself!')




class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('Animal started walking')

    def eat(self):
        print('Animal started eating')

    def run(self):
        print('Animal is running')

    def get_name(self):
        print(self.name)

    
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    age: int


# employee = Employee()
# employee.name = 'Husniddin'
# employee.age = 21
# employee.dept = 'Accounting'

# print(employee)




# s = 'andsbd'
# it = iter(s)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next((it)))



class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index-1
        return self.data[self.index]
    
rev = Reverse('data manipulation')


