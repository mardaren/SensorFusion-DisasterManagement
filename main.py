import sensor
import building
import pandas as pd

def main():
    s0 = sensor.Airplane(sid=0)
    s1 = sensor.CarbonMonoxideDetector(sid=1)

    b0 = building.School()
    b0.sensor_list = [s0.sid, s1.sid]

    sensors = pd.DataFrame()
    sensors = pd.concat([sensors, s0.get_df()], ignore_index=True)
    sensors = pd.concat([sensors, s1.get_df()], ignore_index=True)

    buildings = pd.DataFrame()
    buildings = pd.concat([buildings, b0.get_df()], ignore_index=True)

    print(buildings)
    print(sensors)


if __name__ == '__main__':
    main()
