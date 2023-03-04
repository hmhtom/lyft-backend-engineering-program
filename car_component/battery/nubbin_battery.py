from abc import ABC
from car_component.BatteryInterface import Battery
from datetime import datetime


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
