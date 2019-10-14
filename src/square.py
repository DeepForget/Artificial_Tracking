import cv2
import numpy as np
from .shape import Shape

class Square(Shape):
    def __init__(self, opt):
        super(Square, self).__init__(opt)
        self.half_side = self.size

    def move(self):
        super(Square, self).move()
        self.half_side = self.size

    def draw(self, img):
        x, y = self.x, self.y
        half_side = self.half_side
        color = [int(c) for c in self.color]
        edge = self.edge
        black = (0,0,0)
        x_min, y_min, x_max, y_max = self.get_bb()

        img = cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color, -1)
        if edge > 0:
            img = cv2.rectangle(img, (x_min, y_min), (x_max, y_max), black, edge)
        return img

    def get_bb(self):
        x_min = self.x - self.half_side
        y_min = self.y - self.half_side
        x_max = self.x + self.half_side
        y_max = self.y + self.half_side
        return (x_min, y_min, x_max, y_max)
