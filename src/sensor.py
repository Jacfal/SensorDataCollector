from abc import ABC, abstractmethod


class Sensor(ABC):
    """Sensor super class"""

    @abstractmethod
    def get_sensor_name(self):
        """Gets sensor name

        :return: a sensor name
        :rtype: str
        """
        pass

    @abstractmethod
    def get_sensor_data(self):
        """Sensor reads the data a returned them as a dictionary

        :return: sensor data
        :rtype: dict
        """

        pass
