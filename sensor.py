from enum import Enum


class Sensor:
    def __init__(self):
        self.speed = 0.0
        self.price = 0.0
        self.detectHuman = False
        self.detectDamage = False
        self.type = None # type will come
        self.subtype = None