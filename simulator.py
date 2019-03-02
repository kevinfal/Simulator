import pygame
import math
import time


class creature(object):
    def __init__(self):
        self.health = 100


class tile(object):
    def __init__(self):
        self.id = 0

    def __init__(self,num):
        self.num = num
