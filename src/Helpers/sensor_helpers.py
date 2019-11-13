from configuration import SensorConfiguration, TargetConfiguration
from sensors.dummy import Dummy, dummy_sensor_name


def create_sensor_from_configuration(sensor_configuration, target_configuration):
    if not isinstance(sensor_configuration, SensorConfiguration):
        raise TypeError("Invalid type of sensor configuration")
    elif not isinstance(target_configuration, TargetConfiguration):
        raise TypeError("Invalid type of target configuration")

    sensor_configuration = SensorConfiguration(sensor_configuration)
    target_configuration = TargetConfiguration(target_configuration)

    sensor = None
    if sensor_configuration.get_sensor_name() is dummy_sensor_name:
        sensor = Dummy

    return sensor
