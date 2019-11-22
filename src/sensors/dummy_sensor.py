from logging import getLogger
from src.sensor import Sensor

dummy_sensor_type = "DUMMY_SENSOR"


class DummySensor(Sensor):
    """Dummy sensor for test and dec purposes"""

    __log = getLogger(__name__)

    def get_sensor_type(self):
        return dummy_sensor_type

    def get_sensor_data(self):
        # create dummy data
        return {
            "value_1": "1",
            "value_2": "2",
            "value_3": "3"
        }
