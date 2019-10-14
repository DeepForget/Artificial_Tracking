import cv2
import numpy as np
from .shape import Shape

class Circle(Shape):
    def __init__(self, opt):
        super(Circle, self).__init__(opt)
        self.radius = int(round(1.273 * self.size))

    def move(self):
        super(Circle, self).move()
        self.radius = int(round(1.273 * self.size))

    def draw(self, img):
        x, y = self.x, self.y
        radius = self.radius
        color = [int(c) for c in self.color]
        edge = self.edge
        black = (0,0,0)

        img = cv2.circle(img, (x, y), radius, color, -1)
        if edge > 0:
            img = cv2.circle(img, (x, y), radius, black, edge)
        return img

    def get_bb(self):
        x_min = self.x - self.radius
        y_min = self.y - self.radius
        x_max = self.x + self.radius
        y_max = self.y + self.radius
        return (x_min, y_min, x_max, y_max)
