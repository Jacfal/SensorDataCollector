from abc import ABC, abstractmethod

from target_system import TargetSystem


class Sensor(ABC):
    """Sensor super class"""

    def __init__(self):
        self._target_systems = []
        self._gathering_interval = 1

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

    def add_target_system(self, target_system):
        if not isinstance(target_system, TargetSystem):
            raise TypeError("Invalid input data type")

        self._target_systems.append(target_system)

    def set_gathering_interval(self, gathering_interval):
        if not isinstance(gathering_interval, int):
            raise TypeError("Mut be type of int")

        self._gathering_interval = gathering_interval

    def get_gathering_interval(self):
        return self._gathering_interval
