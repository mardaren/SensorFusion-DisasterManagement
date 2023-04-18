import copy

import pandas as pd

import sensor
import building

from query_types import SensorQuery


class SensorManager:

    def __init__(self):  # obje olarak tut ama pandas olarak print eyle
        # self.sensors = []
        self.buildings = {}

        self.sensorDB = pd.DataFrame()
        self.buildingDB = pd.DataFrame()
        self.sensor_id = 0
        self.building_id = 0

    def add_sensor(self, sensor_instance: sensor.Sensor, bid: int):
        sensor_clone = copy.deepcopy(sensor_instance)

        # change id of the sensor
        sensor_clone.sid = self.sensor_id
        self.sensor_id += 1
        sensor_clone.bid = bid

        # add sensor to the building
        self.buildings[bid].sensor_list.append(sensor_clone.sid)
        self.buildingDB.iloc[bid] = self.buildings[bid].get_df()

        self.sensorDB = pd.concat([self.sensorDB, sensor_clone.get_df()], ignore_index=True)

    def add_building(self, building_instance: building.BaseBuilding):
        building_clone = copy.deepcopy(building_instance)

        # change id of the sensor
        building_clone.id = self.building_id
        self.building_id += 1

        self.buildings[building_clone.id] = building_clone
        self.buildingDB = pd.concat([self.buildingDB, building_clone.get_df()], ignore_index=True)

    def sensor_query(self, sensor_instance: sensor.Sensor, bid: int, query: SensorQuery,
                     value: int = 0):
        target_building = self.buildings[bid]
        if target_building.check_constraints(query=query):
            match query:
                case SensorQuery.AssignToBuilding:
                    self.add_sensor(sensor_instance, bid)
                case SensorQuery.AssignToBuildingMulti:
                    for i in range(value):
                        self.add_sensor(sensor_instance, bid)
                case SensorQuery.AssignToFloors:
                    for i in range(target_building.floor_count):
                        self.add_sensor(sensor_instance, bid)
                case SensorQuery.AssignToFloorsMulti:
                    for i in range(target_building.floor_count * value):
                        self.add_sensor(sensor_instance, bid)
