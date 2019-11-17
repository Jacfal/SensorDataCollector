from sensor import Sensor
from target_system import TargetSystem


class Null(TargetSystem):
    """
    Null target. For testing and developing purposes
    """

    def send_data(self, sensor_data: dict) -> None:
        print("Data received by " + self.get_target_name() + " :" + sensor_data)

    def get_target_name(self):
        return "NULL_TARGET"

