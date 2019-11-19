from logging import getLogger
from abc import ABC, abstractmethod
from typing import List


class Sensor(ABC):
    """Sensor super class"""

    _log = getLogger(__name__)
    _target_systems: List[str] = []
    _gathering_interval: int = 1

    @abstractmethod
    def get_sensor_type(self) -> str:
        """Gets sensor name

        :return: a sensor name
        :rtype: str
        """
        pass

    @abstractmethod
    def get_sensor_data(self) -> dict:
        """Sensor reads the data a returned them as a dictionary

        :return: sensor data
        :rtype: dict
        """
        pass

    def add_target_system(self, target_name: str) -> None:
        """Attach a target system to the sensor

        :param target_name:
        :return: None
        """
        self._target_systems.append(target_name)

    def remove_target_system(self, target_name: str) -> None:
        """Remove a target system from the sensor

        :param target_name:
        :return: None
        """
        self._target_systems.remove(target_name)

    def set_gathering_interval(self, gathering_interval: int) -> None:
        """Set gathering interval

        :param gathering_interval:
        :return: None
        """
        if gathering_interval < 0:
            raise ValueError("Invalid value of gathering interval")

        self._gathering_interval = gathering_interval

    def get_gathering_interval(self) -> int:
        """Get gathering interval

        :return: int
        """
        return self._gathering_interval

    def start_gathering(self) -> None:
        pass

    def stop_gathering(self) -> None:
        pass
