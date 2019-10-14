import cv2
import numpy as np
from numpy.random import choice
from src.circle import Circle
from src.square import Square
from opt import opt

class Canvas(object):
    def __init__(self, number=opt.number, opt=opt, background=None):
        choices = np.array(opt.shapes).reshape(-1)
        shapes = [Circle, Square]
        assert np.max(choices) < len(shapes)
        self.objects = [shapes[choice(choices)](opt) for i in range(number)]
        if background is None:
            self.background = np.zeros((opt.height, opt.width, 3), np.uint8) + 255
        else:
            img = cv2.imread(background)
            assert (img is not None)
            self.background = cv2.resize(img, (opt.width, opt.height), interpolation=cv2.INTER_AREA)

    def draw(self, show_meta=False):
        img = self.background.copy()
        for obj in self.objects:
            img = obj.draw(img)
            if show_meta:
                img = obj.draw_meta(img)
        return img

    def get_meta(self):
        meta = []
        for obj in self.objects:
            meta.append(obj.get_bb(), obj.id)
        return meta

    def move(self):
        for obj in self.objects:
            obj.move()
