class Pikachu:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    @property
    def height(self):
        return self._height
    @property
    def width(self):
        return self._width

class Pichu:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    @property
    def height(self):
        return self._height
    @property
    def width(self):
        return self._width



class Program:
    pikachu = Pikachu(26, 30)
    print(pikachu.height, pikachu.width)
