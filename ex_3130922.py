# 1.1 Напишите функцию, которая  будет принимать номер  кредитной карты и показывать  только последние 4 цифры.
# Остальные цифры должны заменяться звездочками
def card_hide(card_num):
    card_num = str(card_num)
    return "*" * (len(card_num)-4) + card_num[-4:]

print(card_hide(5456789515658562))

# 1.2 Напишите функцию, которая  проверяет: является ли слово  палиндромом
def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome('summer'))
print(is_palindrome('шалаш'))

# 1.3 Напишите классы Круг,  Прямоугольник, Квадрат.  Каждый класс должен  содержать метод нахождения  площади фигуры.Используйте:
# - Наследование - Абстрактный класс и методы
# - Округлите площадь круга до 2х чисел после запятой - Число π возьмите из модуля math

from abc import ABC, abstractmethod
import math as m


class Figures(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Figures):  # квадрат
    def __init__(self, height):
        self.height = height

    def area(self):
        return "Площадь квадрата = " + str(self.height ** 2)


class Rectangle(Figures):  # Прямоугольник
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return "Площадь прямоугольника = " + str(self.height * self.width)


class Circle(Figures):  # круг
    def __init__(self, height):
        self.radius = height

    def area(self):
        return "Площадь круга = " + str(round(self.radius ** 2 * m.pi, 2))


square = Square(4)
rectangle = Rectangle(2, 6)
circle = Circle(3)
figures = [square, rectangle, circle]

for i in figures:
    print(i.area())