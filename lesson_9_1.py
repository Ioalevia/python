import time
import itertools
class  TrafficLight:
    __color = ['красный', 'жёлтый', 'зеленый']
    def running(self):
        for color in itertools.cycle(self.__color):
            if color == self.__color[0]:
                print(self.__color[0])
                time.sleep(7)
            elif color == self.__color[1]:
                print(self.__color[1])
                time.sleep(2)
            elif color == self.__color[2]:
                print(self.__color[2])
                time.sleep(4)
light = TrafficLight()
light.running()