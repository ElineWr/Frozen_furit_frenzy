

class Object:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image


class Food(Object):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    

class Isbjorn(Object):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)


