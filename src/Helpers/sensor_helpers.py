from configuration import SensorConfiguration, TargetConfiguration
from sensor import Sensor
from sensors.dummy import Dummy, dummy_sensor_name


def create_sensor_from_configuration(sensor_configuration: SensorConfiguration,
                                     target_configuration: TargetConfiguration) -> Sensor:

    sensor = None
    if sensor_configuration.get_sensor_name() == dummy_sensor_name:
        sensor = Dummy

    return sensor
