from os import environ
from typing import List


class SensorConfiguration:
    def __init__(self, sensor_name: str, gathering_interval: int = 1):

        if gathering_interval < 1:
            self._gathering_interval = 1
        else:
            self._gathering_interval = gathering_interval

        self.sensor_name = sensor_name.upper()

    def get_sensor_name(self):
        return self.sensor_name

    def get_sensor_gathering_interval(self):
        return self._gathering_interval


class Configuration:

    @staticmethod
    def load_sensor_configuration() -> List[SensorConfiguration]:
        # only conf loading from env is supported at this time
        return [Configuration._load_sensor_configuration_from_env()]

    @staticmethod
    def _load_sensor_configuration_from_env() -> SensorConfiguration:
        sensor_name = environ['SENSOR_NAME']
        gathering_interval = int(environ['GATHERING_INTERVAL'])

        return SensorConfiguration(sensor_name, gathering_interval)


class TargetConfiguration:
    pass
