from sensor import Sensor
from target_system import TargetSystem

null_target_type = "NULL_TARGET"


class NullTarget(TargetSystem):
    """
    Null target. For testing and developing purposes
    """

    def send_data(self, sensor_data: dict) -> None:
        print("Data received by " + self.get_target_name() + " :" + sensor_data)

    def get_target_type(self):
        return null_target_type

