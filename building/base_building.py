import abc


class BaseBuilding(metaclass=abc.ABCMeta):

    def __init__(self):
        self.id = 0
        self.latitude, self.longitude = 0.0, 0.0
        self.robustness = 0.0
        self.size = 0.0
        self.floor_count = 0
        self.sensor_list = []  # you must get a variable here

