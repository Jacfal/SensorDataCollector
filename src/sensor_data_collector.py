import logging
from typing import List
from helpers.sensor_helpers import create_sensor_from_configuration, create_targets_from_configuration
from sensor import Sensor
from src.configuration import load_target_configuration, load_sensor_configuration
from target_system import TargetSystem
from targets.log_target import LogTarget


def main():
    logging.basicConfig(level=logging.NOTSET)

    targets: List[TargetSystem] = create_targets_from_configuration(load_target_configuration())
    sensors: List[Sensor] = create_sensor_from_configuration(load_sensor_configuration())

    # add targets to sensors
    for sensor in sensors:
        log_target: LogTarget = LogTarget("defaultLogger")

        sensor.add_sensor_data_subscriber(log_target.send_data)
        sensor.send_sensor_data_to_subscribers()

    # sensor_configuration = Configuration.load_sensor_configuration()

    # for conf in sensor_configuration:
    #    sensor: Sensor = create_sensor_from_configuration(conf, None)
    #    sensor.start_gathering()

    raise NotImplementedError


if __name__ == "__main__":
    main()
