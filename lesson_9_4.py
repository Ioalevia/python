class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        if direction == 'right':
            print(f'Машина повернула направо')
        elif direction == 'left':
            print(f'Машина повернула налево')
    def show_speed(self):
        print(f'скорость {self.speed}км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed}км/ч! Превышение скорости!')
        else:
            print(f'скорость {self.speed}км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed}км/ч! Превышение скорости!')
        else:
            print(f'скорость {self.speed}км/ч')

class PoliceCar(Car):
    pass

car = Car(120, 'green', 'McLaren')
print(f'скорость: {car.speed}км/ч, цвет: {car.color}, название: {car.name}, состоит в полиции: {car.is_police}')
car.go()
car.stop()
car.turn('right')
car.show_speed()

t_car = TownCar(65, 'red', 'Audi')
print(f'скорость: {t_car.speed}км/ч, цвет: {t_car.color}, название: {t_car.name}, состоит в полиции: {t_car.is_police}')
t_car.go()
t_car.stop()
t_car.turn('left')
t_car.show_speed()

s_car = SportCar(80, 'black', 'BMW')
print(f'скорость: {s_car.speed}км/ч, цвет: {s_car.color}, название: {s_car.name}, состоит в полиции: {s_car.is_police}')
s_car.go()
s_car.stop()
s_car.turn('right')
s_car.show_speed()

w_car = WorkCar(35, 'brown', 'Kia')
print(f'скорость: {w_car.speed}км/ч, цвет: {w_car.color}, название: {w_car.name}, состоит в полиции: {w_car.is_police}')
w_car.go()
w_car.stop()
w_car.turn('left')
w_car.show_speed()

p_car = PoliceCar(100, 'blue', 'Ford', True)
print(f'скорость: {p_car.speed}км/ч, цвет: {p_car.color}, название: {p_car.name}, состоит в полиции: {p_car.is_police}')
p_car.go()
p_car.stop()
p_car.turn('right')
p_car.show_speed()