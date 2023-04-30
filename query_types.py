from enum import Enum

import pandas as pd


class SensorQuery(Enum):
    AssignToBuilding = 1
    AssignToBuildingMulti = 2
    AssignToFloors = 3
    AssignToFloorsMulti = 4
    AssignToApartments = 5
    AssignToApartmentsMulti = 6

    @staticmethod
    def list():
        return list(map(lambda c: c, SensorQuery))


def check_building_constraint(sensor_type: str, building_type: str, query: SensorQuery):
    if query in building_constraints[(sensor_type, building_type)]:
        return True
    return False


# Other sensors:
# Seismic, Drone, Satellite, Airplane, GPSTracker, AppTracker, BaseStationTracker

# Create building constraints
# Create sensor constraints
# Match building-sensor constraint peers

building_types = ["ApartmentComplex", "FireStation", "Hospital", "Mall", "PoliceStation", "ReligiousBuildings",
                  "School"]

b_constraints = [
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list()
]

building_sensor_types = ["MotionCS", "BeamCS", "WaterLeakageDetector", "CarbonMonoxideDetector", "SmokeDetector",
                         "MotionDetector", "FireDetector", "CameraSHD", "FaceRecognizer", "CameraPC", "BeamPC",
                         "ElectricityUM", "WaterUM", "GasUM", "MicrophoneDetector", "CarbonDioxideDetector",
                         "MicrowaveRadar"]

bs_constraints = [
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list(),
    SensorQuery.list()
]

building_constraints = {}
# b_c_dict[(key0, key1)]
for sensor_type_idx in range(len(building_sensor_types)):
    for building_type_idx in range(len(building_types)):
        cons_key = (building_sensor_types[sensor_type_idx], building_types[building_type_idx])
        list1 = bs_constraints[sensor_type_idx]
        list2 = b_constraints[building_type_idx]
        building_constraints[cons_key] = [list(set(list1).intersection(list2))]

# print(building_constraints)
