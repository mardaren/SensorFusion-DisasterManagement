from building import BaseBuilding
from query_types import SensorQuery


class ApartmentComplex(BaseBuilding):

    def __init__(self):
        super().__init__()
        self.available_queries = [SensorQuery.AssignToBuilding, SensorQuery.AssignToFloors,
                                  SensorQuery.AssignToFloorsMulti]

