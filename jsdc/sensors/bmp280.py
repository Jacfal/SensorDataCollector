import bme280
from logging import getLogger
from smbus2 import smbus2

from jsdc.sensor import Sensor

bmp280_sensor_type = "BMP280_SENSOR"


class Bmp280(Sensor):
    """BMP 280 sensor"""
    __log = getLogger(__name__)

    def __init__(self, port: int, address: int):
        bus = smbus2.SMBus(port)
        calibration_params = bme280.load_calibration_params(bus, address)
        self.data = bme280.sample(bus, address, calibration_params)

    def get_sensor_type(self):
        return bmp280_sensor_type

    def get_sensor_data(self):
        # create dummy data
        return {
            "temperature": self.data.temperature,
            "pressure": self.data.pressure
        }
