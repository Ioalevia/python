class Road:
    _road_length = 0
    _road_width = 0
    def __init__(self, road_length, road_width):
        self._road_length = road_length
        self._road_width = road_width
        self._weight = 25
        self._depth = 1
    def calc(self):
        cover = self._road_length * self._road_width * self._weight * self._depth
        print(f'{self._road_length}м * {self._road_width}м * {self._weight}кг * {self._depth}см = {cover // 1000}т')

road1 = Road(50, 500)
road1.calc()

