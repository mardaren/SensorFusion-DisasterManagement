import sensor
import pandas as pd

def main():
    s0 = sensor.Airplane(sid=0)
    s1 = sensor.CarbonMonoxideDetector(sid=1)

    # s1.print_type()
    # s1.print_category()

    sensors = pd.DataFrame()
    sensors = pd.concat([sensors, s0.get_df()], ignore_index=True)
    sensors = pd.concat([sensors, s1.get_df()], ignore_index=True)

    print(sensors)


if __name__ == '__main__':
    main()
