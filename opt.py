import cv2

class Opt(object):
    pass

opt = Opt()
opt.number = 15
opt.shapes = (0, 1) # 0=circle, 1=square
opt.width = 1080
opt.height = 640
opt.max_x_speed = 8
opt.max_y_speed = 5
opt.max_acc = 1
opt.min_size = 8
opt.max_size = 30
opt.max_size_change = 2
opt.random_edge = True
opt.p_change_edge = 0.1
opt.max_color_change = 10
opt.font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
opt.font_size = 0.5
opt.space = 5
