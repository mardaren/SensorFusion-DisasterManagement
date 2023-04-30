import sensor
import building
import pandas as pd
from sensor_manager import SensorManager
from query_types import SensorQuery
import query_types

def main():
    # s0 = sensor.Airplane(sid=0)
    # s1 = sensor.CarbonMonoxideDetector(sid=1)
    #
    # b0 = building.ApartmentComplex()
    # b0.floor_count = 4
    #
    # b1 = building.ApartmentComplex()
    #
    # manager = SensorManager()
    #
    # manager.add_building(b0)
    # manager.add_building(b1)
    #
    # manager.sensor_query(s1, 0, SensorQuery.AssignToFloors)
    # manager.sensor_query(s1, 1, SensorQuery.AssignToBuilding)
    #
    # # print(manager.buildings[1].get_df())
    # # print(manager.buildingDB.type)
    # print(manager.sensorDB.columns)
    pass


if __name__ == '__main__':
    main()
