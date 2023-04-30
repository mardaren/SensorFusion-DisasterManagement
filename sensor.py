from enum import Enum
import pandas as pd


class Sensor:
    def __init__(self,
                 sid: int = 0,
                 bid: int = 0,
                 is_smart: bool = False,
                 speed: float = 0.0,
                 price: float = 0.0,
                 success: float = 0.0):
        self.sid = sid
        self.bid = bid
        self.category = "Sensor"
        self.type = self.__class__.__name__
        self.is_smart = is_smart
        self.brand = None  # will be added
        self.model = None

        self.speed = speed
        self.price = price
        self.success = success  # based on type

    def print_type(self):
        print(self.type)

    def print_category(self):
        print(self.category)

    def get_df(self):
        return pd.DataFrame([self.__dict__])


class SensorVariation:

    def __init__(self):
        self.hanne = 1



"""***************** LAYER - 1 *****************"""


class DisasterDetector(Sensor):

    def __init__(self, **kwargs):
        super(DisasterDetector, self).__init__(**kwargs)
        self.category = "DisasterDetector"


class SmartHomeDetector(Sensor):

    def __init__(self, **kwargs):
        super(SmartHomeDetector, self).__init__(**kwargs)
        self.category = "SmartHomeDetector"


class PersonTracker(Sensor):

    def __init__(self, **kwargs):
        super(PersonTracker, self).__init__(**kwargs)
        self.category = "PersonTracker"


class AfterEarthquake(Sensor):

    def __init__(self, **kwargs):
        super(AfterEarthquake, self).__init__(**kwargs)
        self.category = "AfterEarthquake"


"""***************** LAYER - 2 *****************"""


class CollapseDetector(DisasterDetector):

    def __init__(self, **kwargs):
        super(CollapseDetector, self).__init__(**kwargs)


class MotionCS(CollapseDetector):

    def __init__(self, **kwargs):
        super(CollapseDetector, self).__init__(**kwargs)


class BeamCS(CollapseDetector):

    def __init__(self, **kwargs):
        super(CollapseDetector, self).__init__(**kwargs)


########################################

class Seismic(DisasterDetector):

    def __init__(self, **kwargs):
        super(Seismic, self).__init__(**kwargs)

########################################


class Airborn(DisasterDetector):

    def __init__(self, **kwargs):
        super(Airborn, self).__init__(**kwargs)


class Drone(Airborn):

    def __init__(self, **kwargs):
        super(Drone, self).__init__(**kwargs)


class Satellite(Airborn):

    def __init__(self, **kwargs):
        super(Satellite, self).__init__(**kwargs)


class Airplane(Airborn):

    def __init__(self, **kwargs):
        super(Airplane, self).__init__(**kwargs)


#################################

class WaterLeakageDetector(SmartHomeDetector):

    def __init__(self, **kwargs):
        super(WaterLeakageDetector, self).__init__(**kwargs)


##################################

class GasDetector(SmartHomeDetector):

    def __init__(self, **kwargs):
        super(GasDetector, self).__init__(**kwargs)


class CarbonMonoxideDetector(GasDetector):

    def __init__(self, **kwargs):
        super(CarbonMonoxideDetector, self).__init__(**kwargs)


class SmokeDetector(GasDetector):

    def __init__(self, **kwargs):
        super(GasDetector, self).__init__(**kwargs)


#######################################

class MotionDetector(SmartHomeDetector):

    def __init__(self, **kwargs):
        super(MotionDetector, self).__init__(**kwargs)


class FireDetector(SmartHomeDetector):

    def __init__(self, **kwargs):
        super(FireDetector, self).__init__(**kwargs)


class CameraSHD(SmartHomeDetector):

    def __init__(self, **kwargs):
        super(CameraSHD, self).__init__(**kwargs)

#######################################


class GPS(PersonTracker):

    def __init__(self, **kwargs):
        super(GPS, self).__init__(**kwargs)


class GPSTracker(GPS):

    def __init__(self, **kwargs):
        super(GPSTracker, self).__init__(**kwargs)


class MobilePhoneTracker(GPS):

    def __init__(self, **kwargs):
        super(MobilePhoneTracker, self).__init__(**kwargs)


class AppTracker(MobilePhoneTracker):

    def __init__(self, **kwargs):
        super(AppTracker, self).__init__(**kwargs)


class BaseStationTracker(MobilePhoneTracker):

    def __init__(self, **kwargs):
        super(BaseStationTracker, self).__init__(**kwargs)


###########################################

class OpticalDetector(PersonTracker):

    def __init__(self, **kwargs):
        super(OpticalDetector, self).__init__(**kwargs)


class FaceRecognizer(OpticalDetector):

    def __init__(self, **kwargs):
        super(FaceRecognizer, self).__init__(**kwargs)


class PeopleCounter(OpticalDetector):

    def __init__(self, **kwargs):
        super(PeopleCounter, self).__init__(**kwargs)


class CameraPC(PeopleCounter):

    def __init__(self, **kwargs):
        super(CameraPC, self).__init__(**kwargs)


class BeamPC(PeopleCounter):

    def __init__(self, **kwargs):
        super(BeamPC, self).__init__(**kwargs)


############################################


class SmartUtilityMeter(PersonTracker):

    def __init__(self, **kwargs):
        super(SmartUtilityMeter, self).__init__(**kwargs)


class ElectricityUM(SmartUtilityMeter):

    def __init__(self, **kwargs):
        super(ElectricityUM, self).__init__(**kwargs)


class WaterUM(SmartUtilityMeter):

    def __init__(self, **kwargs):
        super(WaterUM, self).__init__(**kwargs)


class GasUM(SmartUtilityMeter):

    def __init__(self, **kwargs):
        super(GasUM, self).__init__(**kwargs)


##############################################


class MicrophoneDetector(AfterEarthquake):

    def __init__(self, **kwargs):
        super(MicrophoneDetector, self).__init__(**kwargs)


class CarbonDioxideDetector(AfterEarthquake):

    def __init__(self, **kwargs):
        super(CarbonDioxideDetector, self).__init__(**kwargs)


class MicrowaveRadar(AfterEarthquake):

    def __init__(self, **kwargs):
        super(MicrowaveRadar, self).__init__(**kwargs)
