from logging import getLogger
from time import sleep
from threading import Thread, currentThread
from sensor import Sensor


class Gatherer:
    """Sensor data gatherer"""

    def __init__(self, sensor: Sensor):
        self.sensor = sensor
        self.gatherer = Thread(target=self.__gathering)
        self._log = getLogger(self.sensor.get_sensor_type())

    def __gathering(self):
        lt = currentThread()
        while getattr(lt, 'gathering', True):
            self.sensor.send_sensor_data_to_subscribers()
            sleep(self.sensor.get_gathering_interval())

    def start_gathering(self):
        """Start data gathering"""
        self._log.info(f'Gathering started on sensor {self.sensor.get_sensor_type()}')
        self.gatherer.start()

    def stop_gathering(self):
        """Stop data gathering"""
        self._log.info(f'Gathering stopped stopped on sensor {self.sensor.get_sensor_type()}')
        self.gatherer.gathering = False
        self.gatherer.join()
