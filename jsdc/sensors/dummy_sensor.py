from logging import getLogger
from random import randint

from jsdc.sensor import Sensor

dummy_sensor_type = "DUMMY_SENSOR"


class DummySensor(Sensor):
    """Dummy sensor for test and dec purposes"""

    __log = getLogger(__name__)

    def get_sensor_type(self):
        return dummy_sensor_type

    def get_sensor_data(self):
        # create dummy data
        return {
            "value_1": randint(1, 100),
            "value_2": randint(1, 100),
            "value_3": randint(1, 100)
        }
