from Helpers.sensor_helpers import create_sensor_from_configuration
from sensor import Sensor
from src.configuration import Configuration


def main():
    sensor_configuration = Configuration.load_sensor_configuration()

    for conf in sensor_configuration:
        sensor: Sensor = create_sensor_from_configuration(conf, None)
        sensor.start_gathering()

    raise NotImplementedError


if __name__ == "__main__":
    main()
