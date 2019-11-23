from abc import ABC, abstractmethod
from event import Event


class Sensor(ABC):
    """Sensor super class"""

    __on_send_data: Event = Event()

    __gathering_interval: int = 1

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

    def send_sensor_data_to_subscribers(self):
        """Read sensor data with get_sensor_data() method an send them to registered subscribers"""
        self.__on_send_data(self.get_sensor_data())

    def add_sensor_data_subscriber(self, object_method) -> None:
        """Attach a target system to the sensor

        :param object_method:
        :return: None
        """
        self.__on_send_data += object_method

    def remove_sensor_data_subscriber(self, object_method) -> None:
        """Remove a target system from the sensor

        :param object_method:
        :return: None
        """
        self.__on_send_data -= object_method

    def set_gathering_interval(self, gathering_interval: int) -> None:
        """Set gathering interval

        :param gathering_interval:
        :return: None
        """
        if gathering_interval < 0:
            raise ValueError("Invalid value of gathering interval")

        self.__gathering_interval = gathering_interval

    def get_gathering_interval(self) -> int:
        """Get gathering interval

        :return: int
        """
        return self.__gathering_interval
