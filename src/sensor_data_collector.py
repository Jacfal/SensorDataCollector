from typing import List

from helpers.sensor_helpers import create_sensor_from_configuration, create_targets_from_configuration
from sensor import Sensor
from src.configuration import load_target_configuration, load_sensor_configuration
from target_system import TargetSystem


def main():
    targets: List[TargetSystem] = create_targets_from_configuration(load_target_configuration())
    sensors: List[Sensor] = create_sensor_from_configuration(load_sensor_configuration())

    # sensor_configuration = Configuration.load_sensor_configuration()

    # for conf in sensor_configuration:
    #    sensor: Sensor = create_sensor_from_configuration(conf, None)
    #    sensor.start_gathering()

    raise NotImplementedError


if __name__ == "__main__":
    main()
