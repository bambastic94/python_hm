"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные
методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class TypedProperty:
    def __init__(self, name, type_name):
        self.name = "_" + name
        self.type = type_name

    def __get__(self, instance, cls):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Значение должно быть типа %s" % self.type)
        setattr(instance, self.name, value)


class Worker:
    name = TypedProperty("name", str)
    surname = TypedProperty("surname", str)
    position = TypedProperty("position", str)

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(self._income.get("wage") + self._income.get("bonus"))


a = Position("George", 122312, "Gardener", 123123, 1555)
a.get_full_name()
print(a.position)
a.get_total_income()
