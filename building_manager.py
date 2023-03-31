import pandas as pd
from building import BaseBuilding
import sensor


class BuildingManager:

    def __init__(self):
        self.dataset = pd.DataFrame()

    def add_building(self, building: BaseBuilding):
        pass  # add dataset