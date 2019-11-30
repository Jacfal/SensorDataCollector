import logging
import signal
import sys
from typing import List

from gatherer import Gatherer
from helpers.sensor_helpers import create_sensor_from_configuration, create_targets_from_configuration
from sensor import Sensor
from configuration import load_target_configuration, load_sensor_configuration
from target_system import TargetSystem
from targets.log_target import LogTarget

# todo_list:
# TODO signal handler - SIGHUP
# TODO better logging
# TODO makefile
# TODO real sensor implementation

gatherers: List[Gatherer] = []


def main():
    logging.basicConfig(level=logging.NOTSET)

    targets: List[TargetSystem] = create_targets_from_configuration(load_target_configuration())
    sensors: List[Sensor] = create_sensor_from_configuration(load_sensor_configuration(), targets)

    # add targets to sensors
    for sensor in sensors:
        log_target: LogTarget = LogTarget('defaultLogger')

        sensor.add_sensor_data_subscriber(log_target.send_data)

        gatherer: Gatherer = Gatherer(sensor)
        gatherer.start_gathering()

        gatherers.append(gatherer)


def stop_app(signal_code: int, frame: int):
    logging.info("Stopping application")

    for gatherer in gatherers:
        gatherer.stop_gathering()

    logging.info("Successfully stopped")
    sys.exit()


if __name__ == "__main__":
    # register the signals to be caught
    signal.signal(signal.SIGTERM, stop_app)
    main()
