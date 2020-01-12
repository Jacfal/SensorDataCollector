import logging
import signal
import sys
from typing import List

from jsdc.gatherer import Gatherer
from jsdc.helpers.sensor_helpers import create_sensor_from_configuration, create_targets_from_configuration
from jsdc.sensor import Sensor
from jsdc.configuration import load_target_configuration, load_sensor_configuration
from jsdc.target_system import TargetSystem
from jsdc.targets.log_target import LogTarget

gatherers: List[Gatherer] = []


def main():
    argv = sys.argv[1:]

    # args handling
    if "--debug" in argv:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info("Starting application")

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
    signal.signal(signal.SIGINT, stop_app)
    main()

    # keep alive main thread
    while True:
        signal.pause()
