#  Задание 1
from itertools import cycle
from time import sleep

class Traffic_Light:
        def __init__(self):
            self.color = (('Red', 5), ('Yellow', 2), ('Green', 10))
        def running(self):
            for color, sec in cycle(self.__color):
                print(color, '(Wait {} sec)'.format(sec))
                sleep(sec)
traffic_light = Traffic_Light()
traffic_light.running()

# Задание 2

class Roads:
        def __init__(self, width, length):
            self.width = width
            self.length = length
        def calc_mass(self):
            mass = self.length * self.width * 25 * 5 / 1000
            return mass
my_road = Roads(5000, 20)
print(my_road.calc_mass(), 'т.')


# Задание 3

class Worker:
    def __init__(self, name, surname,position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wages = income['зарплата']
        self._income_bonus = income['бонус']
class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'
    def get_total_res(self):
        return self._income_wages + self._income_bonus

pos = Position('Алексей', 'Калачёв', 'Студент', {'зарплата': 99999, 'бонус': 12345.6})
print(pos.get_full_name())
print(pos.get_total_res())

# Задание 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! Your speed is more than max!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Warning! Your speed is more than max!')


class PoliceCar(Car):
    pass


sport_car = SportCar(240, 'Синий', 'Мустанг', False)
town_car = TownCar(140, 'Красная', 'Тайота', False)
work_car = WorkCar(90, 'Черный', 'Мерседес', False)
police_car = PoliceCar(210, 'Белая', 'Лада', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')

# Задача 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка рисует')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер рисуте')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()