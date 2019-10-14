import cv2
import numpy as np
from numpy.random import randint, uniform

class Shape(object):
    _id = 0
    def __init__(self, opt):
        self.opt = opt
        self.x = randint(0, opt.width)
        self.y = randint(0, opt.height)
        self.vx = randint(-opt.max_x_speed, opt.max_x_speed+1)
        self.vy = randint(-opt.max_y_speed, opt.max_y_speed+1)

        self.color = randint(0, 256, 3)
        self.size = randint(opt.min_size, opt.max_size)

        if opt.random_edge:
            self.edge = randint(0, 3)
        else:
            self.edge = 1

        self.id = Shape._id
        Shape._id += 1

    def draw(self, image):
        raise NotImplemented

    def draw_meta(self, image):
        bb = self.get_bb()
        cv2.rectangle(image, (bb[0], bb[1]), (bb[2], bb[3]), (255, 0, 0), 2)
        font = self.opt.font
        font_size = self.opt.font_size
        space = self.opt.space
        cv2.putText(image, str(self.id), (bb[0], bb[1]-space), font, font_size, (255,0,0), 1)
        return image

    def get_bb(self):
        raise NotImplemented

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # bounce on edge
        if self.x > self.opt.width or self.x < 0:
            self.x = max(min(self.x, self.opt.width), 0)
            self.vx = -self.vx
        if self.y > self.opt.height or self.y < 0:
            self.y = max(min(self.y, self.opt.height), 0)
            self.vy = -self.vy

        max_acc = self.opt.max_acc

        self.vx += randint(-max_acc, max_acc+1)
        max_x_speed = self.opt.max_x_speed
        self.vx = min(max(self.vx, -max_x_speed), max_x_speed)

        self.vy += randint(-max_acc, max_acc+1)
        max_y_speed = self.opt.max_y_speed
        self.vy = min(max(self.vy, -max_y_speed), max_y_speed)

        max_size_change = self.opt.max_size_change
        self.size += randint(-max_size_change, max_size_change+1)
        self.size = min(self.size, self.opt.max_size)
        self.size = max(self.size, self.opt.min_size)

        max_color_change = self.opt.max_color_change
        self.color += randint(-max_color_change, max_color_change+1, 3)
        self.color = np.clip(self.color, 0, 255)

        if self.opt.random_edge:
            if uniform() < self.opt.p_change_edge:
                self.edge += randint(-1, 2)
                self.edge = min(max(self.edge, 0), 2)
