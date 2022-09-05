# 14.1 Создать класс Dog. Класс имеет четыре атрибута: height,
# weight, name, age. Класс имеет три метода: jump, run, bark. Каждый
# метод выводит сообщение на экран. Создать объект класса Dog, вызвать все
# методы объекта и вывести на экран все его атрибуты.

# class Dog:
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.age = age
#         self.name = name
#
#     def jump(self):
#         print(self.name, "прыгать!")
#     def run(self):
#         print(self.name, "бегать!")
#     def dark(self):
#         print(self.name, "гавкать :(")
#
# bobik = Dog(30, 60, "Бобик", 2)
# bobik.run()
# bobik.jump()
# bobik.dark()
# print(bobik.name, bobik.height, bobik.weight, bobik.age)

# 14.2 Добавить в класс Dog метод change_name. Метод принимает на вход новое
# имя и меняет атрибут имени у объекта. Создать один объект класса.
# Вывести имя. Вызвать метод change_name. Вывести имя

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.age = age
        self.name = name

    def jump(self):
        print(self.name, "прыгать!")
    def run(self):
        print(self.name, "бегать!")
    def bark(self):
        print(self.name, "гавкать :(")
    def change_name(self, name):
        self.name = name

sharik = Dog(90, 60, "Бобик", 90)
print(sharik.name)
sharik.change_name("Шарик")
print(sharik.name)
