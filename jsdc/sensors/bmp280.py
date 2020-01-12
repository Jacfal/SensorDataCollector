import bme280
from logging import getLogger
from smbus2 import smbus2

from jsdc.sensor import Sensor

bmp280_sensor_type = "BMP280_SENSOR"


class Bmp280(Sensor):
    """BMP 280 sensor"""
    __log = getLogger(__name__)

    def __init__(self, port: int = 1, address: int = 0x76):
        """
        Init BMP280 sensor
        :param port: sensor port (default 1)
        :param address: sensor address (default 0x76)
        """
        self.address = address
        self.port = port
        self.bus = smbus2.SMBus(port)
        self.__log.info(f'Initializing BMP280 sensor => port {port}, address {address}')

    def get_sensor_type(self):
        return bmp280_sensor_type

    def get_sensor_data(self):
        calibration_params = bme280.load_calibration_params(self.bus, self.address)
        data = bme280.sample(self.bus, self.address, calibration_params)

        return {
            "temperature": data.temperature,
            "pressure": data.pressure
        }
