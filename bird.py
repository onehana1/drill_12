import game_framework
from pico2d import *
from ball import Ball

import random

# bird Run Speed
PIXEL_PER_METER = (10.0 / 1.0)  # 10 pixel 100 cm
RUN_SPEED_KMPH = 100.0  # Km / Hour #시속 100km
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# bird Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 14  # 14개의 날개짓이 있기 때문에
FRAMES_PER_ACTION = 1  # 시간당 1번의 날개짓을 하고 14개 종류의 날개짓을 수행한다.


class Bird:

    def __init__(self):
        self.x, self.y = random.randint(0, 1600), 300
        self.image = load_image('bird100x100x14.png')

        self.dir = 1
        self.velocity = 0
        self.jump_timer = 0
        self.frame = 0
        self.timer = 0


    def get_bb(self):
        if(self.x == 1600):
            self.dir +=1
            return 0

    def do(self):
        pass

    def update(self):

        self.velocity = 0

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14



        if ((self.dir % 2) == 1):
                self.velocity += RUN_SPEED_PPS
                self.x += self.velocity * game_framework.frame_time
        else:
                self.velocity -= RUN_SPEED_PPS
                self.x += self.velocity * game_framework.frame_time

        if (self.x >= 1600):
                self.dir += 1

        if (self.x <= 0):
                self.dir += 1



    def draw(self):
        if ((self.dir % 2) == 1):
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100,3.14,'v', self.x, self.y,100,100)

