import copy

import pandas as pd

import sensor
import building

from query_types import SensorQuery, building_constraints


class DatabaseManager:

    def __init__(self):  # obje olarak tut ama pandas olarak print eyle
        self.buildings = {}
        self.building_constraints = building_constraints
        self.floors = {}
        self.apartment = {}
        self.persons = {}
        self.sensors = {}
        self.sensor_variations = {}
        self.base_stations = {}
        self.air_gadgets = {}

        # We dont need these
        self.sensor_counter = 0
        self.variation_counter = 0
        self.building_counter = 0
        self.person_counter = 0


    def add_variation(self, bilmem):
        pass
