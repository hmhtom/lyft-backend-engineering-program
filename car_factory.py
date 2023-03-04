from car_component.engine.capulet_engine import CapuletEngine
from car_component.engine.willoughby_engine import WilloughbyEngine
from car_component.engine.sternman_engine import SternmanEngine
from car_component.battery.nubbin_battery import NubbinBattery
from car_component.battery.sindler_battery import SindlerBattery
from car import Car


class CarFactory:

    def create_calliope(current_mileage, last_service_mileage, current_date, last_service_date):
        calliope = Car(CapuletEngine(current_mileage, last_service_mileage),
                       SindlerBattery(current_date, last_service_date))
        return calliope

    def create_glissade(current_mileage, last_service_mileage, current_date, last_service_date):
        glissade = Car(WilloughbyEngine(current_mileage, last_service_mileage),
                       SindlerBattery(current_date, last_service_date))
        return glissade

    def create_rorschach(current_mileage, last_service_mileage, current_date, last_service_date):
        rorschach = Car(WilloughbyEngine(current_mileage, last_service_mileage),
                        NubbinBattery(current_date, last_service_date))
        return rorschach

    def create_thovex(current_mileage, last_service_mileage, current_date, last_service_date):
        thovex = Car(CapuletEngine(current_mileage, last_service_mileage),
                     NubbinBattery(current_date, last_service_date))
        return thovex

    def create_palindrome(warning_light_is_on, current_date, last_service_date):
        palindrome = Car(SternmanEngine(warning_light_is_on),
                         SindlerBattery(current_date, last_service_date))
        return palindrome