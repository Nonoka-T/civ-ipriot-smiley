from smiley import Smiley


class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_eyes()
        self.draw_mouth()

    def draw_mouth(self):
        mouth = [42, 43, 44, 45, 50, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self):
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK