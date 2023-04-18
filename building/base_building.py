import abc
import pandas as pd

from query_types import SensorQuery


class BaseBuilding(metaclass=abc.ABCMeta):

    def __init__(self):
        self.id = 0
        self.latitude, self.longitude = 0.0, 0.0
        self.robustness = 0.0
        self.size = 0.0
        self.floor_count = 0
        self.sensor_list = []  # you must get a variable here
        self.type = self.__class__.__name__
        self.available_queries = []

    def get_df(self):
        return pd.DataFrame([self.__dict__])

    def check_constraints(self, query: SensorQuery):
        if query in self.available_queries:
            return True
        else:
            print("Building-Sensor constraints not matched!")
            return False
